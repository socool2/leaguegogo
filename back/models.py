from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from database import Base


class MemberInfo(Base):
    __tablename__ = "member_info"

    member_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    nick_name = Column(String, nullable=False)
    reg_date = Column(DateTime, nullable=False)
    with_date = Column(DateTime)
    phone_num = Column(String, nullable=False)
    introduce_member = Column(Text)
    profile_image_link = Column(String)
    consent_yn = Column(String, nullable=False)
    consent_date = Column(DateTime, nullable=False)
    adver_yn = Column(String, nullable=False)
    adver_date = Column(DateTime, nullable=False)
    remark = Column(Text)


class TeamInfo(Base):
    __tablename__ = "team_info"

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String, nullable=False)
    team_creator = Column(String, nullable=False)
    introduce_team = Column(Text)
    team_image_link = Column(String)
    team_create_date = Column(DateTime, nullable=False)
    team_close_date = Column(DateTime)
    remark = Column(Text)


class TeamMemberInfo(Base):
    __tablename__ = "team_member_info"

    team_member_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, nullable=False)
    member_id = Column(String, nullable=False)
    team_reg_date = Column(DateTime, nullable=False)
    team_with_date = Column(DateTime)
    team_member_grade = Column(String, nullable=False)
    remark = Column(Text)


class SupportersInfo(Base):
    __tablename__ = "supporters_info"

    supporters_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, nullable=False)
    member_id = Column(Integer, nullable=False)
    supp_reg_date = Column(DateTime, nullable=False)
    supp_with_date = Column(DateTime)
    supp_grade = Column(String, nullable=False)
    remark = Column(Text)


class LeagueInfo(Base):
    __tablename__ = "league_info"

    league_id = Column(Integer, primary_key=True)
    league_name = Column(String, nullable=False)
    league_creator = Column(String, nullable=False)
    league_create_date = Column(DateTime, nullable=False)
    introduce_league = Column(Text)
    league_image_link = Column(String)
    league_start_date = Column(DateTime, nullable=False)
    league_end_date = Column(DateTime, nullable=False)
    league_status = Column(String, nullable=False)
    remark = Column(Text)


class SeasonInfo(Base):
    __tablename__ = "season_info"

    season_id = Column(Integer, primary_key=True)
    league_id = Column(Integer, nullable=False)
    season_name = Column(String, nullable=False)
    season_start_date = Column(DateTime, nullable=False)
    season_end_date = Column(DateTime, nullable=False)
    season_desc = Column(String, nullable=False)
    season_image_link = Column(String)
    season_reg_start_date = Column(DateTime, nullable=False)
    season_reg_end_date = Column(DateTime, nullable=False)
    preli_yn = Column(String)
    preli_game_cnt = Column(Integer)
    preli_start_date = Column(DateTime)
    preli_end_date = Column(DateTime)
    preli_status = Column(String)
    # 프리뷰 상태에서는 main만 사용
    main_yn = Column(String)
    main_game_cnt = Column(Integer)
    main_start_date = Column(DateTime)
    main_end_date = Column(DateTime)
    main_status = Column(String)
    playoff_yn = Column(String)
    playoff_game_cnt = Column(Integer)
    playoff_start_date = Column(DateTime)
    playoff_end_date = Column(DateTime)
    playoff_status = Column(String)
    remark = Column(String)


class GameInfo(Base):
    __tablename__ = "game_info"

    game_id = Column(Integer, primary_key=True)
    season_id = Column(Integer, nullable=False)
    game_type = Column(String)
    game_round = Column(Integer)
    team1_id = Column(Integer)
    team2_id = Column(Integer)
    game_date = Column(DateTime, nullable=False)
    team1_point = Column(Integer, nullable=False)
    team1_result = Column(String, nullable=False)
    team2_point = Column(Integer, nullable=False)
    team2_result = Column(String, nullable=False)
    round_status = Column(String, nullable=False)
    round_video_link = Column(String, nullable=False)
    remark = Column(Text)


