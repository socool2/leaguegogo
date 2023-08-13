from domain.team_board.team_board_schema import TeamBoard, TeamBoardUpdate
from models import TeamBoard
from sqlalchemy.orm import Session


def get_team_board_list(db: Session, skip: int = 0, limit: int = 10):
    _team_board_list = db.query(TeamBoard) \
        .order_by(TeamBoard.write_date.desc())
    total = _team_board_list.count()
    team_board_list = _team_board_list.offset(skip).limit(limit).all()
    return total, team_board_list


def get_team_board_info(db: Session, board_id: int):
    team_board = db.query(TeamBoard).get(board_id)
    return team_board


def create_team_board_info(db: Session, team_board_info: TeamBoard):
    db_team_board = TeamBoard(
        board_id=team_board_info.board_id,
        team_id=team_board_info.team_id,
        board_type=team_board_info.board_type,
        board_title=team_board_info.board_title,
        board_desc=team_board_info.board_desc,
        board_date=team_board_info.board_date,
        file_link=team_board_info.file_link,
        write_member_id=team_board_info.write_member_id,
        write_date=team_board_info.write_date,
        delete_date=team_board_info.delete_date,
        comment_yn=team_board_info.comment_yn,
        remark=team_board_info.remark
    )
    db.add(db_team_board)
    db.commit()


def update_team_board_info(db: Session, team_board_info: TeamBoard, team_board_update: TeamBoardUpdate):
    team_board_info.board_id = team_board_update.board_id,
    team_board_info.team_id = team_board_update.team_id,
    team_board_info.board_type = team_board_update.board_type,
    team_board_info.board_title = team_board_update.board_title,
    team_board_info.board_desc = team_board_update.board_desc,
    team_board_info.board_date = team_board_update.board_date,
    team_board_info.file_link = team_board_update.file_link
    team_board_info.delete_date = team_board_update.delete_date
    team_board_info.comment_yn = team_board_update.comment_yn
    team_board_info.remark = team_board_update.remark
    db.add(team_board_info)
    db.commit()


def delete_team_board(db: Session, db_team_board: TeamBoard):
    db.delete(db_team_board)
    db.commit()
