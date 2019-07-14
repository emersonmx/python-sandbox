import os
import click


@click.group()
def cli():
    _setup_config_file()
    _setup_templates_directory()


def _setup_config_file():
    if os.path.isfile(CONFIG_FILEPATH):
        return

    os.makedirs(CONFIG_PATH, exist_ok=True)
    with open(CONFIG_FILEPATH, 'w+') as cf:
        configs = config.get_merged_configs()
        cf.write(dumps_json(configs))
        click.echo('Config file created in {}'.format(CONFIG_FILEPATH))


def _setup_templates_directory():
    template_path = get_config('template_path')
    if not os.path.isdir(template_path):
        os.makedirs(template_path, exist_ok=True)


from tmplt import make, config
from tmplt.config import CONFIG_PATH, CONFIG_FILEPATH, get_config, dumps_json
