import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.season import season_schema, season_crud

router = APIRouter(
    prefix="/api/season",
)


@router.get("/list", response_model=season_schema.SeasonList)
def season_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _season_list = season_crud.get_season_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'season_list': _season_list
    }


@router.get("/detail/{season_id}", response_model=season_schema.Season)
def season_detail(season_id: int, db: Session = Depends(get_db)):
    season = season_crud.get_season_info(db, season_id=season_id)
    return season


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def season_create(_season_info: season_schema.Season, db: Session = Depends(get_db)):
    season_crud.create_season_info(db, season_info=_season_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def season_update(_season_update: season_schema.SeasonUpdate,
                db: Session = Depends(get_db)):
    db_season = season_crud.get_season_info(db, season_id=_season_update.season_id)
    if not db_season:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    season_crud.update_season_info(db=db, season_info=db_season, season_update=_season_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def season_delete(_season_delete: season_schema.SeasonDelete,
                db: Session = Depends(get_db)):
    db_season = season_crud.get_season_info(db, season_id=_season_delete.season_id)
    if not db_season:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    season_crud.delete_season(db=db, db_season=db_season)
