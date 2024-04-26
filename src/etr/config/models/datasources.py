from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import model_validator
from pydantic_core import PydanticCustomError

from etr.config.models.base import _Configuration


class DatasourceType(Enum):
    FILE = "file"
    API = "api"


class DataFormat(Enum):
    JSON = "json"
    YAML = "yaml"


class SourceConfig(_Configuration):
    name: str
    type: DatasourceType
    args: FileSourceArgs | APISourceArgs

    @model_validator(mode="after")
    def validate_type(self) -> str:
        arguments_types = {
            DatasourceType.FILE: FileSourceArgs,
            DatasourceType.API: APISourceArgs,
        }

        if not isinstance(self.args, arguments_types[self.type]):
            raise PydanticCustomError(
                "incorrect_datasource_type",
                f"{self.type} does not match the datasource arguments",
                {"type": self.type},
            )
        return self


class SourceArgs(_Configuration):
    pass


class FileSourceArgs(SourceArgs):
    path: str
    format: DataFormat


class APISourceArgs(SourceArgs):
    url: str
    method: Literal["get", "post"]
    headers: dict[str, str]
    body: dict[str, str]
