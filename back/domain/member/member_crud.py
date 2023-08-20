import datetime

from passlib.context import CryptContext
from domain.member.member_schema import Member, MemberUpdate
from models import MemberInfo
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def get_member_list(db: Session, skip: int = 0, limit: int = 10):
    _member_list = db.query(MemberInfo) \
        .order_by(MemberInfo.reg_date.desc())
    total = _member_list.count()
    member_list = _member_list.offset(skip).limit(limit).all()
    return total, member_list


def get_member_info(db: Session, member_id: int):
    member = db.query(MemberInfo).get(member_id)
    return member


def create_member_info(db: Session, member_info: Member):
    db_member = MemberInfo(
        member_id=member_info.member_id,
        member_nick_name=member_info.member_nick_name,
        reg_date=datetime.datetime.now(),
        with_date=None,
        phone_num=member_info.phone_num,
        introduce_member=member_info.introduce_member,
        consent_yn=member_info.consent_yn,
        consent_date=member_info.consent_date,
        adver_yn=member_info.adver_yn,
        adver_date=member_info.adver_date,
        remark=member_info.remark
    )
    db.add(db_member)
    db.commit()


def get_existing_user(db: Session, member_create: Member):
    return db.query(MemberInfo).filter(
        MemberInfo.member_id == member_create.member_id
    ).first()


def update_member_info(db: Session, member_info: Member, member_update: MemberUpdate):
    member_info.member_nick_name = member_update.member_nick_name,
    member_info.phone_num = member_update.phone_num,
    member_info.introduce_member = member_update.introduce_member
    member_info.remark = member_update.remark
    db.add(member_info)
    db.commit()


def delete_member(db: Session, db_member: Member):
    db.delete(db_member)
    db.commit()
