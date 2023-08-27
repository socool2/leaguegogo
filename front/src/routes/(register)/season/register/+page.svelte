<script lang="ts">
  import {selectLeagueName} from "$lib/store.ts";
  import SaveSeason from "$lib/components/season/SaveSeason.svelte";

  let data = $selectLeagueName

  $: openModal = false;
  let seasonName = '';
  let seasonIntroduce = '';
  let seasonImgLink = '';
  let seasonStartDate = '';
  let seasonEndDate = '';
  let teamStartDate = '';
  let teamEndDate = '';
  let preStartDate = '';
  let preEndDate = '';
  let preRound = '';
  let mainStartDate = '';
  let mainEndDate = '';
  let mainRound = '';
  let finalStartDate = '';
  let finalEndDate = '';
  let finalRound = '';
  let preYn = '';
  let mainYn = '';
  let finalYn = '';

  type Season = {
    league_name: string
    season_name: string
    season_start_date: Date| string
    season_end_date: Date| string
    season_desc?: string| null
    season_image_link?: string| null
    season_reg_start_date: Date| string
    season_reg_end_date: Date| string
    preli_game_cnt?: number| string | null
    preli_start_date?: Date| string | null
    preli_end_date?: Date| string | null
    main_game_cnt: number| string | null
    main_start_date: Date| string | null
    main_end_date: Date| string | null
    playoff_game_cnt: number| string | null
    playoff_start_date: Date| string | null
    playoff_end_date: Date| string | null
    preli_yn: string
    main_yn: string
    playoff_yn: string
  }

  let status = ''
  let seasonInfo:Season;

  const reqSaveSeason = () => {
    seasonInfo = {
      league_name: data,
      season_name : seasonName,
      season_start_date : seasonStartDate,
      season_end_date : seasonEndDate,
      season_desc : seasonIntroduce,
      season_image_link : seasonImgLink,
      season_reg_start_date : teamStartDate,
      season_reg_end_date : teamEndDate,
      preli_game_cnt : preRound,
      preli_start_date : preStartDate,
      preli_end_date :preEndDate,
      main_game_cnt : mainRound,
      main_start_date : mainStartDate,
      main_end_date : mainEndDate,
      playoff_game_cnt : finalRound,
      playoff_start_date : finalStartDate,
      playoff_end_date : finalEndDate,
      main_yn: mainYn,
      playoff_yn: finalYn,
      preli_yn: preYn
    }

    status = '1'
  }


