import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.member import member_schema, member_crud

router = APIRouter(
    prefix="/api/member",
)


@router.get("/list", response_model=member_schema.MemberList)
def member_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _member_list = member_crud.get_member_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'member_list': _member_list
    }


@router.get("/detail/{member_id}", response_model=member_schema.Member)
def member_detail(member_id: str, db: Session = Depends(get_db)):
    member = member_crud.get_member_info(db, member_id=member_id)
    return member


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def member_create(_member_info: member_schema.Member, db: Session = Depends(get_db)):
    member = member_crud.get_existing_user(db, member_create=_member_info)
    if member:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='이미 존재하는 사용자입니다.')
    _member_info.reg_date = datetime.datetime.now()
    member_crud.create_member_info(db, member_info=_member_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def member_update(_member_update: member_schema.MemberUpdate,
                  db: Session = Depends(get_db)):
    db_member = member_crud.get_member_info(db, member_id=_member_update.member_id)
    if not db_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    member_crud.update_member_info(db=db, member_info=db_member, member_update=_member_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def member_delete(_member_delete: member_schema.MemberDelete,
                  db: Session = Depends(get_db)):
    db_member = member_crud.get_member_info(db, member_id=_member_delete.member_id)
    if not db_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    member_crud.delete_member(db=db, db_member=db_member)

