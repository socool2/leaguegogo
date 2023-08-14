import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.league import league_schema, league_crud

router = APIRouter(
    prefix="/api/league",
)


@router.get("/list", response_model=league_schema.LeagueList)
def league_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _league_list = league_crud.get_league_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'league_list': _league_list
    }


@router.get("/detail/{league_id}", response_model=league_schema.League)
def league_detail(league_id: int, db: Session = Depends(get_db)):
    league = league_crud.get_league_info(db, league_id=league_id)
    return league


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def league_create(_league_info: league_schema.League, db: Session = Depends(get_db)):
    _league_info.league_create_date = datetime.datetime.now()
    league_crud.create_league_info(db, league_info=_league_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def league_update(_league_update: league_schema.LeagueUpdate,
                db: Session = Depends(get_db)):
    db_league = league_crud.get_league_info(db, league_id=_league_update.league_id)
    if not db_league:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    league_crud.update_league_info(db=db, league_info=db_league, league_update=_league_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def league_delete(_league_delete: league_schema.LeagueDelete,
                db: Session = Depends(get_db)):
    db_league = league_crud.get_league_info(db, league_id=_league_delete.league_id)
    if not db_league:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    league_crud.delete_league(db=db, db_league=db_league)
