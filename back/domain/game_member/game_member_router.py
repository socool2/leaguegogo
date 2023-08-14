import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.game_member import game_member_crud
from domain.game_member.game_member_schema import GameMemberList, GameMember, GameMemberUpdate, GameMemberDelete

router = APIRouter(
    prefix="/api/game_member",
)


@router.get("/list", response_model=GameMemberList)
def game_member_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _game_member_list = game_member_crud.get_game_member_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'game_member_list': _game_member_list
    }


@router.get("/detail/{game_member_id}", response_model=GameMember)
def game_member_detail(game_member_id: int, db: Session = Depends(get_db)):
    game_member = game_member_crud.get_game_member_info(db, game_member_id=game_member_id)
    return game_member


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def game_member_create(_game_member_info: GameMember, db: Session = Depends(get_db)):
    game_member_crud.create_game_member_info(db, game_member_info=_game_member_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def game_member_update(_game_member_update: GameMemberUpdate,
                db: Session = Depends(get_db)):
    db_game_member = game_member_crud.get_game_member_info(db, game_member_id=_game_member_update.game_member_id)
    if not db_game_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    game_member_crud.update_game_member_info(db=db, game_member_info=db_game_member, game_member_update=_game_member_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def game_member_delete(_game_member_delete: GameMemberDelete,
                db: Session = Depends(get_db)):
    db_game_member = game_member_crud.get_game_member_info(db, game_member_id=_game_member_delete.game_member_id)
    if not db_game_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    game_member_crud.delete_game_member(db=db, db_game_member=db_game_member)

