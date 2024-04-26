from __future__ import annotations

from etr.config.models.base import _Configuration
from etr.config.models.datasources import SourceConfig


class ETRConfig(_Configuration):
    data: list[SourceConfig]
