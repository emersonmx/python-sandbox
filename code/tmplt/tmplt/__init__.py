import os
import click

PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@click.group()
def cli():
    pass


from tmplt import make, config
