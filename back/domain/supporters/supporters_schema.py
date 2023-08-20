import datetime

from pydantic import BaseModel


class Supporters(BaseModel):
    supporters_id: int
    team_id: int
    member_id: int
    supp_reg_date: datetime.datetime
    supp_with_date: datetime.datetime | None
    supp_grade: str
    remark: str | None

    class Config:
        from_attributes = True


class SupportersList(BaseModel):
    total: int = 0
    supporters_list: list[Supporters] = []


class SupportersUpdate(BaseModel):
    supporters_id: int
    team_id: int
    member_id: int
    supp_with_date: datetime.datetime | None
    supp_grade: str
    remark: str | None


class SupportersDelete(BaseModel):
    supporters_id: int

