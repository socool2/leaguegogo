from domain.game.game_schema import Game, GameUpdate
from models import GameInfo
from sqlalchemy.orm import Session


def get_game_list(db: Session, skip: int = 0, limit: int = 10):
    _game_list = db.query(GameInfo) \
        .order_by(GameInfo.game_date.desc())
    total = _game_list.count()
    game_list = _game_list.offset(skip).limit(limit).all()
    return total, game_list


def get_game_info(db: Session, game_id: int):
    game = db.query(GameInfo).get(game_id)
    return game


def create_game_info(db: Session, game_info: Game):
    db_game = define_game_info(db, game_info)
    db.add(db_game)
    db.commit()


def define_game_info(db: Session, game_info: Game):
    return GameInfo(
        game_id=game_info.game_id,
        season_id=game_info.season_id,
        game_type=game_info.game_type,
        game_round=game_info.game_round,
        team1_id=game_info.team1_id,
        team2_id=game_info.team2_id,
        game_date=game_info.game_date,
        team1_point=game_info.team1_point,
        team1_result=game_info.team1_result,
        team2_point=game_info.team2_point,
        team2_result=game_info.team2_result,
        round_status=game_info.round_status,
        round_video_link=game_info.round_video_link,
        remark=game_info.remark
    )

    
def update_game_info(db: Session, game_info: Game, game_update: GameUpdate):
    game_info.game_id = game_update.game_id,
    game_info.season_id = game_update.season_id,
    game_info.game_type = game_update.game_type
    game_info.game_round = game_update.game_round
    game_info.team1_id = game_update.team1_id
    game_info.team2_id = game_update.team2_id
    game_info.game_date = game_update.game_date
    game_info.team1_point = game_update.team1_point
    game_info.team1_result = game_update.team1_result
    game_info.team2_point = game_update.team2_point
    game_info.team2_result = game_update.team2_result
    game_info.round_status = game_update.round_status
    game_info.round_video_link = game_update.round_video_link
    game_info.remark = game_update.remark
    db.add(game_info)
    db.commit()


def delete_game(db: Session, db_game: Game):
    db.delete(db_game)
    db.commit()
