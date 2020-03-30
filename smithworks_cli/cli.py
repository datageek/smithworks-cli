import typer

app = typer.Typer()


@app.command()
def begin():
    pretty = typer.style("smithworks CLI", fg="red")
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
    print(provider[0])




if __name__ == "__main__":
    app()
