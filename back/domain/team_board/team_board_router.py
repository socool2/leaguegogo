import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.team_board import team_board_crud
from domain.team_board.team_board_schema import TeamBoardList, TeamBoard, TeamBoardUpdate, TeamBoardDelete

router = APIRouter(
    prefix="/api/team_board",
)


@router.get("/list", response_model=TeamBoardList)
def team_board_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _team_board_list = team_board_crud.get_team_board_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'team_board_list': _team_board_list
    }


@router.get("/detail/{team_board_id}", response_model=TeamBoard)
def team_board_detail(team_board_id: int, db: Session = Depends(get_db)):
    team_board = team_board_crud.get_team_board_info(db, team_board_id=team_board_id)
    return team_board


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def team_board_create(_team_board_info: TeamBoard, db: Session = Depends(get_db)):
    _team_board_info.board_date = datetime.datetime.now()
    team_board_crud.create_team_board_info(db, team_board_info=_team_board_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def board_update(_team_board_update: TeamBoardUpdate,
                db: Session = Depends(get_db)):
    db_team_board = team_board_crud.get_team_board_info(db, board_id=_team_board_update.board_id)
    if not db_team_board:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    team_board_crud.update_team_board_info(db=db, team_board_info=db_team_board, team_board_update=_team_board_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def board_delete(_team_board_delete: TeamBoardDelete,
                db: Session = Depends(get_db)):
    db_team_board = team_board_crud.get_team_board_info(db, board_id=_team_board_delete.board_id)
    if not db_team_board:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    team_board_crud.delete_team_board(db=db, db_team_board=db_team_board)


