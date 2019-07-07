import os
import click


@click.group()
def cli():
    pass


def get_default_confgs():
    return {
        'template_path': os.path.join(click.get_app_dir('tmplt'), 'templates')
    }

from tmplt import make
