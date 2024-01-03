from click.testing import CliRunner

from odyssey_example_cli.cli import cli

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert result.output == 'Hello world!\n'