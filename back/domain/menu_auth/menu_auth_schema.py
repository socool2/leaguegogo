import datetime

from pydantic import BaseModel


class MenuAuth(BaseModel):
    menu_auth_id: int
    menu_id: int
    create_date: datetime.datetime
    delete_date: datetime.datetime | None
    remark: str | None

    class Config:
        from_attributes = True


class MenuAuthList(BaseModel):
    total: int = 0
    menu_auth_list: list[MenuAuth] = []


class MenuAuthUpdate(BaseModel):
    menu_auth_id: int
    menu_id: int
    delete_date: datetime.datetime | None
    remark: str | None


class MenuAuthDelete(BaseModel):
    menu_auth_id: int
