import click


@click.group()
def cli():
    pass


from tmplt import make, config
