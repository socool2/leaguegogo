<script lang="ts">

  import {onMount} from "svelte";
  import {setLeagues} from "$lib/request/leagues";

  export let leagueInfo
  let data;

  $: openModal = true;

  onMount(async () => {
    data = await setLeagues(leagueInfo)
    let div = document.createElement('div')
    div.setAttribute('class', 'text-center text-gray-700')
    if (data.status === 204){
      div.innerHTML = leagueInfo.league_name + ' 생성이 완료되었습니다!<br/> 이제, 첫 시즌 정보를 등록하겠습니다.'
      let a = document.getElementById('successUrl');
      a.setAttribute('href','/season/register')
    }else{
      div.innerHTML = leagueInfo.league_name + ' 생성에 실패 했습니다!<br/> 입력값을 확인해주세요.'
    }
    document.getElementById('div-content-box').appendChild(div)
  })

</script>

{#if openModal}
  <div class="relative z-20" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div
          class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
          <div id="div-content-box">
          </div>
          <div class="mt-5 sm:mt-6">
            <a id="successUrl">
              <button
              on:click={() => openModal = false}
              type="button"
              class="inline-flex w-full justify-center rounded-md bg-primary-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">
              확인
            </button>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  {/if}
