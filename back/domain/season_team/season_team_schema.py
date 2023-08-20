import datetime

from pydantic import BaseModel


class SeasonTeam(BaseModel):
    season_team_id: int
    season_id: int
    team_id: int
    reg_user_id: int
    reg_date: datetime.datetime
    reg_cancel_date: datetime.datetime
    main_advance_yn: str
    playoff_advance_yn: str
    remark: str

    class Config:
        from_attributes = True


class SeasonTeamList(BaseModel):
    total: int = 0
    season_team_list: list[SeasonTeam] = []


class SeasonTeamUpdate(BaseModel):
    season_team_id: int
    season_id: int
    team_id: int
    reg_cancel_date: datetime.datetime
    main_advance_yn: str
    playoff_advance_yn: str
    remark: str


class SeasonTeamDelete(BaseModel):
    season_team_id: int