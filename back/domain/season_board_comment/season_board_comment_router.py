import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.season_board_comment import season_board_comment_schema, season_board_comment_crud

router = APIRouter(
    prefix="/api/season_board_comment",
)


@router.get("/list", response_model=season_board_comment_schema.SeasonBoardCommentList)
def season_board_comment_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _season_board_comment_list = season_board_comment_crud.get_season_board_comment_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'season_board_comment_list': _season_board_comment_list
    }


@router.get("/detail/{season_board_comment_id}", response_model=season_board_comment_schema.SeasonBoardComment)
def season_board_comment_detail(season_board_comment_id: int, db: Session = Depends(get_db)):
    season_board_comment = season_board_comment_crud.get_season_board_comment_info(db, season_board_comment_id=season_board_comment_id)
    return season_board_comment


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def season_board_comment_create(_season_board_comment_info: season_board_comment_schema.SeasonBoardComment, db: Session = Depends(get_db)):
    _season_board_comment_info.write_date = datetime.datetime.now()
    season_board_comment_crud.create_season_board_comment_info(db, season_board_comment_info=_season_board_comment_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def season_board_comment_update(_season_board_comment_update: season_board_comment_schema.SeasonBoardCommentUpdate,
                db: Session = Depends(get_db)):
    db_season_board_comment = season_board_comment_crud.get_season_board_comment_info(db, season_board_comment_id=_season_board_comment_update.comment_id)
    if not db_season_board_comment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    season_board_comment_crud.update_season_board_comment_info(db=db, season_board_comment_info=db_season_board_comment, season_board_comment_update=_season_board_comment_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def season_board_comment_delete(_season_board_comment_delete: season_board_comment_schema.SeasonBoardCommentDelete,
                db: Session = Depends(get_db)):
    db_season_board_comment = season_board_comment_crud.get_season_board_comment_info(db, season_board_comment_id=_season_board_comment_delete.comment_id)
    if not db_season_board_comment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    season_board_comment_crud.delete_season_board_comment(db=db, db_season_board_comment=db_season_board_comment)

