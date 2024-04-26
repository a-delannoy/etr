from __future__ import annotations

import yaml

from etr.config.models.root import ETRConfig


def parse_configuration_file(path: str) -> ETRConfig:
    with open(path) as file:
        data = yaml.safe_load(file)
    return ETRConfig.model_validate(data)
