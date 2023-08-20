import datetime

from pydantic import BaseModel


class Member(BaseModel):
    member_id: int
    member_nick_name: str
    reg_date: datetime.datetime
    with_date: datetime.datetime | None
    phone_num: str
    introduce_member: str | None
    consent_yn: str
    consent_date: datetime.datetime
    adver_yn: str
    adver_date: datetime.datetime
    remark: str | None

    class Config:
        from_attributes = True

    # @validator('member_id', 'member_nick_name', 'phone_num', 'member_grade',
    #            'introduce_member')
    # def not_empty(cls, v):
    #     if not v or not v.strip():
    #         raise ValueError('빈 값은 허용되지 않습니다.')
    #     return v


class MemberList(BaseModel):
    total: int = 0
    member_list: list[Member] = []


class MemberUpdate(BaseModel):
    member_id: int
    member_nick_name: str
    phone_num: str
    introduce_member: str | None
    remark: str | None


class MemberDelete(BaseModel):
    member_id: int

