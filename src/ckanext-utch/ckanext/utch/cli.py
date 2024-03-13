import click


@click.group(short_help="utch CLI.")
def utch():
    """utch CLI.
    """
    pass


@utch.command()
@click.argument("name", default="utch")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [utch]
