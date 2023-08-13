import datetime

from pydantic import BaseModel


class TeamBoard(BaseModel):
    board_id: int
    team_id: str
    board_type: str
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


class TeamBoardList(BaseModel):
    total: int = 0
    team_board_list: list[TeamBoard] = []


class TeamBoardUpdate(BaseModel):
    board_id: int
    team_id: str
    board_type: str
    board_title: str
    board_desc: str
    board_date: datetime.datetime
    file_link: str
    delete_date: datetime.datetime
    comment_yn: str
    remark: str


class TeamBoardDelete(BaseModel):
    board_id: int

