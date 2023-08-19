import {API_URL} from "$lib/request/base";

export const getSeasons = async (seasonId: string) =>{
  const response = await fetch(`${API_URL}/season/${seasonId}`);
  return await response.json();
}
