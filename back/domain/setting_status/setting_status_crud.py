from domain.setting_status.setting_status_schema import SettingStatus, SettingStatusUpdate
from models import SettingStatus
from sqlalchemy.orm import Session


def get_setting_status_list(db: Session, skip: int = 0, limit: int = 10):
    _setting_status_list = db.query(SettingStatus) \
        .order_by(SettingStatus.season_create_date.desc())
    total = _setting_status_list.count()
    setting_status_list = _setting_status_list.offset(skip).limit(limit).all()
    return total, setting_status_list


def get_setting_status_info(db: Session, setting_status_id: int):
    setting_status = db.query(SettingStatus).get(setting_status_id)
    return setting_status


def create_setting_status_info(db: Session, setting_status_info: SettingStatus):
    db_setting_status = SettingStatus(
        setting_id=setting_status_info.setting_id,
        league_id=setting_status_info.league_id,
        passwd_change_yn=setting_status_info.passwd_change_yn,
        passwd_change_date=setting_status_info.passwd_change_date,
        league_create_yn=setting_status_info.league_create_yn,
        league_create_date=setting_status_info.league_create_date,
        season_create_yn=setting_status_info.season_create_yn,
        season_create_date=setting_status_info.season_create_date
    )
    db.add(db_setting_status)
    db.commit()


def update_setting_status_info(db: Session, setting_status_info: SettingStatus, setting_status_update: SettingStatusUpdate):
    setting_status_info.setting_id = setting_status_update.setting_id,
    setting_status_info.league_id = setting_status_update.league_id,
    setting_status_info.passwd_change_yn = setting_status_update.passwd_change_yn
    setting_status_info.passwd_change_date = setting_status_update.passwd_change_date
    setting_status_info.league_create_yn = setting_status_update.league_create_yn
    setting_status_info.league_create_date = setting_status_update.league_create_date
    setting_status_info.season_create_yn = setting_status_update.season_create_yn
    setting_status_info.season_create_date = setting_status_update.season_create_date
    db.add(setting_status_info)
    db.commit()


def delete_setting_status(db: Session, db_setting_status: SettingStatus):
    db.delete(db_setting_status)
    db.commit()
