<script lang="ts">
  import TableButton from "$lib/components/teams/TableButton.svelte";
  import TdDetail from "$lib/components/TdDetail.svelte";
  import SearchButton from "$lib/components/SearchButton.svelte";
  import SaveResultReq from "$lib/components/games/SaveResultReq.svelte";
  import SaveEnterMain from "$lib/components/games/SaveEnterMain.svelte";
  import DetailInfo from "$lib/components/games/DetailInfo.svelte";

  type Game = {
    game_id: string
    season_id: number
    game_type: string
    game_round: number
    team1_id: string
    team2_id: string
    game_date: Date
    team1_point: number | null
    team1_result: string | null
    team2_point: number | null
    team2_result: string | null
    round_status: string | null
  }

  type Team = {
    id: number
    name: string
    logo: string
    point: number
    rank: number
    status: string
  }

  const sampleGame: Game[] = [
    {
      game_id: "1",
      season_id: 1,
      game_type: "결선",
      game_round: 3,
      team1_id: "업라이징",
      team2_id: "퓨얼",
      game_date: new Date(),
      team1_point: 245,
      team1_result: "승리",
      team2_point: 234,
      team2_result: "패배",
      round_status: "종료"
    },
    {
      game_id: "2",
      season_id: 1,
      game_type: "결선",
      game_round: 3,
      team1_id: "업라이징",
      team2_id: "스핏파이어",
      game_date: new Date(),
      team1_point: null,
      team1_result: null,
      team2_point: null,
      team2_result: null,
      round_status: "진행 중"
    },
    {
      game_id: "3",
      season_id: 1,
      game_type: "결선",
      game_round: 3,
      team1_id: "퓨얼",
      team2_id: "스핏파이어",
      game_date: new Date(),
      team1_point: 245,
      team1_result: "승리",
      team2_point: 223,
      team2_result: "패배",
      round_status: "확정 대기 중"
    }
  ]

  const sampleTeam: Team[] = [
    {
      id: 1,
      name: '퓨얼',
      logo: 'logo1',
      point: 3,
      rank: 1,
      status: '본선진출확정'
    },
    {
      id: 2,
      name: '업스트림',
      logo: 'logo2',
      point: 2,
      rank: 2,
      status: '본선진출대기'
    },
    {
      id: 3,
      name: '스핏파이어',
      logo: 'logo3',
      rank: 3,
      point: 1,
      status: '본선진출실패'
    }
  ]

  $: saveResult = ""
  $: mainTeamId = ""
  $: gameRoundId = ""

  const resultSubmit = (game_id: string) => {
    saveResult = game_id;
  }

  const submitMain = (team_id: string) => {
    mainTeamId = team_id
  }

  const getRoundDetail = (game_id: string) => {
    gameRoundId = game_id
  }

</script>

<div class="overflow-auto">
  <div class="flex w-full h-full">
    <div class="lg:w-3/5 p-8">
      <!-- Start of Table -->
      <div class="px-4 sm:px-6 lg:px-8">
        <div class="mt-8 flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              시즌 <select class="form-control"><option>1st Season</option><option>2nd Season</option></select>
              유형 <select class="form-control"><option>예선</option><option>본선</option><option>결선</option></select>
              팀 <select class="form-control"><option>업라이징</option><option>퓨얼</option><option>스핏파이어</option></select>
              <SearchButton>검색</SearchButton>
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0 text-center">No
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center w-16 text-sm font-semibold text-gray-900 break-keep">날짜
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">유형</th>
                  <th scope="col" class="px-3 py-3.5 text-center  text-sm font-semibold text-gray-900">회차</th>
                  <th scope="col" class="px-3 py-3.5 text-center w-1/2 text-sm font-semibold text-gray-900">진행 현황</th>
                  <th scope="col" class="px-3 py-3.5 text-center  text-sm font-semibold text-gray-900">상태</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                {#each sampleGame as game, i}
                  <tr class="even:bg-gray-50">
                    <td
                      class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0 text-center">{i + 1}
                    </td>
                    <td class="whitespace-nowrap w-20 px-3 py-4 text-sm text-gray-500">{game.game_date.toLocaleDateString("ko")}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">{game.game_type}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">{game.game_round}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-800 text-center">
                      <TdDetail onClick={()=>getRoundDetail(game.game_id)}>{game.team1_id} vs {game.team2_id}</TdDetail></td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                      {#if game.round_status === '확정 대기 중'}
                        <TableButton onClick={() => resultSubmit(game.game_id)}>확정</TableButton>
                      {:else}
                        {game.round_status}
                      {/if}
                    </td>
                  </tr>
                {/each}
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <!-- End of Table-->
      </div>
    </div>
    <div class="lg:w-2/5 p-8">
        <!-- Start of Table -->
      <div class="px-4 sm:px-6 lg:px-8">
        <div class="mt-8 flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              [예선/본선/결선] 팀순위
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">순위
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900 break-keep">팀명
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">총점</th>
                  <th scope="col" class="px-3 py-3.5 text-center  text-sm font-semibold text-gray-900">상태</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                {#each sampleTeam as team}
                  <tr class="even:bg-gray-50">
                    <td
                      class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0 text-center">{team.rank}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">{team.name}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">{team.point}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-400 text-center">
                      {#if team.status === '본선진출대기'}
                        <TableButton onClick={() => submitMain(team.id)}>본선진출</TableButton>
                      {:else}
                        {team.status}
                      {/if}
                    </td>
                  </tr>
                {/each}
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <!-- End of Table-->
    </div>
  </div>
</div>
</div>

{#if saveResult !== ""}
  <SaveResultReq game_id={saveResult} close={() => resultSubmit("")}/>
{/if}

{#if mainTeamId !== ""}
  <SaveEnterMain team_id={mainTeamId} close={() => submitMain("")}/>
{/if}

{#if gameRoundId !== ""}
  <DetailInfo game_id={gameRoundId} close={() => getRoundDetail("")}/>
{/if}