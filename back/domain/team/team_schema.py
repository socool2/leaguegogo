import datetime

from pydantic import BaseModel


class Team(BaseModel):
    team_id: str
    team_name: str
    team_creator: str
    introduce_team: str | None
    team_image_link: str | None
    team_create_date: datetime.datetime
    team_close_date: datetime.datetime | None
    remark: str | None

    class Config:
        from_attributes = True


class TeamList(BaseModel):
    total: int = 0
    team_list: list[Team] = []


class TeamUpdate(BaseModel):
    team_id: str
    team_name: str
    introduce_team: str | None
    team_image_link: str | None
    team_close_date: datetime.datetime | None
    remark: str | None


class TeamDelete(BaseModel):
    team_id: str