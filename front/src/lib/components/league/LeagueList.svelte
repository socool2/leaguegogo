<script lang="ts">

  import {onMount} from "svelte";
  import {getLeagues} from "$lib/request/leagues";
  import TdDetail from "$lib/components/TdDetail.svelte";
  import LeagueDetail from "$lib/components/league/LeagueDetail.svelte";

    type League = {
      league_id: number
      league_name: string
      league_start_date: Date
      league_end_date: Date
    }

  $: openModal = true;
  export let data;
  export let leagues:League[] = [];
  onMount(async () => {
    data = await getLeagues()
    leagues = data['league_list']

  })

  $: detailLeagueId = ''

  const openDetail = (league_id) => {
    detailLeagueId = league_id;
  }

</script>

{#if detailLeagueId!==""}
    <LeagueDetail league_id={detailLeagueId} close={() => openDetail("")}/>
{/if}

{#each leagues as league}
  <tr class="even:bg-gray-50">
    <td
      class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0 text-center">{league.league_id}
    </td>
    <td class="whitespace-nowrap w-20 px-3 py-4 text-center text-sm text-gray-500">
      <TdDetail onClick={() => openDetail(league.league_id)}>{league.league_name}</TdDetail>
    </td>
    <td class="whitespace-nowrap px-3 py-4 text-center text-sm text-gray-400">
      <div class="gap-2">
        {new Date(league.league_start_date).toLocaleDateString("ko")} ~ {new Date(league.league_end_date).toLocaleDateString("ko")}
      </div>
    </td>
  </tr>
{/each}