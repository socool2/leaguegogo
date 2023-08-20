import datetime

from pydantic import BaseModel


class TeamBoardComment(BaseModel):
    comment_id: int
    board_id: int
    comment_Desc: str
    write_member_id: int
    write_date: datetime.datetime
    delete_date: datetime.datetime
    remark: str

    class Config:
        from_attributes = True


class TeamBoardCommentList(BaseModel):
    total: int = 0
    team_board_comment_list: list[TeamBoardComment] = []


class TeamBoardCommentUpdate(BaseModel):
    comment_id: int
    comment_Desc: str
    delete_date: datetime.datetime
    remark: str


class TeamBoardCommentDelete(BaseModel):
    comment_id: int
