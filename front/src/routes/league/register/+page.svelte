<script>
  $: openModal = false;
  $: leagueName = '';
</script>
<div class="">
  <div class="relative isolate px-6 pt-14 lg:px-8">
    <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
         aria-hidden="true">

    </div>
    <div class="mx-auto max-w-2xl px-4 py-8 sm:py-16 lg:py-20 bg-white rounded-xl shadow-lg bg-opacity-50">
      <div class="text-center pb-8">
        <h1 class="text-xl font-bold tracking-tight text-neutral-700 sm:text-4xl break-keep"><span class="text-primary-500">첫 리그 정보</span>를 등록해주세요.</h1>
      </div>
      <div class="flex flex-col max-w-md items-center gap-4 mx-auto">
        <div class="w-full">
          <label for="league-name" class="block text-sm font-medium leading-6 text-gray-900"><span class="text-red-600">*</span> 리그 제목</label>
          <div class="mt-2">
            <input
              bind:value={leagueName}
              type="text" name="league-name" id="league-name"
                   maxlength="60"
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                   placeholder="리그의 이름을 적어주세요 ex)한국 스플래툰 연합 리그" aria-describedby="league-description">
          </div>
        </div>
        <div class="w-full">
          <label for="league-introduce" class="block text-sm font-medium leading-6 text-gray-900"><span class="text-red-600">*</span> 리그 소개</label>
          <div class="mt-2">
            <textarea name="league-introduce" id="league-introduce"
                      maxlength="2000"
                      rows="6"
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                   placeholder="리그 소개에 대해 적어주세요. " aria-describedby="league-information-description" />
          </div>
        </div>
        <div class="w-full">
          <label for="league-thumbnail" class="block text-sm font-medium leading-6 text-gray-900"><span class="text-red-600">*</span> 대표 이미지</label>
          <div class="mt-2">
            <input type="file" name="league-thumbnail" id="league-thumbnail"
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                   placeholder="리그의 이름을 적어주세요 ex)한국 스플래툰 연합 리그" aria-describedby="league-description">
          </div>
          <p class="text-gray-600 pt-1 text-sm">
            이미지는 1MB 이하의 jpg, png, gif 파일만 가능합니다.
          </p>
        </div>
        <div class="w-full">
          <label for="league-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span class="text-red-600">*</span> 리그 시작일</label>
          <div class="mt-2">
            <input type="date" name="league-name" id="league-start-date"
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                   >
          </div>
        </div>
        <div class="w-full">
          <label for="league-start-date" class="block text-sm font-medium leading-6 text-gray-900"><span class="text-red-600">*</span> 리그 종료일</label>
          <div class="mt-2">
            <input type="date" name="league-name" id="league-end-date"
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
            >
          </div>
        </div>
        <button
          on:click={() => openModal = true}
          type="button" class="rounded-lg w-full  bg-primary-600 px-3.5 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">리그 만들기</button>
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
            {leagueName} 생성이 완료되었습니다! <br/>
            이제, 첫 시즌 정보를 등록하겠습니다.
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