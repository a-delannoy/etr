from __future__ import annotations

import os

import click

from etr.settings import CONFIG_PATH_VAR
from etr.settings import DEFAULT_CONFIG_PATH


@click.command()
@click.option(
    "--config",
    default=os.environ.get(CONFIG_PATH_VAR, DEFAULT_CONFIG_PATH),
    help="The path towards the configuration file.",
)
def generate(config):
    """Generate an inventory using the given configuration file."""
    raise NotImplementedError("This feature is not yet implemented.")
