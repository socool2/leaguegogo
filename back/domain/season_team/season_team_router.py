import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.season_team import season_team_schema, season_team_crud

router = APIRouter(
    prefix="/api/season_team",
)


@router.get("/list", response_model=season_team_schema.SeasonTeamList)
def season_team_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _season_team_list = season_team_crud.get_season_team_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'season_team_list': _season_team_list
    }


@router.get("/detail/{season_team_id}", response_model=season_team_schema.SeasonTeam)
def season_team_detail(season_team_id: str, db: Session = Depends(get_db)):
    season_team = season_team_crud.get_season_team_info(db, season_team_id=season_team_id)
    return season_team


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def season_team_create(_season_team_info: season_team_schema.SeasonTeam, db: Session = Depends(get_db)):
    _season_team_info.reg_date = datetime.datetime.now()
    season_team_crud.create_season_team_info(db, season_team_info=_season_team_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def team_update(_season_team_update: season_team_schema.SeasonTeamUpdate,
                db: Session = Depends(get_db)):
    db_season_team = season_team_crud.get_season_team_info(db, season_team_id=_season_team_update.season_team_id)
    if not db_season_team:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    season_team_crud.update_season_team_info(db=db, season_team_info=db_season_team, season_team_update=_season_team_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def team_delete(_season_team_delete: season_team_schema.SeasonTeamDelete,
                db: Session = Depends(get_db)):
    db_season_team = season_team_crud.get_season_team_info(db, season_team_id=_season_team_delete.season_team_id)
    if not db_season_team:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    season_team_crud.delete_season_team(db=db, db_season_team=db_season_team)
