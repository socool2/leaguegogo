<script lang="ts">
  $: openModal = false;
  let seasonName = '';
</script>
<div class="my-4">
  <div class="relative isolate px-6 pt-14 lg:px-8">
    <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
         aria-hidden="true">

    </div>
    <div class="mx-auto max-w-2xl px-4 py-8 sm:py-16 lg:py-20 bg-white rounded-xl shadow-lg bg-opacity-50">
      <div class="text-center pb-8">
        <h1 class="text-xl font-bold tracking-tight text-neutral-700 sm:text-4xl break-keep"><span
          class="text-primary-500">첫 시즌 정보</span>를 등록해주세요.</h1>
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
            <textarea name="season-introduce" id="season-introduce"
                      maxlength="2000"
                      rows="6"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                      placeholder="시즌 소개에 대해 적어주세요. " aria-describedby="season-information-description"/>
          </div>
        </div>
        <div class="w-full">
          <label for="season-thumbnail" class="block text-sm font-medium leading-6 text-gray-900">대표 이미지</label>
          <div class="mt-2">
            <input type="file" name="season-thumbnail" id="season-thumbnail"
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
              <input type="date" name="season-start-date" id="season-start-date"
                     class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              >
            </div>
          </div>
          <div class="w-full">
            <label for="season-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
              class="text-red-600">*</span> 시즌 종료일</label>
            <div class="mt-2">
              <input type="date" name="season-end-date" id="season-end-date"
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
              <input type="date" name="team-start-date" id="team-start-date"
                     class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              >
            </div>
          </div>
          <div class="w-full">
            <label for="season-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
              class="text-red-600">*</span> 팀 등록 종료일</label>
            <div class="mt-2">
              <input type="date" name="team-end-date" id="team-end-date"
                     class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
              >
            </div>
          </div>
        </div>

        <!--  Start of 게임정보      -->
        <div class="flex justify-center flex-col items-center gap-8 my-4">
          <h2 class="text-xl font-bold tracking-tight text-neutral-700 sm:text-2xl break-keep">게임 정보</h2>
          <div class="flex items-center justify-center gap-4 ">
            <div class="pt-8">
              <input type="checkbox"/>
            </div>
            <div class="w-full">
              <label for="pre-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 예선 시작일</label>
              <div class="mt-2">
                <input type="date" name="pre-start-date" id="pre-start-date"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="pre-end-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 예선 종료일</label>
              <div class="mt-2">
                <input type="date" name="pre-end-date" id="pre-end-date"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="pre-game-count" class="block text-sm font-medium leading-6 text-gray-900">게임 횟수</label>
              <div class="mt-2">
                <input type="number" name="pre-game-count" id="pre-game-count"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
          </div>
          <div class="flex items-center justify-center gap-4 ">
            <div class="pt-8">
              <input type="checkbox"/>
            </div>
            <div class="w-full">
              <label for="main-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 본선 시작일</label>
              <div class="mt-2">
                <input type="date" name="main-start-date" id="main-start-date"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="main-end-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 본선 종료일</label>
              <div class="mt-2">
                <input type="date" name="main-end-date" id="main-end-date"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="main-game-count" class="block text-sm font-medium leading-6 text-gray-900">게임 횟수</label>
              <div class="mt-2">
                <input type="number" name="main-game-count" id="main-game-count"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
          </div>
          <div class="flex items-center justify-center gap-4">
            <div class="pt-8">
              <input type="checkbox"/>
            </div>
            <div class="w-full">
              <label for="final-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 예선 시작일</label>
              <div class="mt-2">
                <input type="date" name="final-start-date" id="final-start-date"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="final-end-date" class="block text-sm font-medium leading-6 text-gray-900"><span
                class="text-red-600">*</span> 예선 종료일</label>
              <div class="mt-2">
                <input type="date" name="final-end-date" id="final-end-date"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
            <div class="w-full">
              <label for="final-game-count" class="block text-sm font-medium leading-6 text-gray-900">게임 횟수</label>
              <div class="mt-2">
                <input type="number" name="final-game-count" id="final-game-count"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                >
              </div>
            </div>
          </div>
          <!--   End of 게임정보   -->
          <div class="flex justify-center items-center">
            <button
              on:click={() => openModal = true}
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

{#if openModal}
  <div class="relative z-20" aria-labelledby="modal-title" role="dialog" aria-modal="true">

    <div
      class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

    <div class="fixed inset-0 z-10 overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div
          class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
          <div class="text-center text-gray-700">
            {seasonName} 생성이 완료되었습니다! <br/>
            리그 화면으로 이동합니다.
          </div>
          <div class="mt-5 sm:mt-6">
            <button
              on:click={() => openModal = false}
              type="button"
              class="inline-flex w-full justify-center rounded-md bg-primary-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">
              확인
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}