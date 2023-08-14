import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.setting_status import setting_status_crud
from domain.setting_status.setting_status_schema import SettingStatusList, SettingStatus, SettingStatusUpdate, SettingStatusDelete

router = APIRouter(
    prefix="/api/setting_status",
)


@router.get("/list", response_model=SettingStatusList)
def setting_status_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _setting_status_list = setting_status_crud.get_setting_status_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'setting_status_list': _setting_status_list
    }


@router.get("/detail/{setting_status_id}", response_model=SettingStatus)
def setting_status_detail(setting_status_id: int, db: Session = Depends(get_db)):
    setting_status = setting_status_crud.get_setting_status_info(db, setting_status_id=setting_status_id)
    return setting_status


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def setting_status_create(_setting_status_info: SettingStatus, db: Session = Depends(get_db)):
    setting_status_crud.create_setting_status_info(db, setting_status_info=_setting_status_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def setting_status_update(_setting_status_update: SettingStatusUpdate,
                db: Session = Depends(get_db)):
    db_setting_status = setting_status_crud.get_setting_status_info(db, setting_status_id=_setting_status_update.setting_id)
    if not db_setting_status:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    setting_status_crud.update_setting_status_info(db=db, setting_status_info=db_setting_status, setting_status_update=_setting_status_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def setting_status_delete(_setting_status_delete: SettingStatusDelete,
                db: Session = Depends(get_db)):
    db_setting_status = setting_status_crud.get_setting_status_info(db, setting_status_id=_setting_status_delete.setting_id)
    if not db_setting_status:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    setting_status_crud.delete_setting_status(db=db, db_setting_status=db_setting_status)
