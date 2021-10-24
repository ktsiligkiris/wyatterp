"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Wyatterp."""


if __name__ == "__main__":
    main(prog_name="wyatterp")  # pragma: no cover
