from domain.season_board.season_board_schema import SeasonBoard, SeasonBoardUpdate
from models import SeasonBoard
from sqlalchemy.orm import Session


def get_season_board_list(db: Session, skip: int = 0, limit: int = 10):
    _season_board_list = db.query(SeasonBoard) \
        .order_by(SeasonBoard.write_date.desc())
    total = _season_board_list.count()
    season_board_list = _season_board_list.offset(skip).limit(limit).all()
    return total, season_board_list


def get_season_board_info(db: Session, board_id: int):
    season_board = db.query(SeasonBoard).get(board_id)
    return season_board


def create_season_board_info(db: Session, season_board_info: SeasonBoard):
    db_season_board = SeasonBoard(
        board_id=season_board_info.board_id,
        season_id=season_board_info.season_id,
        board_title=season_board_info.board_title,
        board_desc=season_board_info.board_desc,
        board_date=season_board_info.board_date,
        file_link=season_board_info.file_link,
        write_member_id=season_board_info.write_member_id,
        write_date=season_board_info.write_date,
        delete_date=season_board_info.delete_date,
        comment_yn=season_board_info.comment_yn,
        remark=season_board_info.remark
    )
    db.add(db_season_board)
    db.commit()


def update_season_board_info(db: Session, season_board_info: SeasonBoard, season_board_update: SeasonBoardUpdate):
    season_board_info.board_id = season_board_update.board_id,
    season_board_info.season_id = season_board_update.season_id,
    season_board_info.board_title = season_board_update.board_title,
    season_board_info.board_desc = season_board_update.board_desc,
    season_board_info.board_date = season_board_update.board_date,
    season_board_info.file_link = season_board_update.file_link,
    season_board_info.write_member_id = season_board_update.write_member_id
    season_board_info.delete_date = season_board_update.delete_date
    season_board_info.comment_yn = season_board_update.comment_yn
    season_board_info.remark = season_board_update.remark
    db.add(season_board_info)
    db.commit()


def delete_season_board(db: Session, db_season_board: SeasonBoard):
    db.delete(db_season_board)
    db.commit()
