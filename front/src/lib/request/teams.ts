import {API_URL} from "$lib/request/base";

export const getTeam = async (teamId: string) =>{
  const response = await fetch(`${API_URL}/teams/${teamId}`);
  return await response.json();
}

export const setEnterMain = async (teamId: string) =>{
  const response = await fetch(`${API_URL}/teams/${teamId}`);
  return await response.json();
}
