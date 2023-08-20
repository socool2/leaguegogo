<script lang="ts">
  import TableButton from "$lib/components/teams/TableButton.svelte";
  import TdDetail from "$lib/components/TdDetail.svelte";
  import SearchButton from "$lib/components/teams/SearchButton.svelte";
  import SeasonDetail from "$lib/components/season/SeasonDetail.svelte";
  import SeasonTeamInfo from "$lib/components/season/SeasonTeamInfo.svelte";
  import SeasonGameReq from "$lib/components/season/SeasonGameReq.svelte";

  type Season = {
    season_id: number
    league_id: string
    season_name: string
    season_start_date: Date
    season_end_date: Date
    season_desc?: string| null
    season_image_link?: string| null
    season_reg_start_date: Date
    season_reg_end_date: Date
    preli_yn: string
    preli_game_cnt?: number| null
    preli_start_date?: Date| null
    preli_end_date?: Date| null
    preli_status?: string| null
    main_yn: string
    main_game_cnt: number
    main_start_date: Date
    main_end_date: Date
    main_status: string
    playoff_yn: string
    playoff_game_cnt: number
    playoff_start_date: Date
    playoff_end_date: Date
    playoff_status: string
    remark?: string | null
  }

  const sampleSeasons: Season[] = [
    {
      season_id: 1,
      league_id: "1",
      season_name: "1st Season",
      season_start_date: new Date(),
      season_end_date: new Date(),
      season_desc: "2023 1st Season",
      season_image_link: "https://picsum.photos/200/300",
      season_reg_start_date: new Date(),
      season_reg_end_date: new Date(),
      preli_yn: "no",
      preli_game_cnt: 120,
      preli_start_date: new Date(),
      preli_end_date: new Date(),
      preli_status: "complete",
      main_yn: "yes",
      main_game_cnt: 24,
      main_start_date: new Date(),
      main_end_date: new Date(),
      main_status: "Complete",
      playoff_yn: "yes",
      playoff_game_cnt: 5,
      playoff_start_date: new Date(),
      playoff_end_date: new Date(),
      playoff_status: "complete",
      remark: null
    },
    {
      season_id: 2,
      league_id: "2",
      season_name: "2nd Season",
      season_start_date: new Date(),
      season_end_date: new Date(),
      season_desc: "2023 2nd Season",
      season_image_link: "https://picsum.photos/200/300",
      season_reg_start_date: new Date(),
      season_reg_end_date: new Date(),
      preli_yn: "no",
      preli_game_cnt: 120,
      preli_start_date: new Date(),
      preli_end_date: new Date(),
      preli_status: "complete",
      main_yn: "yes",
      main_game_cnt: 24,
      main_start_date: new Date(),
      main_end_date: new Date(),
      main_status: "Complete",
      playoff_yn: "yes",
      playoff_game_cnt: 5,
      playoff_start_date: new Date(),
      playoff_end_date: new Date(),
      playoff_status: "complete",
      remark: null
    }
  ]

  $: detailSeasonId = ""
  $: seasonTeamId = ""
  $: seasonGameId = ""

  const openDetail = (season_id: string) => {
    detailSeasonId = season_id;
  }

  const openSubmit = (season_id: string) => {
    seasonTeamId = season_id
  }

  const openGame = (season_id: string) => {
    seasonGameId = season_id
  }


</script>


<div class="overflow-auto">
  <div class="flex w-full h-full">
    <div class="w-full p-8">
      <!-- Start of Table -->
      <div class="px-4 sm:px-6 lg:px-8">
        <div class="mt-8 flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              시즌 <select class="form-control"><option>1st Season</option><option>2nd Season</option></select> <SearchButton>검색</SearchButton>
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">No
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center w-16 text-sm font-semibold text-gray-900 break-keep">시즌 이름
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">시즌 기간</th>
                  <th scope="col" class="px-3 py-3.5 text-left w-full text-sm font-semibold text-gray-900">시즌 소개글</th>
                  <th scope="col" class="px-3 py-3.5 text-center  text-sm font-semibold text-gray-900">경기 기간</th>
                  <th scope="col" class="px-3 py-3.5 text-center  text-sm font-semibold text-gray-900">진행 현황</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                {#each sampleSeasons as season, i}
                  <tr class="even:bg-gray-50">
                    <td
                      class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0">{i + 1}
                    </td>
                    <td class="whitespace-nowrap w-20 px-3 py-4 text-sm text-gray-500"><TdDetail onClick={() => openDetail(season.season_id)}>{season.season_name}</TdDetail></td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                        {season.season_start_date.toLocaleDateString("ko")} ~ {season.season_end_date.toLocaleDateString("ko")}
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-left">
                      {season.season_desc}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-400 text-center">
                      <div class="flex gap-2">
                        신청: {season.season_reg_start_date.toLocaleDateString("ko")} ~ {season.season_reg_end_date.toLocaleDateString("ko")}<br/>
                        예선: {season.preli_start_date.toLocaleDateString("ko")} ~ {season.preli_end_date.toLocaleDateString("ko")}<br/>
                        본선: {season.main_start_date.toLocaleDateString("ko")} ~ {season.main_end_date.toLocaleDateString("ko")}<br/>
                        결선: {season.playoff_start_date.toLocaleDateString("ko")} ~ {season.playoff_end_date.toLocaleDateString("ko")}
                      </div>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                      <div class="flex gap-2">
                        {season.playoff_status}
                        <TableButton onClick={() => openSubmit(season.season_id)}>신청 현황</TableButton>
                        <TableButton onClick={() => openGame(season.season_id)}>게임 생성</TableButton>
                      </div>
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


{#if detailSeasonId !== ""}
  <SeasonDetail season_id={detailSeasonId} close={() => openDetail("")}/>
{/if}

{#if seasonTeamId !== ""}
  <SeasonTeamInfo season_id={seasonTeamId} close={() => openSubmit("")}/>
{/if}

{#if seasonGameId !== ""}
  <SeasonGameReq season_id={seasonGameId} close={() => openGame("")}/>
{/if}