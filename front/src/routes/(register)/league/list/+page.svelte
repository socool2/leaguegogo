<script lang="ts">
    import SearchButton from "$lib/components/SearchButton.svelte";
    import LeagueList from "$lib/components/league/LeagueList.svelte";
</script>


<div class="overflow-auto">
  <div class="flex w-full h-full">
    <div class="w-full p-8">
      <!-- Start of Table -->
      <div class="px-4 sm:px-6 lg:px-8">
        <div class="mt-8 flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              리그 <input type="search"> <SearchButton>검색</SearchButton>
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-center w-1 text-sm font-semibold text-gray-900 sm:pl-0">No
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center w-2/3 text-sm font-semibold text-gray-900 break-keep">리그 이름
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-center text-gray-900">리그 기간</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                <LeagueList/>
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
