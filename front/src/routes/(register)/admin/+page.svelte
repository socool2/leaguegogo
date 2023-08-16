<script lang="ts">
import ChangePasswordModal from "$lib/components/admin/ChangePasswordModal.svelte";

$: isOpenModal = false;

function openModal(open: boolean) {
  isOpenModal = open
}

</script>

<div class="">
  <div class="relative isolate px-6 pt-14 lg:px-8">
    <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
         aria-hidden="true">

    </div>
    <div class="mx-auto max-w-2xl py-8 sm:py-16 lg:py-20 bg-white rounded-xl shadow-lg bg-opacity-50">
      <div class="text-center">
        <h1 class="text-xl font-bold tracking-tight text-stone-900 sm:text-4xl break-keep">리그고고에 오신것을 환영합니다.</h1>
        <h2 class="text-lg p-4 font-bold tracking-tight text-stone-600 sm:text-2xl break-keep">관리자 계정(Admin)으로 로그인
          바랍니다.</h2>
      </div>
      <div class="flex flex-col max-w-md items-center gap-4 mx-auto">
        <div class="w-full">
          <label for="username" class="block text-sm font-medium leading-6 text-gray-900">아이디</label>
          <div class="mt-2">
            <input type="text" name="username" id="username"
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                   placeholder="leaguejoa" aria-describedby="email-description">
          </div>
        </div>
        <div class="w-full">
          <label for="password" class="block text-sm font-medium leading-6 text-gray-900">비밀번호</label>
          <div class="mt-2">
            <input type="password" name="password" id="password"
                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-600 sm:text-sm sm:leading-6 px-2"
                   placeholder="Password" aria-describedby="email-description">
          </div>
        </div>
        <button
          on:click={() =>openModal(true)}
          type="button" class="rounded-full w-full  bg-primary-600 px-3.5 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">로그인</button>
      </div>
    </div>
  </div>
</div>

{#if isOpenModal}
  <ChangePasswordModal isOpenModal={isOpenModal} openModal={openModal} />
{/if}
