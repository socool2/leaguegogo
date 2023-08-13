from domain.game_member.game_member_schema import GameMember, GameMemberUpdate
from models import GameMemberInfo
from sqlalchemy.orm import Session


def get_game_member_list(db: Session, skip: int = 0, limit: int = 10):
    _game_member_list = db.query(GameMemberInfo) \
        .order_by(GameMemberInfo.game_position.desc())
    total = _game_member_list.count()
    game_member_list = _game_member_list.offset(skip).limit(limit).all()
    return total, game_member_list


def get_game_member_info(db: Session, game_member_id: int):
    game_member = db.query(GameMemberInfo).get(game_member_id)
    return game_member


def create_game_member_info(db: Session, game_member_info: GameMember):
    db_game_member = GameMemberInfo(
        game_id=game_member_info.game_id,
        team_id=game_member_info.team_id,
        member_id=game_member_info.member_id,
        game_position=game_member_info.game_position,
        remark=game_member_info.remark
    )
    db.add(db_game_member)
    db.commit()


def update_game_member_info(db: Session, game_member_info: GameMember, game_member_update: GameMemberUpdate):
    game_member_info.member_id = game_member_update.member_id,
    game_member_info.game_position = game_member_update.game_position,
    game_member_info.remark = game_member_update.remark
    db.add(game_member_info)
    db.commit()


def delete_game_member(db: Session, db_game_member: GameMember):
    db.delete(db_game_member)
    db.commit()
