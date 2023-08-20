from domain.season_team_history.season_team_history_schema import SeasonTeamHistoryUpdate, SeasonTeamHistory
from models import SeasonTeamHistory
from sqlalchemy.orm import Session


def get_season_team_history_list(db: Session, skip: int = 0, limit: int = 10):
    _season_team_history_list = db.query(SeasonTeamHistory) \
        .order_by(SeasonTeamHistory.history_date.desc())
    total = _season_team_history_list.count()
    season_team_history_list = _season_team_history_list.offset(skip).limit(limit).all()
    return total, season_team_history_list


def get_season_team_history_info(db: Session, season_team_history_id: int):
    season_team_history = db.query(SeasonTeamHistory).get(season_team_history_id)
    return season_team_history


def create_season_team_history_info(db: Session,
                                    season_team_history_info: SeasonTeamHistory):
    db_season_team_history = SeasonTeamHistory(
        history_id=season_team_history_info.history_id,
        season_id=season_team_history_info.season_id,
        team_id=season_team_history_info.team_id,
        history_type=season_team_history_info.history_type,
        history_date=season_team_history_info.history_date,
        enter_date=season_team_history_info.enter_date,
        enter_manager_id=season_team_history_info.enter_manager_id,
        remark=season_team_history_info.remark
    )
    db.add(db_season_team_history)
    db.commit()


def update_season_team_history_info(db: Session, season_team_history_info: SeasonTeamHistory, season_team_history_update: SeasonTeamHistoryUpdate):
    season_team_history_info.history_id = season_team_history_update.history_id,
    season_team_history_info.season_id = season_team_history_update.season_id,
    season_team_history_info.team_id = season_team_history_update.team_id
    season_team_history_info.history_type = season_team_history_update.history_type
    season_team_history_info.history_date = season_team_history_update.history_date
    season_team_history_info.enter_date = season_team_history_update.enter_date
    season_team_history_info.enter_manager_id = season_team_history_update.enter_manager_id
    season_team_history_info.remark = season_team_history_update.remark
    db.add(season_team_history_info)
    db.commit()


def delete_season_team_history(db: Session, db_season_team_history: SeasonTeamHistory):
    db.delete(db_season_team_history)
    db.commit()
