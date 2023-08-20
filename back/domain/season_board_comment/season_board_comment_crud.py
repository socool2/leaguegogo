import datetime

from domain.season_board_comment.season_board_comment_schema import SeasonBoardComment, SeasonBoardCommentUpdate
from models import SeasonBoardComment
from sqlalchemy.orm import Session


def get_season_board_comment_list(db: Session, skip: int = 0, limit: int = 10):
    _season_board_comment_list = db.query(SeasonBoardComment) \
        .order_by(SeasonBoardComment.write_date.desc())
    total = _season_board_comment_list.count()
    season_board_comment_list = _season_board_comment_list.offset(skip).limit(limit).all()
    return total, season_board_comment_list


def get_season_board_comment_info(db: Session, season_board_comment_id: int):
    season_board_comment = db.query(SeasonBoardComment).get(season_board_comment_id)
    return season_board_comment


def create_season_board_comment_info(db: Session, season_board_comment_info: SeasonBoardComment):
    db_season_board_comment = SeasonBoardComment(
        comment_id=season_board_comment_info.comment_id,
        board_id=season_board_comment_info.board_id,
        comment_desc=season_board_comment_info.comment_desc,
        write_member_id=season_board_comment_info.write_member_id,
        write_date=season_board_comment_info.write_date,
        delete_date=season_board_comment_info.delete_date,
        remark=season_board_comment_info.remark
    )
    db.add(db_season_board_comment)
    db.commit()
    
    
def update_season_board_comment_info(db: Session, season_board_comment_info: SeasonBoardComment, season_board_comment_update: SeasonBoardCommentUpdate):
    season_board_comment_info.comment_id = season_board_comment_update.comment_id,
    season_board_comment_info.comment_desc = season_board_comment_update.comment_desc,
    season_board_comment_info.delete_date = season_board_comment_update.delete_date
    season_board_comment_info.remark = season_board_comment_update.remark
    db.add(season_board_comment_info)
    db.commit()


def delete_season_board_comment(db: Session, db_season_board_comment: SeasonBoardComment):
    db.delete(db_season_board_comment)
    db.commit()
