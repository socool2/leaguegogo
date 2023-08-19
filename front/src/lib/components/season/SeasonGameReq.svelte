<script lang="ts">

  import {onMount} from "svelte";
  import {getSeasonTeam} from "$lib/request/seasonTeams";

  export let season_id = "";
  export let close: () => void;
  let data;
  onMount(async () => {
    data = await getSeasonTeam(season_id)
  })

  type SeasonInfo = {
    season_id: string
    season_name: string
    season_image_link: string
    preli_yn: string
    preli_status: string
    main_yn: string
    main_status: string
    playoff_yn: string
    playoff_status: string
    season_start_date: Date
    season_end_date: Date
  }

  type SeasonTeamInfo = {
    season_id: string
    team_id: string
    main_advance_yn: string
    playoff_advance_yn: string
  }

  const season_game_info: SeasonInfo[] = [
    {
      season_id: "1",
      season_name: "1st Season",
      season_image_link: "image link",
      preli_yn: "yes",
      preli_status: "complete",
      main_yn: "yes",
      main_status: "waiting",
      playoff_yn: "yes",
      playoff_status: "waiting",
      season_start_date: new Date(),
      season_end_date: new Date()
    }
  ]

  const season_team_info: SeasonTeamInfo[] = [
    {
      season_id: "1",
      team_id: "1",
      main_advance_yn: "yes",
      playoff_advance_yn: "waiting"
    }
  ]

  const seasonTeam = {
      season_id: "1",
      season_name: "1st Season",
      season_image_link: "image link",
      preli_yn: "yes",
      preli_status: "complete",
      main_yn: "yes",
      main_status: "waiting",
      playoff_yn: "yes",
      playoff_status: "waiting",
      season_team: season_team_info,
      season_start_date: new Date(),
      season_end_date: new Date()
  }


</script>


<div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <button
    on:click={close}
    class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></button>
  <div class="fixed inset-0 z-10 overflow-y-auto">

    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

      <div
        class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg lg:max-w-2xl sm:p-6">
        <div>
          <div class="mt-3 text-center sm:mt-5">
            <h1 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">게임 생성</h1>
              {seasonTeam.season_image_link} {seasonTeam.season_name}<br/>
            시즌 기간: {seasonTeam.season_start_date.toLocaleDateString("ko")} ~ {seasonTeam.season_end_date.toLocaleDateString("ko")}<br/>
            <div class="mt-2">
              게임 유형은 [예선/본선/결선] 입니다.<br>
              현재 [접수한 /본선 진출 / 결선 진출] 팀은 {seasonTeam.season_team.length}팀 입니다.<br>

              총 {seasonTeam.season_team.length} 팀에 대한 [예선/본선/결선]게임에 대해 <br>
              각 팀별 [{seasonTeam.season_team.length}]회의 게임을 생성하시겠습니까?
            </div>
          </div>
        </div>
        <div class="mt-5 sm:mt-6">
          <button
            on:click={ console.log('생성 요청') }
            type="button"
            class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            게임 생성
          </button>
        </div>
      </div>
    </div>
  </div>
</div>