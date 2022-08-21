import click
from dingobot.namegen import NameGenerator


@click.group()
def cli():
    pass


@cli.command()
@click.option("-n", default=1, help="Number of unique names to generate")
def names(n):
    for _ in range(n):
        namegen = NameGenerator()
        print(namegen.get_fullname())
