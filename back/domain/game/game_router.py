from domain.game import game_schema, game_crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

router = APIRouter(
    prefix="/api/game",
)


@router.get("/list", response_model=game_schema.GameList)
def game_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _game_list = game_crud.get_game_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'game_list': _game_list
    }


@router.get("/detail/{game_id}", response_model=game_schema.Game)
def game_detail(game_id: str, db: Session = Depends(get_db)):
    game = game_crud.get_game_info(db, game_id=game_id)
    return game


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def game_create(_game_info: game_schema.Game, db: Session = Depends(get_db)):
    game_crud.create_game_info(db, game_info=_game_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def game_update(_game_update: game_schema.GameUpdate,
                db: Session = Depends(get_db)):
    db_game = game_crud.get_game_info(db, game_id=_game_update.game_id)
    if not db_game:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    game_crud.update_game_info(db=db, game_info=db_game, game_update=_game_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def game_delete(_game_delete: game_schema.GameDelete,
                db: Session = Depends(get_db)):
    db_game = game_crud.get_game_info(db, game_id=_game_delete.game_id)
    if not db_game:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    game_crud.delete_game(db=db, db_game=db_game)
