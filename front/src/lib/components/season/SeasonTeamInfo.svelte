<script lang="ts">

  import {onMount} from "svelte";
  import {getSeasonTeam} from "$lib/request/seasonTeams";

  export let season_id = "";
  export let close: () => void;
  let data;
  onMount(async () => {
    data = await getSeasonTeam(season_id)
  })

  type SeasonTeam = {
    season_team_id: number
    season_id: number
    team_id: string
    reg_user_id: string
    reg_date: Date
    reg_cancel_date: Date | null
    main_advance_yn: string
    playoff_advance_yn: string
    remark: string | null
  }


  const season_team: SeasonTeam[] = [{
      season_team_id: 1,
      season_id: 1,
      team_id: "업라이징",
      reg_user_id: "홍길동",
      reg_date: new Date(),
      reg_cancel_date: null,
      main_advance_yn: "yes",
      playoff_advance_yn: "yes",
      remark: null
    },
    {
      season_team_id: 2,
      season_id: 1,
      team_id: "퓨얼",
      reg_user_id: "OOO",
      reg_date: new Date(),
      reg_cancel_date: null,
      main_advance_yn: "yes",
      playoff_advance_yn: "yes",
      remark: null
    }]

  const seasonTeam = {
    season_id: 1,
    season_name: "1st season",
    season_start_date: new Date(),
    season_end_date: new Date(),
    season_reg_start_date: new Date(),
    season_reg_end_date: new Date(),
    season_team: season_team
  }


</script>


<div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <button
    on:click={close}
    class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"/>
  <div class="fixed inset-0 z-10 overflow-y-auto">

    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

      <div
        class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg lg:max-w-2xl sm:p-6">
        <div>
          <div class="mt-3 text-center sm:mt-5">
            <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">{seasonTeam.season_name}</h3>
            시즌 기간: {seasonTeam.season_start_date.toLocaleDateString("ko")} ~ {seasonTeam.season_end_date.toLocaleDateString("ko")}<br/>
            신청 기간: {seasonTeam.season_reg_start_date.toLocaleDateString("ko")} ~ {seasonTeam.season_reg_end_date.toLocaleDateString("ko")}
            <div class="mt-2">
              <table>
                <thead>
                <tr class="">
                  <th scope="col" class="px-2 py-3.5 text-center w-full text-sm font-semibold text-gray-900">팀명</th>
                  <th scope="col" class="px-2 py-3.5 text-center text-sm font-semibold text-gray-900">신청일</th>
                  <th scope="col" class="px-2 py-3.5 text-center text-sm font-semibold text-gray-900">신청자</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                {#each seasonTeam.season_team as season_team}
                  <tr class="even:bg-gray-50">
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                      {season_team.team_id}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                      {season_team.reg_date.toLocaleDateString("ko")}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                      {season_team.reg_user_id}
                    </td>
                  </tr>
                {/each}
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="mt-5 sm:mt-6">
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