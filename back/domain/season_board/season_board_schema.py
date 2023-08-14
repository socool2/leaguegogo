import datetime

from pydantic import BaseModel


class SeasonBoard(BaseModel):
    board_id: int
    season_id: str
    board_title: str
    board_desc: str
    board_date: datetime.datetime
    file_link: str
    write_member_id: str
    write_date: datetime.datetime
    delete_date: datetime.datetime
    comment_yn: str
    remark: str

    class Config:
        from_attributes = True


class SeasonBoardList(BaseModel):
    total: int = 0
    season_board_list: list[SeasonBoard] = []


class SeasonBoardUpdate(BaseModel):
    board_id: int
    season_id: str
    board_title: str
    board_desc: str
    board_date: datetime.datetime
    file_link: str
    write_member_id: str
    delete_date: datetime.datetime
    comment_yn: str
    remark: str


class SeasonBoardDelete(BaseModel):
    board_id: int