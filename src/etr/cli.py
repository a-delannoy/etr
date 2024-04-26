from __future__ import annotations

import os

import click

from etr.config import parse_configuration_file
from etr.config.settings import CONFIG_PATH_VAR
from etr.config.settings import DEFAULT_CONFIG_PATH


@click.command()
@click.option(
    "--config",
    default=os.environ.get(CONFIG_PATH_VAR, DEFAULT_CONFIG_PATH),
    help="The path towards the configuration file.",
)
def generate(config):
    """Generate an inventory using the given configuration file."""
    # logger.info(f"Generating inventory using configuration file: {config}")
    configuration = parse_configuration_file(config)
    print(configuration)
