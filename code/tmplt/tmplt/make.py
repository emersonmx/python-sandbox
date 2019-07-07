import os
import json
import click

from tmplt import cli
from tmplt.config import get_merged_configs, get_config, CONFIG_FILENAME

TEMPLATE_PATH = get_config('template_path')


def get_template_configs():
    if not TEMPLATE_PATH:
        return []
    if not os.path.isdir(TEMPLATE_PATH):
        return []

    for template in os.listdir(TEMPLATE_PATH):
        template_path = os.path.join(TEMPLATE_PATH, template)
        if not os.path.isdir(template_path):
            continue
        template_config = os.path.join(template_path, CONFIG_FILENAME)
        if not os.path.isfile(template_config):
            continue
        with open(template_config, 'r') as c:
            try:
                yield json.load(c)
            except json.decoder.JSONDecodeError:
                continue


@cli.command()
def make():
    for config in get_template_configs():
        click.echo(config)
