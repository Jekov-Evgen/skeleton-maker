CONST_CLICK = """
import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Привет, мир!")

@cli.command()
@click.argument('name')
@click.option('--greeting', default='Привет', help='Фраза приветствия.')
def greet(name, greeting):
    click.echo(f"{greeting}, {name}!")

if __name__ == "__main__":
    cli()
"""