import click

from tmplt import cli


@cli.command()
def make():
    click.echo('hello')
