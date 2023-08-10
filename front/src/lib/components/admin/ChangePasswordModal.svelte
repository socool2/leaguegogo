<script lang="ts">
  export let isOpenModal: boolean;
  export let openModal: (open: boolean) => void;
  $: isConfirmMessage = false;

  const openConfirmMessage = (open: boolean) => {
    isConfirmMessage = open;
  }


</script>

{#if isOpenModal}
  <div
    class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">

    <div
      class="fixed z-10 inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

    <div class="fixed inset-0 z-10 overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div
          class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
          <div class="flex flex-col max-w-md items-center gap-4 mx-auto">
            <div class="w-full">
              <label for="current-password" class="block text-sm font-medium leading-6 text-gray-900">비밀번호</label>
              <div class="mt-2">
                <input type="password" name="current-password" id="current-password"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 px-2"
                       placeholder="***********" aria-describedby="email-description">
              </div>
            </div>
            <div class="w-full">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">비밀번호</label>
              <div class="mt-2">
                <input type="password" name="password" id="password"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 px-2"
                       placeholder="***********" aria-describedby="email-description">
              </div>
            </div>
            <div class="w-full">
              <label for="confirm-password" class="block text-sm font-medium leading-6 text-gray-900">비밀번호 확인</label>
              <div class="mt-2">
                <input type="password" name="confirm-password" id="confirm-password"
                       class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 px-2"
                       placeholder="***********" aria-describedby="email-description">
              </div>
            </div>
          </div>
          <div class="flex gap-2 mt-5 sm:mt-6">
            <button
              on:click={() => openModal(false)}
              type="button"
              class="mt-3 inline-flex w-1/3 justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:col-start-1 sm:mt-0">
              취소
            </button>

            <button
              on:click={() => openConfirmMessage(true)}
              type="button"
              class="inline-flex w-2/3 justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              변경 완료
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  {#if isConfirmMessage}
    <div class="relative z-20" aria-labelledby="modal-title" role="dialog" aria-modal="true">

      <div
        class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <div
            class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
            <div class="text-center text-gray-700">
              비밀번호가 정상적으로 변경되었습니다. <br/>
              이제, 리그 정보를 등록하겠습니다.
            </div>
            <div class="mt-5 sm:mt-6">
              <button
                on:click={() => openConfirmMessage(false)}
                type="button"
                      class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                확인
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  {/if}
{/if}