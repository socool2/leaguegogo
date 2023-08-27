import {API_URL} from "$lib/request/base";

export const getSeasons = async (seasonId: string) =>{
  const response = await fetch(`${API_URL}/season/${seasonId}`);
  return await response.json();
}

type Season = {
    league_id: number
    season_name: string
    season_start_date: Date | string
    season_end_date: Date | string
    season_desc?: string| null
    season_image_link: string| null
    season_reg_start_date: Date | string
    season_reg_end_date: Date | string
    preli_yn: string
    main_yn: string
    playoff_yn: string
    preli_game_cnt: number| string | null
    preli_start_date: Date | string
    preli_end_date: Date | string
    main_game_cnt: number| string | null
    main_start_date: Date | string
    main_end_date: Date | string
    playoff_game_cnt: number| string | null
    playoff_start_date: Date | string
    playoff_end_date: Date | string
    remark: string | null
    preli_status: string
    main_status: string
    playoff_status: string
  }

export const setSeason = async (seasonInfo: Season) => {
    console.log(JSON.stringify(seasonInfo))

    seasonInfo.season_start_date = new Date(seasonInfo.season_start_date)
    seasonInfo.season_end_date = new Date(seasonInfo.season_end_date)
    seasonInfo.season_reg_start_date = new Date(seasonInfo.season_reg_start_date)
    seasonInfo.season_reg_end_date = new Date(seasonInfo.season_reg_end_date)
    seasonInfo.preli_start_date = new Date(seasonInfo.preli_start_date)
    seasonInfo.preli_end_date = new Date(seasonInfo.preli_end_date)
    seasonInfo.main_start_date = new Date(seasonInfo.main_start_date)
    seasonInfo.main_end_date = new Date(seasonInfo.main_end_date)
    seasonInfo.playoff_start_date = new Date(seasonInfo.playoff_start_date)
    seasonInfo.playoff_end_date = new Date(seasonInfo.playoff_end_date)
    seasonInfo.remark = ''
    seasonInfo.preli_status = 'waiting'
    seasonInfo.main_status = 'waiting'
    seasonInfo.playoff_status = 'waiting'
  return await fetch(`${API_URL}/api/season/create`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(seasonInfo),
  })
}