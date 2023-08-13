from domain.league.league_schema import League, LeagueUpdate
from models import LeagueInfo
from sqlalchemy.orm import Session



def get_league_list(db: Session, skip: int = 0, limit: int = 10):
    _league_list = db.query(LeagueInfo) \
        .order_by(LeagueInfo.league_create_date.desc())
    total = _league_list.count()
    league_list = _league_list.offset(skip).limit(limit).all()
    return total, league_list


def get_league_info(db: Session, league_id: int):
    league = db.query(LeagueInfo).get(league_id)
    return league


def create_league_info(db: Session, league_info: League):
    db_league = LeagueInfo(
        league_id=league_info.league_id,
        league_name=league_info.league_name,
        league_creator=league_info.league_creator,
        league_create_date=league_info.league_create_date,
        introduce_league=league_info.introduce_league,
        league_image_link=league_info.league_image_link,
        league_start_date=league_info.league_start_date,
        league_end_date=league_info.league_end_date,
        league_status=league_info.league_status,
        remark=league_info.remark
    )
    db.add(db_league)
    db.commit()


def update_league_info(db: Session, league_info: League, league_update: LeagueUpdate):
    league_info.league_id = league_update.league_id,
    league_info.league_name = league_update.league_name,
    league_info.introduce_league = league_update.introduce_league
    league_info.league_image_link = league_update.league_image_link
    league_info.league_start_date = league_update.league_start_date
    league_info.league_end_date = league_update.league_end_date
    league_info.league_status = league_update.league_status
    league_info.remark = league_update.remark
    db.add(league_info)
    db.commit()


def delete_league(db: Session, db_league: League):
    db.delete(db_league)
    db.commit()
