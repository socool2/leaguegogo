import datetime

from pydantic import BaseModel


class SeasonTeamHistory(BaseModel):
    history_id: int
    season_id: int
    team_id: int
    history_type: str
    history_date: datetime.datetime
    enter_date: datetime.datetime
    enter_manager_id: int
    remark: str

    class Config:
        from_attributes = True


class SeasonTeamHistoryList(BaseModel):
    total: int = 0
    season_team_history_list: list[SeasonTeamHistory] = []


class SeasonTeamHistoryUpdate(BaseModel):
    history_id: int
    season_id: int
    team_id: int
    history_type: str
    history_date: datetime.datetime
    enter_date: datetime.datetime
    enter_manager_id: int
    remark: str


class SeasonTeamHistoryDelete(BaseModel):
    history_id: int

