#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import logging
from typing import List

from fate.arch.abc import PartyMeta

from ..._standalone import Federation as RawFederation
from ..._standalone import Table as RawTable
from ...computing.standalone import Table
from ..federation import Federation

LOGGER = logging.getLogger(__name__)


class StandaloneFederation(Federation):
    def __init__(
        self,
        standalone_session,
        federation_session_id: str,
        party: PartyMeta,
        parties: List[PartyMeta],
    ):
        super().__init__()
        LOGGER.debug(
            f"[federation.standalone]init federation: "
            f"standalone_session={standalone_session}, "
            f"federation_session_id={federation_session_id}, "
            f"party={party}"
        )
        self._session_id = federation_session_id
        self._federation = RawFederation(standalone_session._session, federation_session_id, party)
        LOGGER.debug("[federation.standalone]init federation context done")

        self.local_party = party
        self.parties = parties

    @property
    def session_id(self) -> str:
        return self._session_id

    def _push_table(
        self,
        table: Table,
        name: str,
        tag: str,
        parties: List[PartyMeta],
    ):
        return self._federation.push_table(table=table.table, name=name, tag=tag, parties=parties)

    def _push_bytes(
        self,
        v: bytes,
        name: str,
        tag: str,
        parties: List[PartyMeta],
    ):
        return self._federation.push_bytes(v=v, name=name, tag=tag, parties=parties)

    def _pull_table(
        self,
        name: str,
        tag: str,
        parties: List[PartyMeta],
    ) -> List[Table]:
        rtn = self._federation.pull_table(name=name, tag=tag, parties=parties)

        return [Table(r) if isinstance(r, RawTable) else r for r in rtn]

    def _pull_bytes(
        self,
        name: str,
        tag: str,
        parties: List[PartyMeta],
    ) -> List[bytes]:
        rtn = self._federation.pull_bytes(name=name, tag=tag, parties=parties)

        return [Table(r) if isinstance(r, RawTable) else r for r in rtn]

    def destroy(self):
        self._federation.destroy()
