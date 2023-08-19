import {API_URL} from "$lib/request/base";

export const setRoundResult = async (gameId: string) =>{
  const response = await fetch(`${API_URL}/game/${gameId}`);
  return await response.json();
}
