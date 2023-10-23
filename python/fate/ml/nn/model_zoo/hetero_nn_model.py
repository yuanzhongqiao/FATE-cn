import torch
import torch as t
from fate.arch import Context
from fate.ml.nn.model_zoo.agg_layer.plaintext_agg_layer import InteractiveLayerGuest, InteractiveLayer
from fate.ml.nn.model_zoo.agg_layer.plaintext_agg_layer import InteractiveLayerHost


def backward_loss(z, backward_error):
    return t.sum(z * backward_error)


class HeteroNNModelGuest(t.nn.Module):

    def __init__(self,
                 top_model: t.nn.Module,
                 interactive_layer: InteractiveLayerGuest,
                 bottom_model: t.nn.Module = None,
                 ):

        super(HeteroNNModelGuest, self).__init__()
        self._bottom_model = bottom_model
        self._top_model = top_model
        self._interactive_layer = interactive_layer

        # cached variables
        self._bottom_fw = None  # for backward usage
        self._interactive_fw_rg = None # for backward usage

        # ctx
        self._ctx = None

        # internal mode
        self._guest_direct_backward = True

    def __repr__(self):
        return (f"HeteroNNGuest(top_model={self._top_model}\n"
                f"interactive_layer={self._interactive_layer}\n"
                f"bottom_model={self._bottom_model})")

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)

    def _clear_state(self):
        self._bottom_fw = None
        self._interactive_fw_rg = None

    def set_context(self, ctx: Context):
        self._ctx = ctx
        self._interactive_layer.set_context(ctx)

    def forward(self, x = None):

        if self._bottom_model is None:
            b_out = None
        else:
            b_out = self._bottom_model(x)
            # bottom layer
            if not self._guest_direct_backward:
                self._bottom_fw = b_out

        # hetero layer
        if not self._guest_direct_backward:
            interactive_out = self._interactive_layer.forward(b_out)
            self._interactive_fw_rg = interactive_out.requires_grad_(True)
            # top layer
            top_out = self._top_model(self._interactive_fw_rg)
        else:
            top_out = self._top_model(self._interactive_layer(b_out))

        return top_out

    def backward(self, loss):

        if self._guest_direct_backward:
            # guest side direct backward & send error to hosts
            self._interactive_layer.backward(loss)
            loss.backward()
        else:
            # backward are split into parts
            loss.backward()  # update top
            interactive_error = self._interactive_fw_rg.grad
            self._interactive_fw_rg = None
            bottom_error = self._interactive_layer.backward(interactive_error)  # compute bottom error & update hetero
            if bottom_error is not None:
                bottom_loss = backward_loss(self._bottom_fw, bottom_error)
                bottom_loss.backward()
            self._bottom_fw = False

    def predict(self, x = None):

        with torch.no_grad():
            if self._bottom_model is None:
                b_out = None
            else:
                b_out = self._bottom_model(x)
            interactive_out = self._interactive_layer.predict(b_out)
            top_out = self._top_model(interactive_out)

        return top_out


class HeteroNNModelHost(t.nn.Module):

    def __init__(self, bottom_model: t.nn.Module,
                 interactive_layer: InteractiveLayerHost
                 ):

        super().__init__()
        self._bottom_model = bottom_model
        self._interactive_layer = interactive_layer

        # cached variables
        self._bottom_fw = None  # for backward usage

        # ctx
        self._ctx = None

    def __repr__(self):
        return f"HeteroNNHost(bottom_model={self._bottom_model})"

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)

    def _clear_state(self):
        self._bottom_fw = None

    def set_context(self, ctx: Context):
        self._ctx = ctx
        self._interactive_layer.set_context(ctx)

    def forward(self, x):

        b_out = self._bottom_model(x)
        # bottom layer
        self._bottom_fw = b_out
        # hetero layer
        self._interactive_layer.forward(b_out)

    def backward(self):

        error = self._interactive_layer.backward()
        loss = backward_loss(self._bottom_fw, error)
        loss.backward()
        self._clear_state()

    def predict(self, x):

        with torch.no_grad():
            b_out = self._bottom_model(x)
            self._interactive_layer.predict(b_out)