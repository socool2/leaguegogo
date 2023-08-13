import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.season_board import season_board_crud
from domain.season_board.season_board_schema import SeasonBoardList, SeasonBoard, SeasonBoardUpdate, SeasonBoardDelete

router = APIRouter(
    prefix="/api/season_board",
)


@router.get("/list", response_model=SeasonBoardList)
def season_board_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _season_board_list = season_board_crud.get_season_board_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'season_board_list': _season_board_list
    }


@router.get("/detail/{season_board_id}", response_model=SeasonBoard)
def season_board_detail(season_board_id: int, db: Session = Depends(get_db)):
    season_board = season_board_crud.get_season_board_info(db, season_board_id=season_board_id)
    return season_board


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def season_board_create(_season_board_info: SeasonBoard, db: Session = Depends(get_db)):
    _season_board_info.board_date = datetime.datetime.now()
    season_board_crud.create_season_board_info(db, season_board_info=_season_board_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def board_update(_season_board_update: SeasonBoardUpdate,
                db: Session = Depends(get_db)):
    db_season_board = season_board_crud.get_season_board_info(db, board_id=_season_board_update.board_id)
    if not db_season_board:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    season_board_crud.update_season_board_info(db=db, season_board_info=db_season_board, season_board_update=_season_board_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def board_delete(_season_board_delete: SeasonBoardDelete,
                db: Session = Depends(get_db)):
    db_season_board = season_board_crud.get_season_board_info(db, board_id=_season_board_delete.board_id)
    if not db_season_board:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    season_board_crud.delete_season_board(db=db, db_season_board=db_season_board)


