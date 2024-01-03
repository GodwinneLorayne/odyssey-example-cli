import click

from odyssey_example_cli.__about__ import __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='new cli')
@click.pass_context
def cli(ctx: click.Context):
    click.echo('Hello world!')
