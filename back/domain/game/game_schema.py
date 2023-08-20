import datetime

from pydantic import BaseModel


class Game(BaseModel):
    game_id: int
    season_id: int
    game_type: str
    game_round: int
    team1_id: int
    team2_id: int
    game_date: datetime.datetime
    team1_point: int
    team1_result: str
    team2_point: int
    team2_result: str

    # round_status: scheduled, finished
    round_status: str
    round_video_link: str
    remark: str

    class Config:
        from_attributes = True

    @classmethod
    def new_game(cls, season_id: int, team1_id: int, team2_id: int, game_type: str, game_round: int, game_date: datetime.datetime):
        return cls(
            game_id=None,
            season_id=season_id,
            game_type=game_type,
            game_round=game_round,
            team1_id=team1_id,
            team2_id=team2_id,
            game_date=game_date,
            team1_point=0,
            team1_result="scheduled",
            team2_point=0,
            team2_result="scheduled",
            round_status="scheduled",
            round_video_link=None,
            remark=None
        )


class GameList(BaseModel):
    total: int = 0
    game_member_list: list[Game] = []


class GameUpdate(BaseModel):
    game_id: int
    season_id: int
    game_type: str
    game_round: int
    team1_id: int
    team2_id: int
    game_date: datetime.datetime
    team1_point: int
    team1_result: str
    team2_point: int
    team2_result: str
    round_status: str
    round_video_link: str
    remark: str


class GameDelete(BaseModel):
    game_id: int
