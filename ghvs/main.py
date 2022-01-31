from typing import List

import typer
from requests_html import HTMLSession
from rich.console import Console

from ghvs.models.domain.repositories import Repository
from ghvs.table.compare import create_compare_table

app = typer.Typer()


@app.command()
def compare(repos: List[str]):
    session = HTMLSession()
    repositories = []
    for repo in repos:
        res = session.get(f"https://api.github.com/repos/{repo}")
        res.raise_for_status()
        repositories.append(Repository(**res.json()))

    Console().print(create_compare_table(repositories))


@app.command()
def forks():
    ...


@app.command()
def networks():
    ...


if __name__ == "__main__":
    app()
