<script lang="ts">

  import {onMount} from "svelte";
  import {getSeasons} from "$lib/request/seasons";

  export let season_id = "";
  export let close: () => void;
  let data;
  onMount(async () => {
    data = await getSeasons(season_id)
  })
  type Season = {
    season_id: string
    league_id: string
    season_name: string
    season_start_date: Date
    season_end_date: Date
    season_desc?: string| null
    season_image_link?: string| null
    season_reg_start_date: Date
    season_reg_end_date: Date
    preli_yn: string
    preli_game_cnt?: string| null
    preli_start_date?: Date| null
    preli_end_date?: Date| null
    preli_status?: string| null
    main_yn: string
    main_game_cnt: string
    main_start_date: Date
    main_end_date: Date
    main_status: string
    playoff_yn: string
    playoff_game_cnt: string
    playoff_start_date: Date
    playoff_end_date: Date
    playoff_status: string
    remark?: string | null
  }

  const season = {
      season_id: "1",
      league_id: "1",
      season_name: "1st Season",
      season_start_date: new Date(),
      season_end_date: new Date(),
      season_desc: "2023 1st Season",
      season_image_link: "https://picsum.photos/200/300",
      season_reg_start_date: new Date(),
      season_reg_end_date: new Date(),
      preli_yn: "no",
      preli_game_cnt: "120",
      preli_start_date: new Date(),
      preli_end_date: new Date(),
      preli_status: "complete",
      main_yn: "yes",
      main_game_cnt: "24",
      main_start_date: new Date(),
      main_end_date: new Date(),
      main_status: "Complete",
      playoff_yn: "yes",
      playoff_game_cnt: "5",
      playoff_start_date: new Date(),
      playoff_end_date: new Date(),
      playoff_status: "complete",
      remark: null
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
            <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">시즌 상세 정보</h3>
            <div class="mt-2">
              {season.season_image_link} {season.season_name}<br/>
              시즌 기간: {season.season_start_date.toLocaleDateString("ko")} ~ {season.season_end_date.toLocaleDateString("ko")}<br/>
              시즌 소개: {season.season_desc}<br/>
              신청 기간: {season.season_reg_start_date.toLocaleDateString("ko")} ~ {season.season_reg_end_date.toLocaleDateString("ko")}<br/>
              예선 기간: {season.preli_start_date.toLocaleDateString("ko")} ~ {season.preli_end_date.toLocaleDateString("ko")}<br/>
              본선 기간: {season.main_start_date.toLocaleDateString("ko")} ~ {season.main_end_date.toLocaleDateString("ko")}<br/>
              결선 기간: {season.playoff_start_date.toLocaleDateString("ko")} ~ {season.playoff_end_date.toLocaleDateString("ko")}<br/>
              시즌 비고: {season.remark}<br/>
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