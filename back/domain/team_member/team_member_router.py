import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.team_member import team_member_schema, team_member_crud

router = APIRouter(
    prefix="/api/team_member",
)


@router.get("/list", response_model=team_member_schema.TeamMemberList)
def team_member_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _team_member_list = team_member_crud.get_team_member_list(db, skip=page * size, limit=size)
    print(total)
    return {
        'total': total,
        'team_member_list': _team_member_list
    }


@router.get("/detail/{team_member_id}", response_model=team_member_schema.TeamMember)
def team_member_detail(team_member_id: str, db: Session = Depends(get_db)):
    team_member = team_member_crud.get_team_member_info(db, team_member_id=team_member_id)
    return team_member


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def team_member_create(_team_member_info: team_member_schema.TeamMember, db: Session = Depends(get_db)):
    _team_member_info.team_reg_date = datetime.datetime.now()
    team_member_crud.create_team_member_info(db, team_member_info=_team_member_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def team_member_update(_team_member_update: team_member_schema.TeamMemberUpdate,
                  db: Session = Depends(get_db)):
    db_team_member = team_member_crud.get_team_member_info(db, team_member_id=_team_member_update.team_member_id)
    if not db_team_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    team_member_crud.update_team_member_info(db=db, team_member_info=db_team_member, team_member_update=_team_member_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def team_delete(_team_member_delete: team_member_schema.TeamMemberDelete,
                  db: Session = Depends(get_db)):
    db_team_member = team_member_crud.get_team_member_info(db, team_member_id=_team_member_delete.team_member_id)
    if not db_team_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    team_member_crud.delete_team_member(db=db, db_team_member=db_team_member)

