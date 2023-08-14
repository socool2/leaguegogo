import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.season_team_history import season_team_history_crud
from domain.season_team_history.season_team_history_schema import SeasonTeamHistory, SeasonTeamHistoryUpdate, SeasonTeamHistoryDelete, SeasonTeamHistoryList

router = APIRouter(
    prefix="/api/season_team_history",
)


@router.get("/list", response_model=SeasonTeamHistoryList)
def season_team_history_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _season_team_history_list = season_team_history_crud.get_season_team_history_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'season_team_history_list': _season_team_history_list
    }


@router.get("/detail/{season_team_history_id}", response_model=SeasonTeamHistory)
def season_team_history_detail(season_team_history_id: str, db: Session = Depends(get_db)):
    season_team_history = season_team_history_crud.get_season_team_history_info(db, season_team_history_id=season_team_history_id)
    return season_team_history


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def season_team_history_create(_season_team_history_info: SeasonTeamHistory, db: Session = Depends(get_db)):
    _season_team_history_info.enter_date = datetime.datetime.now()
    season_team_history_crud.create_season_team_history_info(db, season_team_history_info=_season_team_history_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def season_team_history_update(_season_team_history_update: SeasonTeamHistoryUpdate,
                db: Session = Depends(get_db)):
    db_season_team_history = season_team_history_crud.get_season_team_history_info(db, season_team_history_id=_season_team_history_update.history_id)
    if not db_season_team_history:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    season_team_history_crud.update_season_team_history_info(db=db, season_team_history_info=db_season_team_history, season_team_history_update=_season_team_history_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def season_team_history_delete(_season_team_history_delete: SeasonTeamHistoryDelete,
                db: Session = Depends(get_db)):
    db_season_team_history = season_team_history_crud.get_season_team_history_info(db, season_team_history_id=_season_team_history_delete.history_id)
    if not db_season_team_history:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    season_team_history_crud.delete_season_team_history(db=db, db_season_team_history=db_season_team_history)

