import click


@click.group()
def cli():
    pass


@cli.command()
def run():
    print('run')
