import datetime

from pydantic import BaseModel


class Game(BaseModel):
    game_id: str
    season_id: int
    game_type: str
    game_round: int
    team1_id: str
    team2_id: str
    game_date: datetime.datetime
    team1_point: int
    team1_result: str
    team2_point: int
    team2_result: str
    round_status: str
    round_video_link: str
    remark: str

    class Config:
        from_attributes = True


class GameList(BaseModel):
    total: int = 0
    game_member_list: list[Game] = []


class GameUpdate(BaseModel):
    game_id: str
    season_id: int
    game_type: str
    game_round: int
    team1_id: str
    team2_id: str
    game_date: datetime.datetime
    team1_point: int
    team1_result: str
    team2_point: int
    team2_result: str
    round_status: str
    round_video_link: str
    remark: str


class GameDelete(BaseModel):
    game_id: str