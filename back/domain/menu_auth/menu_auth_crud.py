from domain.menu_auth.menu_auth_schema import MenuAuth, MenuAuthUpdate
from models import MenuAuthInfo
from sqlalchemy.orm import Session


def get_menu_auth_list(db: Session, skip: int = 0, limit: int = 10):
    _menu_auth_list = db.query(MenuAuthInfo) \
        .order_by(MenuAuthInfo.create_date.desc())
    total = _menu_auth_list.count()
    menu_auth_list = _menu_auth_list.offset(skip).limit(limit).all()
    return total, menu_auth_list


def get_menu_auth_info(db: Session, menu_auth_id: int):
    menu_auth = db.query(MenuAuthInfo).get(menu_auth_id)
    return menu_auth


def create_menu_auth_info(db: Session, menu_auth_info: MenuAuth):
    db_menu_auth = MenuAuthInfo(
        menu_auth_id=menu_auth_info.menu_auth_id,
        menu_id=menu_auth_info.menu_id,
        create_date=menu_auth_info.create_date,
        delete_date=menu_auth_info.delete_date,
        remark=menu_auth_info.remark,
    )
    db.add(db_menu_auth)
    db.commit()


def update_menu_auth_info(db: Session, menu_auth_info: MenuAuth, menu_auth_update: MenuAuthUpdate):
    menu_auth_info.menu_auth_id = menu_auth_update.menu_auth_id,
    menu_auth_info.menu_id = menu_auth_update.menu_id,
    menu_auth_info.delete_date = menu_auth_update.delete_date,
    menu_auth_info.remark = menu_auth_update.remark,
    db.add(menu_auth_info)
    db.commit()


def delete_menu_auth(db: Session, db_menu_auth: MenuAuth):
    db.delete(db_menu_auth)
    db.commit()
