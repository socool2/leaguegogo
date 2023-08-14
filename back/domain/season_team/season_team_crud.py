from domain.season_team.season_team_schema import SeasonTeam, SeasonTeamUpdate
from models import SeasonTeamInfo
from sqlalchemy.orm import Session


def get_season_team_list(db: Session, skip: int = 0, limit: int = 10):
    _season_team_list = db.query(SeasonTeamInfo) \
        .order_by(SeasonTeamInfo.reg_date.desc())
    total = _season_team_list.count()
    season_team_list = _season_team_list.offset(skip).limit(limit).all()
    return total, season_team_list


def get_season_team_info(db: Session, season_team_id: str):
    season_team = db.query(SeasonTeamInfo).get(season_team_id)
    return season_team


def create_season_team_info(db: Session, season_team_info: SeasonTeam):
    db_season_team = SeasonTeamInfo(
        season_team_id=season_team_info.season_team_id,
        season_id=season_team_info.season_id,
        team_id=season_team_info.team_id,
        reg_user_id=season_team_info.reg_user_id,
        reg_date=season_team_info.reg_date,
        reg_cancel_date=season_team_info.reg_cancel_date,
        main_advance_yn=season_team_info.main_advance_yn,
        playoff_advance_yn=season_team_info.playoff_advance_yn,
        remark=season_team_info.remark
    )
    db.add(db_season_team)
    db.commit()


def update_season_team_info(db: Session, season_team_info: SeasonTeam, season_team_update: SeasonTeamUpdate):
    season_team_info.season_team_id = season_team_update.season_team_id,
    season_team_info.season_id = season_team_update.season_id,
    season_team_info.team_id = season_team_update.team_id,
    season_team_info.reg_cancel_date = season_team_update.reg_cancel_date
    season_team_info.main_advance_yn = season_team_update.main_advance_yn
    season_team_info.playoff_advance_yn = season_team_update.playoff_advance_yn
    season_team_info.remark = season_team_update.remark
    db.add(season_team_info)
    db.commit()


def delete_season_team(db: Session, db_season_team: SeasonTeam):
    db.delete(db_season_team)
    db.commit()
