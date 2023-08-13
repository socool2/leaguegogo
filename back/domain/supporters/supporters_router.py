import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.supporters import supporters_crud
from domain.supporters.supporters_schema import SupportersList, Supporters, SupportersUpdate, SupportersDelete

router = APIRouter(
    prefix="/api/supporters",
)


@router.get("/list", response_model=SupportersList)
def supporters_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _supporters_list = supporters_crud.get_supporters_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'supporters_list': _supporters_list
    }


@router.get("/detail/{supporters_id}", response_model=Supporters)
def supporters_detail(supporters_id: int, db: Session = Depends(get_db)):
    supporters = supporters_crud.get_supporters_info(db, supporters_id=supporters_id)
    return supporters


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def supporters_create(_supporters_info: Supporters, db: Session = Depends(get_db)):
    _supporters_info.supp_reg_date = datetime.datetime.now()
    supporters_crud.create_supporters_info(db, supporters_info=_supporters_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def supporters_update(_supporters_update: SupportersUpdate,
                db: Session = Depends(get_db)):
    db_supporters = supporters_crud.get_supporters_info(db, supporters_id=_supporters_update.supporters_id)
    if not db_supporters:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    supporters_crud.update_supporters_info(db=db, supporters_info=db_supporters, supporters_update=_supporters_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def supporters_delete(_supporters_delete: SupportersDelete,
                db: Session = Depends(get_db)):
    db_supporters = supporters_crud.get_supporters_info(db, supporters_id=_supporters_delete.supporters_id)
    if not db_supporters:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    supporters_crud.delete_supporters(db=db, db_supporters=db_supporters)
