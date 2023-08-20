import datetime

from pydantic import BaseModel


class Season(BaseModel):
    season_id: int
    league_id: int
    season_name: str
    season_start_date: datetime.datetime
    season_end_date: datetime.datetime
    season_desc: str
    season_image_link: str
    season_reg_start_date: datetime.datetime
    season_reg_end_date: datetime.datetime
    preli_yn: str
    preli_game_cnt: int
    preli_start_date: datetime.datetime
    preli_end_date: datetime.datetime
    preli_status: str
    main_yn: str
    main_game_cnt: int
    main_start_date: datetime.datetime
    main_end_date: datetime.datetime
    main_status: str
    playoff_yn: str
    playoff_game_cnt: int
    playoff_start_date: datetime.datetime
    playoff_end_date: datetime.datetime
    playoff_status: str
    remark: str

    class Config:
        from_attributes = True


class SeasonList(BaseModel):
    total: int = 0
    season_list: list[Season] = []


class SeasonUpdate(BaseModel):
    season_id: int
    league_id: int
    season_name: str
    season_start_date: datetime.datetime
    season_end_date: datetime.datetime
    season_desc: str
    season_image_link: str
    season_reg_start_date: datetime.datetime
    season_reg_end_date: datetime.datetime
    preli_yn: str
    preli_game_cnt: int
    preli_start_date: datetime.datetime
    preli_end_date: datetime.datetime
    preli_status: str
    main_yn: str
    main_game_cnt: int
    main_start_date: datetime.datetime
    main_end_date: datetime.datetime
    main_status: str
    playoff_yn: str
    playoff_game_cnt: int
    playoff_start_date: datetime.datetime
    playoff_end_date: datetime.datetime
    playoff_status: str
    remark: str


class SeasonDelete(BaseModel):
    season_id: int