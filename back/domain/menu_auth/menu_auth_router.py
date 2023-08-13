import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.menu_auth import menu_auth_crud
from domain.menu_auth.menu_auth_schema import MenuAuth, MenuAuthUpdate, MenuAuthList, MenuAuthDelete

router = APIRouter(
    prefix="/api/menu_auth",
)


@router.get("/list", response_model=MenuAuthList)
def menu_auth_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _menu_list = menu_auth_crud.get_menu_auth_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'menu_list': _menu_list
    }


@router.get("/detail/{menu_id}", response_model=MenuAuth)
def menu_auth_detail(menu_auth_id: int, db: Session = Depends(get_db)):
    menu = menu_auth_crud.get_menu_auth_info(db, menu_auth_id=menu_auth_id)
    return menu


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def menu_auth_create(_menu_auth_info: MenuAuth, db: Session = Depends(get_db)):
    _menu_auth_info.create_date = datetime.datetime.now()
    menu_auth_crud.create_menu_auth_info(db, menu_auth_info=_menu_auth_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def menu_auth_update(_menu_auth_update: MenuAuthUpdate,
                  db: Session = Depends(get_db)):
    db_menu_auth = menu_auth_crud.get_menu_auth_info(db, menu_auth_id=_menu_auth_update.menu_auth_id)
    if not db_menu_auth:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    menu_auth_crud.update_menu_auth_info(db=db, menu_auth_info=db_menu_auth, menu_auth_update=_menu_auth_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def menu_auth_delete(_menu_auth_delete: MenuAuthDelete,
                  db: Session = Depends(get_db)):
    db_menu_auth = menu_auth_crud.get_menu_auth_info(db, menu_auth_id=_menu_auth_delete.menu_auth_id)
    if not db_menu_auth:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    menu_auth_crud.delete_menu_auth(db=db, db_menu_auth=db_menu_auth)

