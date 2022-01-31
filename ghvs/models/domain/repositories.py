import datetime
from typing import List

import humanize  # type: ignore
from pydantic import BaseConfig, BaseModel, root_validator, validator


def convert_datetime_to_realworld(dt: datetime.datetime) -> str:
    return humanize.naturaldate(dt.replace(tzinfo=datetime.timezone.utc))


def convert_field_to_camel_case(string: str) -> str:
    return "".join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(string.split("_"))
    )


class Repository(BaseModel):
    full_name: str
    description: str = None
    language: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
    license_name: str = None
    topics: List[str] = []
    stargazers_count: int
    forks_count: int
    open_issues_count: int
    network_count: int
    watchers_count: int
    owner_type: str
    size: str
    homepage: str = None
    archived: bool

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(
        cls,  # noqa: N805
        value: datetime.datetime,  # noqa: WPS110
    ) -> datetime.datetime:
        return value

    @validator("size", pre=True)
    def covert_size(cls, size: int):
        return humanize.naturalsize(size)

    @root_validator(pre=True)
    def root_fields(cls, values):
        values["license_name"] = values["license"]["name"] if values["license"] else ""
        values["owner_type"] = values["owner"]["type"]
        return values

    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {datetime.datetime: convert_datetime_to_realworld}
        alias_generator = convert_field_to_camel_case
