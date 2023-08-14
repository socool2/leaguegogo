import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.team import team_schema, team_crud

router = APIRouter(
    prefix="/api/team",
)


@router.get("/list", response_model=team_schema.TeamList)
def team_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _team_list = team_crud.get_team_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'team_list': _team_list
    }


@router.get("/detail/{team_id}", response_model=team_schema.Team)
def team_detail(team_id: str, db: Session = Depends(get_db)):
    team = team_crud.get_team_info(db, team_id=team_id)
    return team


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def team_create(_team_info: team_schema.Team, db: Session = Depends(get_db)):
    team = team_crud.get_existing_team_name(db, team_create=_team_info)
    if team:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='이미 존재하는 팀명입니다.')
    _team_info.team_create_date = datetime.datetime.now()
    team_crud.create_team_info(db, team_info=_team_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def team_update(_team_update: team_schema.TeamUpdate,
                db: Session = Depends(get_db)):
    db_team = team_crud.get_team_info(db, team_id=_team_update.team_id)
    if not db_team:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    team_crud.update_team_info(db=db, team_info=db_team, team_update=_team_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def team_delete(_team_delete: team_schema.TeamDelete,
                db: Session = Depends(get_db)):
    db_team = team_crud.get_team_info(db, team_id=_team_delete.team_id)
    if not db_team:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    team_crud.delete_team(db=db, db_team=db_team)
