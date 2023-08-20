<script lang="ts">

  import {onMount} from "svelte";
  import {setRoundResult} from "$lib/request/games";

  export let game_id = "";
  export let close: () => void;
  let data;
  onMount(async () => {
    data = await setRoundResult(game_id)
  })


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
                해당 게임 결과를 확정하시겠습니까?
          </div>
        </div>
        <div class="mt-5 sm:mt-6">
          <div class="flex align-default">
          <button
            on:click={ setRoundResult(game_id) }
            type="button"
            class="w-1/2 justify-center rounded-md bg-indigo-600 mx-2 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            네
          </button>
          <button
            on:click={ close }
            type="button"
            class="w-1/2 justify-center rounded-md bg-indigo-600 mx-2 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            아니오
          </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>