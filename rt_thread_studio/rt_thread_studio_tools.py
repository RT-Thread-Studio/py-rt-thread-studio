import click
from rt_thread_studio.board_support_package_generator.bsp_generator.generate import Generator

@click.group()
def cli():
    pass

@cli.command()
@click.option(
    '--type',
    "-t",
    envvar="type",
    required=False,
    default="bsp",
    type=click.STRING,
    help="specify the package type",
)
def create(type):
    """: a command to create a package"""
    # TODO :add project update feature
    if str(type).lower().strip()=="bsp":
        gen=Generator()
        gen.generate_bsp()
        pass
    else:
        print("please specify one supported package type")


@cli.command("create_bsp")
@click.option(
    '--json',
    "-j",
    envvar="json",
    required=True,
    default="",
    type=click.STRING,
    help="specify json input",
)
def create_bsp_from_json(json):
    """: a command to create a package"""
    # TODO :add project update feature
    print(json)
    generator1 = Generator()
    generator1.generate_bsp_from_json(json)

if __name__ == '__main__':
    cli()