import {writable} from "svelte/store";

const persist_storage  = (key: string, initValue: string | number) => {
    const storedValue = localStorage.getItem(key);
    const store = writable(storedValue != null? JSON.parse(storedValue):initValue);
    store.subscribe((val)=>{
        localStorage.setItem(key, JSON.stringify(val))
    })
    return store
}
export const selectLeagueName = persist_storage('selectLeagueName','0')
export const selectLeagueId = persist_storage('selectLeagueId',0)
export const leagueData=persist_storage('leagueData','')