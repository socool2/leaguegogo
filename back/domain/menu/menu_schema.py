import datetime

from pydantic import BaseModel


class Menu(BaseModel):
    menu_id: int
    menu_name: str
    menu_desc: str
    create_date: datetime.datetime
    delete_date: datetime.datetime | None
    upper_menu_id: int
    help: str
    remark: str | None

    class Config:
        from_attributes = True


class MenuList(BaseModel):
    total: int = 0
    menu_list: list[Menu] = []


class MenuUpdate(BaseModel):
    menu_name: str
    menu_desc: str
    delete_date: datetime.datetime | None
    upper_menu_id: int
    help: str
    remark: str | None


class MenuDelete(BaseModel):
    menu_id: int