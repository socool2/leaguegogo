import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.menu import menu_crud
from domain.menu.menu_schema import Menu, MenuUpdate, MenuList, MenuDelete

router = APIRouter(
    prefix="/api/menu",
)


@router.get("/list", response_model=MenuList)
def menu_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _menu_list = menu_crud.get_menu_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'menu_list': _menu_list
    }


@router.get("/detail/{menu_id}", response_model=Menu)
def menu_detail(menu_id: str, db: Session = Depends(get_db)):
    menu = menu_crud.get_menu_info(db, menu_id=menu_id)
    return menu


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def menu_create(_menu_info: Menu, db: Session = Depends(get_db)):
    _menu_info.create_date = datetime.datetime.now()
    menu_crud.create_menu_info(db, menu_info=_menu_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def menu_update(_menu_update: MenuUpdate,
                  db: Session = Depends(get_db)):
    db_menu = menu_crud.get_menu_info(db, menu_id=_menu_update.menu_id)
    if not db_menu:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    menu_crud.update_menu_info(db=db, menu_info=db_menu, menu_update=_menu_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def menu_delete(_menu_delete: MenuDelete,
                  db: Session = Depends(get_db)):
    db_menu = menu_crud.get_menu_info(db, menu_id=_menu_delete.menu_id)
    if not db_menu:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    menu_crud.delete_menu(db=db, db_menu=db_menu)