</script>
<div class="my-4">
  <div class="relative isolate px-6 pt-14 lg:px-8">
    <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
         aria-hidden="true">

    </div>
    <div class="mx-auto max-w-2xl px-4 py-8 sm:py-16 lg:py-20 bg-white rounded-xl shadow-lg bg-opacity-50">
      <div class="text-center pb-8">
        <h1 class="text-xl font-bold tracking-tight text-neutral-700 sm:text-4xl break-keep"><span
          class="text-primary-500">시즌 정보</span>를 등록해주세요.</h1>
      </div>
      <div class="flex flex-col max-w-md items-center gap-4 mx-auto">
        <div class="w-full">
          <label for="season-name" class="block text-sm font-medium leading-6 text-gray-900"><span class="text-red-600">*</span>시즌
            제목</label>
          <div class="mt-2">
            <input
              bind:value={seasonName}
              type="text" name="season-name" id="season-name"
              maxlength="60"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              placeholder="시즌의 이름을 적어주세요 ex)가을 시즌" aria-describedby="season-description">
          </div>
        </div>
        <div class="w-full">
          <label for="season-introduce" class="block text-sm font-medium leading-6 text-gray-900"><span
            class="text-red-600">*</span>시즌 소개</label>
          <div class="mt-2">
            <textarea bind:value={seasonIntroduce}
                      name="season-introduce" id="season-introduce"
                      maxlength="2000"
                      rows="6"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                      placeholder="시즌 소개에 대해 적어주세요. " aria-describedby="season-information-description"/>
          </div>
        </div>
        <div class="w-full">
          <label for="season-thumbnail" class="block text-sm font-medium leading-6 text-gray-900">대표 이미지</label>
          <div class="mt-2">
            <input type="file" name="season-thumbnail" id="season-thumbnail" bind:value={seasonImgLink}
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                   placeholder="시즌의 이름을 적어주세요 ex)2023 가을 시즌" aria-describedby="season-description">
          </div>
          <p class="text-gray-600 pt-1 text-sm">
            이미지는 1MB 이하의 jpg, png, gif 파일만 가능합니다.
          </p>
        </div>
        <div class="w-full flex justify-between gap-4">
          <div class="w-full">
            <label for="season-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
              class="text-red-600">*</span> 시즌 시작일</label>
            <div class="mt-2">
              <input type="date" name="season-start-date" id="season-start-date" bind:value={seasonStartDate}
                     class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              >
            </div>
          </div>
          <div class="w-full">
            <label for="season-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
              class="text-red-600">*</span> 시즌 종료일</label>
            <div class="mt-2">
              <input type="date" name="season-end-date" id="season-end-date" bind:value={seasonEndDate}
                     class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              >
            </div>
          </div>
        </div>
        <div class="w-full flex justify-between gap-4">
          <div class="w-full">
            <label for="season-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
              class="text-red-600">*</span> 팀 등록 시작일</label>
            <div class="mt-2">
              <input type="date" name="team-start-date" id="team-start-date" bind:value={teamStartDate}
                     class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              >
            </div>
          </div>
          <div class="w-full">
            <label for="season-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
              class="text-red-600">*</span> 팀 등록 종료일</label>
            <div class="mt-2">
              <input type="date" name="team-end-date" id="team-end-date" bind:value={teamEndDate}
                     class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              >
            </div>
          </div>
        </div>

        <!-- Start of 게임정보 -->
        <div class="flex justify-center flex-col items-center gap-8 my-4">
          <h2 class="text-xl font-bold tracking-tight text-neutral-700 sm:text-2xl break-keep">게임 정보</h2>
          <div class="flex items-center justify-center gap-4 ">
            <div class="pt-8">
              <input type="checkbox" bind:value={preYn}/>
            </div>
            <div class="w-full">
              <label for="pre-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 예선 시작일</label>
              <div class="mt-2">
                <input type="date" name="pre-start-date" id="pre-start-date" bind:value={preStartDate}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="pre-end-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 예선 종료일</label>
              <div class="mt-2">
                <input type="date" name="pre-end-date" id="pre-end-date" bind:value={preEndDate}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="pre-game-count" class="block text-sm font-medium leading-6 text-gray-900">게임 횟수</label>
              <div class="mt-2">
                <input type="number" name="pre-game-count" id="pre-game-count" bind:value={preRound}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
          </div>
          <div class="flex items-center justify-center gap-4 ">
            <div class="pt-8">
              <input type="checkbox" bind:value={mainYn}/>
            </div>
            <div class="w-full">
              <label for="main-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 본선 시작일</label>
              <div class="mt-2">
                <input type="date" name="main-start-date" id="main-start-date" bind:value={mainStartDate}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="main-end-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 본선 종료일</label>
              <div class="mt-2">
                <input type="date" name="main-end-date" id="main-end-date" bind:value={mainEndDate}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="main-game-count" class="block text-sm font-medium leading-6 text-gray-900">게임 횟수</label>
              <div class="mt-2">
                <input type="number" name="main-game-count" id="main-game-count" bind:value={mainRound}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
          </div>
          <div class="flex items-center justify-center gap-4">
            <div class="pt-8">
              <input type="checkbox" bind:value={finalYn}/>
            </div>
            <div class="w-full">
              <label for="final-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 결선 시작일</label>
              <div class="mt-2">
                <input type="date" name="final-start-date" id="final-start-date" bind:value={finalStartDate}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="final-end-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 결선 종료일</label>
              <div class="mt-2">
                <input type="date" name="final-end-date" id="final-end-date" bind:value={finalEndDate}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="final-game-count" class="block text-sm font-medium leading-6 text-gray-900">게임 횟수</label>
              <div class="mt-2">
                <input type="number" name="final-game-count" id="final-game-count" bind:value={finalRound}
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
          </div>
          <!-- End of 게임정보 -->
          <div class="flex justify-center items-center">
            <button
              on:click={() => openModal = reqSaveSeason()}
              type="button"
              class="rounded-lg w-full  bg-primary-600 px-3.5 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">
              시즌 만들기
            </button>
          </div>

        </div>
      </div>
    </div>
  </div>
</div>

{#if status === '1'}
  <SaveSeason {seasonInfo}/>
{/if}