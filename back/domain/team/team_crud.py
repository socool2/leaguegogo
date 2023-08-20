from domain.team import team_schema
from domain.team.team_schema import Team, TeamUpdate
from models import TeamInfo
from sqlalchemy.orm import Session


def get_team_list(db: Session, skip: int = 0, limit: int = 10):
    _team_list = db.query(TeamInfo) \
        .order_by(TeamInfo.team_create_date.desc())
    total = _team_list.count()
    team_list = _team_list.offset(skip).limit(limit).all()
    return total, team_list


def get_team_info(db: Session, team_id: int):
    team = db.query(TeamInfo).get(team_id)
    return team


def create_team_info(db: Session, team_info: team_schema.Team):
    db_team = TeamInfo(
        team_id=team_info.team_id,
        team_name=team_info.team_name,
        team_creator=team_info.team_creator,
        introduce_team=team_info.introduce_team,
        team_image_link=team_info.team_image_link,
        team_create_date=team_info.team_create_date,
        team_close_date=team_info.team_close_date,
        remark=team_info.remark
    )
    db.add(db_team)
    db.commit()


def get_existing_team_name(db: Session, team_create: team_schema.Team):
    return db.query(TeamInfo).filter(TeamInfo.team_name == team_create.team_name).first()


def update_team_info(db: Session, team_info: Team, team_update: TeamUpdate):
    team_info.team_id = team_update.team_id,
    team_info.team_name = team_update.team_name,
    team_info.introduce_team = team_update.introduce_team
    team_info.team_image_link = team_update.team_image_link
    team_info.team_close_date = team_update.team_close_date
    db.add(team_info)
    db.commit()


def delete_team(db: Session, db_team: Team):
    db.delete(db_team)
    db.commit()
