import typer

app = typer.Typer()


@app.command()
def begin():
    pretty = typer.style("smithworks CLI TEST", fg="red")
    typer.echo(
        "\nThank you for choosing the "
        + pretty
        + " to deploy your FoundryVTT instance, please make sure you've read the documentation"
    )
    menu()


@app.command("menu")
def menu():
    typer.secho("\nMenu Options:", fg=typer.colors.BRIGHT_BLUE, underline=True)
    typer.secho("  (D)igital Ocean")
    typer.secho("  (A)mazon Web Services")
    typer.secho("  (G)oogle Cloud Platform")
    provider = typer.prompt("Select your hosting provider (d/a/g)")
    print(read_provider(provider[0]))
    
def read_provider(hosting_provider):
    #TODO My idea would be to have the method calls as the values of
    # this dictionary.  I am thinking the methods would be in a 
    # separate file.
    switch = {
        "d":"d",
        "a":"a",
        "g":"g"
    }
    return switch.get(hosting_provider)



if __name__ == "__main__":
    app()
