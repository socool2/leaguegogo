import datetime

from pydantic import BaseModel


class TeamMember(BaseModel):
    team_member_id: int
    team_id: str
    member_id: str
    team_reg_date: datetime.datetime
    team_with_date: datetime.datetime | None
    team_member_grade: int
    remark: str | None

    class Config:
        from_attributes = True


class TeamMemberList(BaseModel):
    total: int = 0
    team_member_list: list[TeamMember] = []


class TeamMemberUpdate(BaseModel):
    team_member_id: int
    team_id: str
    member_id: str
    team_with_date: datetime.datetime | None
    team_member_grade: int
    remark: str | None


class TeamMemberDelete(BaseModel):
    team_member_id: int