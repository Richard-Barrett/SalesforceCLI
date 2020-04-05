import click 

@click.group()
def API():
    """A CLI wrapper for Salesforce Users and Companies Using Salesforce."""

@click.option('--report', default=1, help='Generate a report based on a Salesforce Object')
@click.option('--severity', default=1, help='Severity Level Defined by Organization')

@API.command()
def entries():
        """List all cataloged APIs."""


if __name__ == '__main__':
        API(prog_name='SalesForce-CLI')

