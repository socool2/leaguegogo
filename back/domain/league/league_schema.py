import datetime

from pydantic import BaseModel


class League(BaseModel):
    league_id: int
    league_name: str
    league_creator: str
    league_create_date: datetime.datetime
    introduce_league: str | None
    league_image_link: str | None
    league_start_date: datetime.datetime
    league_end_date: datetime.datetime
    league_status: str
    remark: str | None

    class Config:
        from_attributes = True


class LeagueList(BaseModel):
    total: int = 0
    league_list: list[League] = []


class LeagueUpdate(BaseModel):
    league_id: int
    league_name: str
    introduce_league: str | None
    league_image_link: str | None
    league_start_date: datetime.datetime
    league_end_date: datetime.datetime
    league_status: str
    remark: str | None


class LeagueDelete(BaseModel):
    league_id: int


class LeagueCreate(BaseModel):
    league_name: str
    league_creator: str
    league_create_date: datetime.datetime
    introduce_league: str | None
    league_image_link: str | None
    league_start_date: datetime.datetime
    league_end_date: datetime.datetime
    league_status: str
    remark: str | None
