from pydantic import BaseModel


class GameMember(BaseModel):
    game_member_id: int
    game_id: str
    team_id: str
    member_id: str
    game_position: str
    remark: str

    class Config:
        from_attributes = True


class GameMemberList(BaseModel):
    total: int = 0
    game_list: list[GameMember] = []


class GameMemberUpdate(BaseModel):
    game_member_id: int
    member_id: str
    game_position: str
    remark: str


class GameMemberDelete(BaseModel):
    game_member_id: int