class SeasonTeamInfo(Base):
    __tablename__ = "season_team_info"

    season_team_id = Column(Integer, primary_key=True)
    season_id = Column(Integer)
    team_id = Column(Integer)
    reg_user_id = Column(Integer, nullable=False)
    reg_date = Column(DateTime, nullable=False)
    reg_cancel_date = Column(DateTime)
    main_advance_yn = Column(String)
    playoff_advance_yn = Column(String)
    remark = Column(Text)


class SeasonTeamHistory(Base):
    __tablename__ = "season_team_history"

    history_id = Column(Integer, primary_key=True)
    season_id = Column(Integer)
    team_id = Column(Integer)
    history_type = Column(String, nullable=False)
    history_date = Column(DateTime, nullable=False)
    enter_date = Column(DateTime, nullable=False)
    enter_manager_id = Column(Integer, nullable=False)
    remark = Column(Text)


class GameMemberInfo(Base):
    __tablename__ = "game_member_info"
    game_member_id = Column(Integer, primary_key=True)
    game_id = Column(Integer)
    team_id = Column(Integer)
    member_id = Column(Integer)
    game_position = Column(String)
    remark = Column(String)


class SettingStatus(Base):
    __tablename__ = "setting_status"

    setting_id = Column(Integer, primary_key=True)
    league_id = Column(Integer)
    passwd_change_yn = Column(String)
    passwd_change_date = Column(DateTime)
    league_create_yn = Column(String)
    league_create_date = Column(DateTime)
    season_create_yn = Column(String)
    season_create_date = Column(DateTime)


class TeamBoard(Base):
    __tablename__ = "team_board"

    board_id = Column(Integer, primary_key=True)
    team_id = Column(Integer)
    board_type = Column(String)
    board_title = Column(String)
    board_desc = Column(Text)
    board_date = Column(DateTime)
    file_link = Column(String)
    write_member_id = Column(Integer)
    write_date = Column(DateTime)
    delete_date = Column(DateTime)
    comment_yn = Column(String)
    remark = Column(Text)


class TeamBoardComment(Base):
    __tablename__ = "team_board_comment"

    comment_id = Column(Integer, primary_key=True)
    board_id = Column(Integer)
    comment_desc = Column(String)
    write_member_id = Column(Integer)
    write_date = Column(DateTime)
    delete_date = Column(DateTime)
    remark = Column(Text)


class SeasonBoard(Base):
    __tablename__ = "season_board"

    board_id = Column(Integer, primary_key=True)
    season_id = Column(Integer)
    board_title = Column(String)
    board_desc = Column(Text)
    board_date = Column(DateTime)
    file_link = Column(String)
    write_member_id = Column(Integer)
    write_date = Column(DateTime)
    delete_date = Column(DateTime)
    comment_yn = Column(String)
    remark = Column(Text)


class SeasonBoardComment(Base):
    __tablename__ = "season_board_comment"

    comment_id = Column(Integer, primary_key=True)
    board_id = Column(Integer)
    comment_desc = Column(String)
    write_member_id = Column(Integer)
    write_date = Column(DateTime)
    delete_date = Column(DateTime)
    remark = Column(Text)
    upper_comment_id = Column(Integer)


class MenuAuthInfo(Base):
    __tablename__ = "menu_auth"

    menu_auth_id = Column(Integer, primary_key=True)
    menu_id = Column(Integer)
    create_date = Column(DateTime)
    delete_date = Column(DateTime)
    remark = Column(Text)


class MenuInfo(Base):
    __tablename__ = "menu_info"

    menu_id = Column(Integer, primary_key=True)
    menu_name = Column(String, nullable=False)
    menu_desc = Column(String)
    create_date = Column(DateTime, nullable=False)
    delete_date = Column(DateTime)
    upper_menu_id = Column(Integer)
    help = Column(Text)
    remark = Column(Text)