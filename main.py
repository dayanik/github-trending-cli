import argparse
import requests

from datetime import date, timedelta
from pydantic import BaseModel
from rich.console import Console
from rich.table import Table
from rich.text import Text


console = Console()


class Repo(BaseModel):
    name: str
    description: str | None
    stargazers_count: int
    language: str | None
    html_url: str


class Response(BaseModel):
    items: list[Repo]


def get_repos(language: str, created: date, limit: int) -> list[Repo]:
    url = "https://api.github.com/search/repositories"
    headers = {"accept": "application/vnd.github+json"}
    params = {
        "q": f"language:{language.lower()} created:>={created.isoformat()} is:public",
        "sort": "stars",
        "order": "desc",
        "per_page": min(limit, 30)
    }

    response = requests.get(url=url, params=params, headers=headers)
    response.raise_for_status()
    print(response.json())
    return Response.model_validate(response.json()).items
    


def positive_int(value: str) -> int:
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "значение должно быть целым числом > 0"
        )
    return ivalue


def get_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        default='',
        help="programming language of repositories"
    )
    parser.add_argument(
        "-d",
        "--duration",
        type=str,
        default="week",
        choices=["day", "week", "month", "year"],
        help="a time range to filter the repositories"
    )
    parser.add_argument(
        "--limit",
        type=positive_int,
        help='count of repos to print',
        default=10
    )
    return parser.parse_args()


def handle_args(args) -> list[Repo]:
    language = args.language
    limit = args.limit

    match args.duration:
        case "day":
            days = 1
        case "week":
            days = 7
        case "month":
            days = 30
        case "year":
            days = 365
    
    created = date.today() - timedelta(days=days)
    return get_repos(language, created, limit)


def render_repos(repos: list[Repo]) -> None:
    if not repos:
        console.print("[bold red]Репозитории не найдены[/]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Stars", justify="right", style="yellow")
    table.add_column("Language", justify="right", style="green")
    table.add_column("Repo", style="bold")
    table.add_column("Description", overflow="fold")
    table.add_column("URL", style="blue")

    for repo in repos:
        table.add_row(
            str(repo.stargazers_count),
            repo.language or "-",
            repo.name,
            repo.description or "—",
            repo.html_url,
        )

    console.print(table)

def main():
    parser = argparse.ArgumentParser(prog="trend-repos")
    args = get_args(parser)
    repos = handle_args(args)
    render_repos(repos)


if __name__ == "__main__":
    main()
