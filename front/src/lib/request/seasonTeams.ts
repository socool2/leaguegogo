import {API_URL} from "$lib/request/base";

export const getSeasonTeam = async (seasonId: string) =>{
  const response = await fetch(`${API_URL}/season_team/${seasonId}`);
  return await response.json();
}