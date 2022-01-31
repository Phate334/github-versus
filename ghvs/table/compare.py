from typing import List

import humanize
from pydantic import BaseModel
from rich.table import Table, box

from ghvs.models.domain.repositories import Repository


class CompareResultTitle(BaseModel):
    repository: str = "Repository"
    description: str = ":book: Description"
    language: str = ":speaker: Language"
    updated_at: str = ":hammer: Updated"
    created_at: str = ":egg: Created"
    license_name: str = ":paperclip: License"
    topics: List[str] = ":magnet: Topics"
    stargazers_count: int = ":star: Stars"
    forks_count: int = ":fork_and_knife: Forks"
    open_issues_count: int = ":wrench: Open Issues"
    network_count: int = ":spider_web: Networks"
    watchers_count: int = ":eyes: Watchers"
    owner_type: str = ":smiley: Owner Type"
    size: str = ":balance_scale: Size"
    homepage: str = "Homepage Link"


def create_compare_table(repostories: List[Repository]):
    title = CompareResultTitle()
    table = Table(
        title="compare two repostories",
        title_justify="center",
        box=box.MINIMAL_HEAVY_HEAD,
    )
    table.add_column(title.repository)
    for repo in repostories:
        table.add_column(f"{repo.full_name} {'(archived:x:)' if repo.archived else ''}")
    table.add_row(title.description, *(r.description for r in repostories))
    table.add_row(title.language, *(r.language for r in repostories))
    table.add_row(
        title.updated_at, *(humanize.naturaldate(r.updated_at) for r in repostories)
    )
    table.add_row(
        title.created_at, *(humanize.naturaldate(r.created_at) for r in repostories)
    )
    table.add_row(title.license_name, *(r.license_name for r in repostories))
    table.add_row(title.topics, *(",".join(r.topics) for r in repostories))
    table.add_row(
        title.stargazers_count,
        *(humanize.intcomma(r.stargazers_count) for r in repostories),
    )
    table.add_row(
        title.forks_count, *(humanize.intcomma(r.forks_count) for r in repostories)
    )
    table.add_row(
        title.open_issues_count,
        *(humanize.intcomma(r.open_issues_count) for r in repostories),
    )
    table.add_row(
        title.network_count, *(humanize.intcomma(r.network_count) for r in repostories)
    )
    table.add_row(
        title.watchers_count,
        *(humanize.intcomma(r.watchers_count) for r in repostories),
    )
    table.add_row(title.owner_type, *(r.owner_type for r in repostories))
    table.add_row(title.size, *(r.size for r in repostories))
    return table
