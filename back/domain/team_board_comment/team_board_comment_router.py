import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import get_db

from domain.team_board_comment import team_board_comment_crud
from domain.team_board_comment.team_board_comment_schema import TeamBoardComment, TeamBoardCommentUpdate, TeamBoardCommentDelete, TeamBoardCommentList

router = APIRouter(
    prefix="/api/team_board_comment",
)


@router.get("/list", response_model=TeamBoardCommentList)
def team_board_comment_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _team_board_comment_list = team_board_comment_crud.get_team_board_comment_list(db, skip=page * size, limit=size)
    return {
        'total': total,
        'team_board_comment_list': _team_board_comment_list
    }


@router.get("/detail/{team_board_comment_id}", response_model=TeamBoardComment)
def team_board_comment_detail(team_board_comment_id: int, db: Session = Depends(get_db)):
    team_board_comment = team_board_comment_crud.get_team_board_comment_info(db, team_board_comment_id=team_board_comment_id)
    return team_board_comment


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def team_board_comment_create(_team_board_comment_info: TeamBoardComment, db: Session = Depends(get_db)):
    _team_board_comment_info.write_date = datetime.datetime.now()
    team_board_comment_crud.create_team_board_comment_info(db, team_board_comment_info=_team_board_comment_info)


@router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def team_board_comment_update(_team_board_comment_update: TeamBoardCommentUpdate,
                db: Session = Depends(get_db)):
    db_team_board_comment = team_board_comment_crud.get_team_board_comment_info(db, team_board_comment_id=_team_board_comment_update.comment_id)
    if not db_team_board_comment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수 없습니다.")
    team_board_comment_crud.update_team_board_comment_info(db=db, team_board_comment_info=db_team_board_comment, team_board_comment_update=_team_board_comment_update)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def team_board_comment_delete(_team_board_comment_delete: TeamBoardCommentDelete,
                db: Session = Depends(get_db)):
    db_team_board_comment = team_board_comment_crud.get_team_board_comment_info(db, team_board_comment_id=_team_board_comment_delete.comment_id)
    if not db_team_board_comment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    team_board_comment_crud.delete_team_board_comment(db=db, db_team_board_comment=db_team_board_comment)


