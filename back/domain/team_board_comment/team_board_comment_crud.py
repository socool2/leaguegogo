from domain.team_board_comment.team_board_comment_schema import TeamBoardComment,TeamBoardCommentUpdate
from models import TeamBoardComment
from sqlalchemy.orm import Session


def get_team_board_comment_list(db: Session, skip: int = 0, limit: int = 10):
    _team_board_comment_list = db.query(TeamBoardComment) \
        .order_by(TeamBoardComment.write_date.desc())
    total = _team_board_comment_list.count()
    team_board_comment_list = _team_board_comment_list.offset(skip).limit(limit).all()
    return total, team_board_comment_list


def get_team_board_comment_info(db: Session, team_board_comment_id: int):
    team_board_comment = db.query(TeamBoardComment).get(team_board_comment_id)
    return team_board_comment


def create_team_board_comment_info(db: Session, team_board_comment_info: TeamBoardComment):
    db_team_board_comment = TeamBoardComment(
        comment_id=team_board_comment_info.comment_id,
        board_id=team_board_comment_info.board_id,
        comment_Desc=team_board_comment_info.comment_Desc,
        write_member_id=team_board_comment_info.write_member_id,
        write_date=team_board_comment_info.write_date,
        delete_date=team_board_comment_info.delete_date,
        remark=team_board_comment_info.remark
    )
    db.add(db_team_board_comment)
    db.commit()


def update_team_board_comment_info(db: Session, team_board_comment_info: TeamBoardComment, team_board_comment_update: TeamBoardCommentUpdate):
    team_board_comment_info.comment_id = team_board_comment_update.comment_id,
    team_board_comment_info.comment_Desc = team_board_comment_update.comment_Desc,
    team_board_comment_info.delete_date = team_board_comment_update.delete_date
    team_board_comment_info.remark = team_board_comment_update.remark
    db.add(team_board_comment_info)
    db.commit()


def delete_team_board_comment(db: Session, db_team_board_comment: TeamBoardComment):
    db.delete(db_team_board_comment)
    db.commit()
