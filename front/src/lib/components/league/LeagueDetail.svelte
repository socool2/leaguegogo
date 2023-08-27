<script lang="ts">

  import {onMount} from "svelte";
  import {getLeagueById} from "$lib/request/leagues"
  import {selectLeagueId} from "$lib/store";
  import {leagueData} from "$lib/store";

  export let league_id = '';

  export let close: () => void;
  let data;
  let league: League = {};

  $selectLeagueId = league_id

  onMount(async () => {
    data = await getLeagueById(league_id)
    league = data
    $leagueData = data
  })
  type League = {
    league_name: string
    introduce_league: string
    league_image_link: string| null
    league_start_date: Date
    league_end_date: Date
    league_create_date: Date
    league_creator: string
    league_status: string
  }

  $: modifyLeagueId = ''

  const modifyLeagueInfo  = (league_id) => {
    modifyLeagueId = league_id;
  }

</script>


<div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <button
    on:click={close}
    class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity">
  <div class="fixed inset-0 z-10 overflow-y-auto">

    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

      <div
        class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg lg:max-w-2xl sm:p-6">
        <div>
          <div class="mt-3 text-center sm:mt-5">
            <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">리그 상세 정보</h3>
            <div class="mt-2">
              {league.league_image_link} :: {league.league_name}<br/>
              리그 기간: {new Date(league.league_start_date).toLocaleDateString("ko")} ~ {new Date(league.league_end_date).toLocaleDateString("ko")}<br/>
              리그 소개 :{league.introduce_league}<br/>
              리그 상태: {league.league_status}<br/>
              리그 개최자: {league.league_creator}<br/>
            </div>
          </div>
        </div>
        <div class="mt-5 sm:mt-6">
          <a href="/league/update">
          <button
            on:click={() => modifyLeagueInfo(league.league_id)}
            type="button"
            class="inline-flex w-full justify-center rounded-md bg-yellow-300 px-3 py-2 text-sm font-semibold text-black shadow-sm hover:bg-yellow-600 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-yellow-600">
            수정하기
          </button>
          </a>
          <button
            on:click={close}
            type="button"
            class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            돌아가기
          </button>
        </div>
      </div>
    </div>
  </div>
</div>