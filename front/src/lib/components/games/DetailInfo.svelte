<script lang="ts">

  import {onMount} from "svelte";
  import {getGameRound} from "$lib/request/games";
  export let game_id = "";
  export let close: () => void;
  let data;
  onMount(async () => {
    data = await getGameRound(game_id)
  })

  type Game = {
      season_name: string
      game_type: string
      game_round: number
      round_status: string
      team1_id: string
      team1_point: number
      team2_id: string
      team2_point: number
      game_member: GameMember[]
  }

  type GameMember = {
    game_id : string
    team_id : string
    member_id : string
  }


  const sampleGameMember: GameMember[] = [
      {
        game_id : "1",
        team_id : "업라이징",
        member_id : "홍길동"
      },
      {
        game_id : "1",
        team_id : "업라이징",
        member_id : "김민수"
      },
      {
        game_id : "1",
        team_id : "퓨얼",
        member_id : "홍영희"
      },
      {
        game_id : "1",
        team_id : "퓨얼",
        member_id : "홍영화"
      }
  ]
  
  const sampleGameRound: Game =
      {
          season_name: "1st Season",
          game_type: "본선",
          game_round: 3,
          round_status: "진행중",
          team1_id: "업라이징",
          team1_point: 234,
          team2_id: "퓨얼",
          team2_point: 253,
          game_member: sampleGameMember
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
            <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">게임 상세 진행 현황</h3>
              시즌: {sampleGameRound.season_name}<br/>
              유형: {sampleGameRound.game_type}<br/>
              회차: {sampleGameRound.game_round} <br/>
              상태: {sampleGameRound.round_status}<br/>
              <br/>
              <table class="divide-y divide-gray-200 w-full">
                <thead>
                <tr class="">
                  <th scope="col" class="px-2 w-1/2 py-3.5 text-center text-sm font-semibold text-gray-900 bg-blue-200">{sampleGameRound.team1_id}({sampleGameRound.team1_point})</th>
                  <th scope="col" class="px-2 w-1/2 py-3.5 text-center text-sm font-semibold text-gray-900 bg-blue-200">{sampleGameRound.team2_id}({sampleGameRound.team2_point})</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                <tr class="even:bg-gray-50">
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                    {#each sampleGameRound.game_member as member}
                        {#if sampleGameRound.team1_id === member.team_id}
                            {member.member_id}<br/>
                        {/if}
                    {/each}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                    {#each sampleGameRound.game_member as member}
                        {#if sampleGameRound.team2_id === member.team_id}
                            {member.member_id}<br/>
                        {/if}
                    {/each}
                    </td>
                </tr>
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
