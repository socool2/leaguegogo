from domain.supporters.supporters_schema import Supporters, SupportersUpdate
from models import SupportersInfo
from sqlalchemy.orm import Session


def get_supporters_list(db: Session, skip: int = 0, limit: int = 10):
    _supporters_list = db.query(SupportersInfo) \
        .order_by(SupportersInfo.supp_reg_date.desc())
    total = _supporters_list.count()
    supporters_list = _supporters_list.offset(skip).limit(limit).all()
    return total, supporters_list


def get_supporters_info(db: Session, supporters_id: int):
    supporters = db.query(SupportersInfo).get(supporters_id)
    return supporters


def create_supporters_info(db: Session, supporters_info: Supporters):
    db_supporters = SupportersInfo(
        supporters_id=supporters_info.supporters_id,
        team_id=supporters_info.team_id,
        member_id=supporters_info.member_id,
        supp_reg_date=supporters_info.supp_reg_date,
        supp_with_date=supporters_info.supp_with_date,
        supp_grade=supporters_info.supp_grade,
        remark=supporters_info.remark
    )
    db.add(db_supporters)
    db.commit()


def update_supporters_info(db: Session, supporters_info: Supporters, supporters_update: SupportersUpdate):
    supporters_info.supporters_id = supporters_update.supporters_id,
    supporters_info.team_id = supporters_update.team_id,
    supporters_info.member_id = supporters_update.member_id
    supporters_info.supp_with_date = supporters_update.supp_with_date
    supporters_info.supp_grade = supporters_update.supp_grade
    supporters_info.remark = supporters_update.remark
    db.add(supporters_info)
    db.commit()


def delete_supporters(db: Session, db_supporters: Supporters):
    db.delete(db_supporters)
    db.commit()
