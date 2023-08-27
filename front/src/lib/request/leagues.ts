import {API_URL} from "$lib/request/base";

export const getLeagues = async () =>{
  const response = await fetch(`${API_URL}/api/league/list`);
  return await response.json();
}

export const getLeagueById = async (league_id: string) =>{
  const response = await fetch(`${API_URL}/api/league/detail/`+league_id);
  return await response.json();
}

export const getLeagueByName = async (league_name:string) =>{
  const response = await fetch(`${API_URL}/api/league/name/`+league_name);
  return await response.json();
}

type League = {
  remark: string | null
  league_status: string;
  league_create_date: Date;
  league_creator: string;
  league_name: string
  introduce_league: string
  league_image_link: string| null
  league_start_date: Date | string
  league_end_date: Date | string
}

type LeagueUpdate = {
  league_id: number
  remark: string | null
  league_status: string;
  league_create_date: Date;
  league_creator: string;
  league_name: string
  introduce_league: string
  league_image_link: string| null
  league_start_date: Date | string
  league_end_date: Date | string
}

export const setLeagues = async (leagueInfo: League) =>{
  leagueInfo.league_creator = 'admin'
  leagueInfo.league_create_date = new Date()
  leagueInfo.league_start_date = new Date(leagueInfo.league_start_date)
  leagueInfo.league_end_date = new Date(leagueInfo.league_end_date)
  leagueInfo.league_status = 'waiting'
  leagueInfo.remark = ''

  return await fetch(`${API_URL}/api/league/create`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(leagueInfo),
  })
}

export const updateLeague = async (leagueInfo: LeagueUpdate)=>{
  leagueInfo.league_status = 'waiting'
  leagueInfo.remark = ''
  console.log(JSON.stringify(leagueInfo))

  return await fetch(`${API_URL}/api/league/update`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(leagueInfo),
  })
}