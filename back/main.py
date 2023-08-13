from fastapi import FastAPI
import uvicorn

from domain.game import game_router
from domain.game_member import game_member_router
from domain.league import league_router
from domain.member import member_router
from domain.season import season_router
from domain.season_board import season_board_router
from domain.season_board_comment import season_board_comment_router
from domain.season_team import season_team_router
from domain.season_team_history import season_team_history_router
from domain.setting_status import setting_status_router
from domain.supporters import supporters_router
from domain.team import team_router
from domain.team_board import team_board_router
from domain.team_board_comment import team_board_comment_router
from domain.team_member import team_member_router
from domain.menu import menu_router
from domain.menu_auth import menu_auth_router

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

app.include_router(member_router.router)
app.include_router(team_router.router)
app.include_router(team_member_router.router)
app.include_router(supporters_router.router)
app.include_router(league_router.router)
app.include_router(season_router.router)
app.include_router(game_member_router.router)
app.include_router(season_board_router.router)
app.include_router(season_board_comment_router.router)
app.include_router(season_team_router.router)
app.include_router(season_team_history_router.router)
app.include_router(setting_status_router.router)
app.include_router(team_board_router.router)
app.include_router(team_board_comment_router.router)
app.include_router(game_router.router)
app.include_router(menu_router.router)
app.include_router(menu_auth_router.router)