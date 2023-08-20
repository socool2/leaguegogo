import datetime

from pydantic import BaseModel


class SeasonBoardComment(BaseModel):
    comment_id: int
    board_id: int
    comment_desc: str
    write_member_id: str
    write_date: datetime.datetime
    delete_date: datetime.datetime
    remark: str

    class Config:
        from_attributes = True


class SeasonBoardCommentList(BaseModel):
    total: int = 0
    season_board_comment_list: list[SeasonBoardComment] = []


class SeasonBoardCommentUpdate(BaseModel):
    comment_id: int
    comment_desc: str
    delete_date: datetime.datetime
    remark: str


class SeasonBoardCommentDelete(BaseModel):
    comment_id: int