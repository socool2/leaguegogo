import datetime

from pydantic import BaseModel



g
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
    # round_status: scheduled, finished
    round_status: str
    round_video_link: str
    remark: str

    class Config:
        from_attributes = True

    @classmethod
    def new_game(cls, season_id: str, team1_id: str, team2_id: str, game_type: str, round: int):
        return cls(
            game_id=None,
            season_id=season_id,
            game_type=game_type,
            game_round=round,
            team1_id=team1_id,
            team2_id=team2_id,
            game_date=None,
            team1_point=None,
            team1_result=None,
            team2_point=None,
            team2_result=None,
            round_status="scheduled",
            round_video_link=None,
            remark=None
        )





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