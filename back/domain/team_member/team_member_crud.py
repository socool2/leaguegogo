from domain.team_member.team_member_schema import TeamMember, TeamMemberUpdate
from models import TeamMemberInfo
from sqlalchemy.orm import Session


def get_team_member_list(db: Session, skip: int = 0, limit: int = 10):
    _team_member_list = db.query(TeamMemberInfo) \
        .order_by(TeamMemberInfo.team_reg_date.desc())
    total = _team_member_list.count()
    team_member_list = _team_member_list.offset(skip).limit(limit).all()
    return total, team_member_list


def get_team_member_info(db: Session, team_member_id: str):
    team_member = db.query(TeamMemberInfo).get(team_member_id)
    return team_member


def create_team_member_info(db: Session, team_member_info: TeamMember):
    db_team_member = TeamMemberInfo(
        member_id=team_member_info.member_id,
        team_id=team_member_info.team_id,
        team_reg_date=team_member_info.team_reg_date,
        team_member_grade=team_member_info.team_member_grade
    )
    db.add(db_team_member)
    db.commit()


def get_existing_team_member_id(db: Session, team_member_create: TeamMember):
    return db.query(TeamMemberInfo).filter(TeamMemberInfo.team_member_id == team_member_create.team_member_id).first()


def update_team_member_info(db: Session, team_member_info: TeamMember, team_member_update: TeamMemberUpdate):
    team_member_info.team_member_id = team_member_update.team_member_id,
    team_member_info.team_id = team_member_update.team_id,
    team_member_info.member_id = team_member_update.member_id,
    team_member_info.team_with_date = team_member_update.team_with_date
    team_member_info.team_member_grade = team_member_update.team_member_grade
    team_member_info.remark = team_member_update.remark
    db.add(team_member_info)
    db.commit()


def delete_team_member(db: Session, db_team_member: TeamMemberInfo):
    db.delete(db_team_member)
    db.commit()
