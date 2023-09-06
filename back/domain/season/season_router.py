import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db
from domain.game.game_crud import define_game_info
from domain.game.game_schema import Game

from domain.season import season_schema, season_crud
from domain.season.season_schema import Season
from domain.season_team.season_team_schema import SeasonTeamList
from models import SeasonTeamInfo

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


@router.post('/{season_id}/confirm', status_code=status.HTTP_204_NO_CONTENT)
def season_confirm(season_id: int, db: Session = Depends(get_db)):
    db_season: Season = season_crud.get_season_info(db, season_id=season_id)
    teams = db.query(SeasonTeamInfo).filter(SeasonTeamInfo.season_id == season_id).all()

    if not db_season:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')

    # match all teams
    match_date = db_season.main_start_date
    games = []
    try:
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)):
                for k in range(db_season.main_game_cnt):
                    games.append(define_game_info(
                        Game.new_game(season_id=season_id, team1_id=teams[i].team_id, team2_id=teams[j].team_id,
                                      game_round=k + 1, game_type='preli', game_date=match_date)))
                    match_date += datetime.timedelta(days=1)

        db.add_all(games)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='게임 생성에 실패했습니다.')

    db.commit()

    season_crud.confirm_season(db=db, db_season=db_season)
