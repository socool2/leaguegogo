import datetime

from pydantic import BaseModel


class SettingStatus(BaseModel):
    setting_id: int
    league_id: int
    passwd_change_yn: str
    passwd_change_date: datetime.datetime
    league_create_yn: str
    league_create_date: datetime.datetime
    season_create_yn: str
    season_create_date: datetime.datetime

    class Config:
        from_attributes = True


class SettingStatusList(BaseModel):
    total: int = 0
    setting_status_list: list[SettingStatus] = []


class SettingStatusUpdate(BaseModel):
    setting_id: int
    league_id: int
    passwd_change_yn: str
    passwd_change_date: datetime.datetime
    league_create_yn: str
    league_create_date: datetime.datetime
    season_create_yn: str
    season_create_date: datetime.datetime


class SettingStatusDelete(BaseModel):
    setting_id: int