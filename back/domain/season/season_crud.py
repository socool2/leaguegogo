from domain.season.season_schema import Season, SeasonUpdate
from models import SeasonInfo
from sqlalchemy.orm import Session


def get_season_list(db: Session, skip: int = 0, limit: int = 10):
    _season_list = db.query(SeasonInfo) \
        .order_by(SeasonInfo.season_start_date.desc())
    total = _season_list.count()
    season_list = _season_list.offset(skip).limit(limit).all()
    return total, season_list


def get_season_info(db: Session, season_id: int):
    season = db.query(SeasonInfo).get(season_id)
    return season


def create_season_info(db: Session, season_info: Season):
    db_season = SeasonInfo(
        season_id=season_info.season_id,
        league_id=season_info.league_id,
        season_name=season_info.season_name,
        season_start_date=season_info.season_start_date,
        season_end_date=season_info.season_end_date,
        season_desc=season_info.season_desc,
        season_image_link=season_info.season_image_link,
        season_reg_start_date=season_info.season_reg_start_date,
        season_reg_end_date=season_info.season_reg_end_date,
        preli_yn=season_info.preli_yn,
        preli_game_cnt=season_info.preli_game_cnt,
        preli_start_date=season_info.preli_start_date,
        preli_end_date=season_info.preli_end_date,
        preli_status=season_info.preli_status,
        main_yn=season_info.main_yn,
        main_game_cnt=season_info.main_game_cnt,
        main_start_date=season_info.main_start_date,
        main_end_date=season_info.main_end_date,
        main_status=season_info.main_status,
        playoff_yn=season_info.playoff_yn,
        playoff_game_cnt=season_info.playoff_game_cnt,
        playoff_start_date=season_info.playoff_start_date,
        playoff_end_date=season_info.playoff_end_date,
        playoff_status=season_info.playoff_status,
        remark=season_info.remark
    )
    db.add(db_season)
    db.commit()
    
    
def update_season_info(db: Session, season_info: Season, season_update: SeasonUpdate):
    season_info.season_id = season_update.season_id,
    season_info.league_id = season_update.league_id,
    season_info.season_name = season_update.season_name,
    season_info.season_start_date = season_update.season_start_date,
    season_info.season_end_date = season_update.season_end_date,
    season_info.season_desc = season_update.season_desc,
    season_info.season_image_link = season_update.season_image_link,
    season_info.season_reg_start_date = season_update.season_reg_start_date,
    season_info.season_reg_end_date = season_update.season_reg_end_date,
    season_info.preli_yn = season_update.preli_yn,
    season_info.preli_game_cnt = season_update.preli_game_cnt,
    season_info.preli_start_date = season_update.preli_start_date,
    season_info.preli_end_date = season_update.preli_end_date,
    season_info.preli_status = season_update.preli_status,
    season_info.main_yn = season_update.main_yn
    season_info.main_game_cnt = season_update.main_game_cnt
    season_info.main_start_date = season_update.main_start_date
    season_info.main_end_date = season_update.main_end_date
    season_info.main_status = season_update.main_status
    season_info.playoff_yn = season_update.playoff_yn
    season_info.playoff_game_cnt = season_update.playoff_game_cnt
    season_info.playoff_start_date = season_update.playoff_start_date
    season_info.playoff_end_date = season_update.playoff_end_date
    season_info.playoff_status = season_update.playoff_status
    season_info.remark = season_update.remark
    db.add(season_info)
    db.commit()


def delete_season(db: Session, db_season: Season):
    db.delete(db_season)
    db.commit()
