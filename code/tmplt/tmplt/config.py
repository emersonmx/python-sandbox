import os
import json
import click
from deepmerge import always_merger
from tmplt import cli

CONFIG_PATH = click.get_app_dir('tmplt')
CONFIG_FILE = os.path.join(CONFIG_PATH, 'tmplt.json')


def get_default_configs():
    return {
        'template_path': os.path.join(CONFIG_PATH, 'templates')
    }


def get_configs():
    config_file = os.path.join(CONFIG_PATH, 'tmplt.json')
    if os.path.isfile(config_file):
        return json.load(config_file)
    return {}


def get_merged_configs():
    return always_merger.merge(
        get_default_configs(),
        get_configs()
    )


def dumps_json(obj):
    return json.dumps(obj, indent=4)


@cli.group()
def config():
    pass


@config.command()
@click.option('-f', '--force', is_flag=True, default=False)
def init(force):
    if os.path.isfile(CONFIG_FILE) and not force:
        click.echo('{} already initialized'.format(CONFIG_FILE))
        return
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
    with open(CONFIG_FILE, 'w') as c:
        c.write(dumps_json(get_default_configs()))
    click.echo('{} initialized!'.format(CONFIG_FILE))


@config.command()
def dump():
    if not os.path.isfile(CONFIG_FILE):
        click.echo(dumps_json(get_default_configs()))
        return
    with open(CONFIG_FILE, 'r') as c:
        click.echo(dumps_json(json.load(c)))
