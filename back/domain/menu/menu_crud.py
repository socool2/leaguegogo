from domain.menu.menu_schema import Menu, MenuUpdate
from models import MenuInfo
from sqlalchemy.orm import Session


def get_menu_list(db: Session, skip: int = 0, limit: int = 10):
    _menu_list = db.query(MenuInfo) \
        .order_by(MenuInfo.menu_create_date.desc())
    total = _menu_list.count()
    menu_list = _menu_list.offset(skip).limit(limit).all()
    return total, menu_list


def get_menu_info(db: Session, menu_id: str):
    menu = db.query(MenuInfo).get(menu_id)
    return menu


def create_menu_info(db: Session, menu_info: Menu):
    db_menu = MenuInfo(
        menu_id=menu_info.menu_id,
        menu_name=menu_info.menu_name,
        menu_desc=menu_info.menu_desc,
        create_date=menu_info.create_date,
        delete_date=menu_info.delete_date,
        upper_menu_id=menu_info.upper_menu_id,
        help=menu_info.help,
        remark=menu_info.remark
    )
    db.add(db_menu)
    db.commit()


def update_menu_info(db: Session, menu_info: Menu, menu_update: MenuUpdate):
    menu_info.menu_id = menu_update.menu_id,
    menu_info.menu_name = menu_update.menu_name,
    menu_info.menu_desc = menu_update.menu_desc,
    menu_info.delete_date = menu_update.delete_date,
    menu_info.upper_menu_id = menu_update.upper_menu_id
    menu_info.help = menu_update.help
    menu_info.remark = menu_update.remark
    db.add(menu_info)
    db.commit()


def delete_menu(db: Session, db_menu: Menu):
    db.delete(db_menu)
    db.commit()
