<script lang="ts">
  import Ranking from "$lib/components/main/Ranking.svelte";

  type Game = {
    game_id: number;
    season_id: number;
    game_type: string
    game_round: number;
    team1_id: number;
    team2_id: number;
    game_date: Date;
    team1_point: number;
    team1_result: string;
    team2_point: number
    team2_result: string;
    round_status: string;
  }

  const sampleGames: Game[] = [
    {
      game_id: 1,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 1,
      team2_id: 2,
      game_date: new Date("2023-08-15"),
      team1_point: 85,
      team1_result: "Win",
      team2_point: 78,
      team2_result: "Loss",
      round_status: "Completed",
    },
    {
      game_id: 2,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 3,
      team2_id: 4,
      game_date: new Date("2023-08-16"),
      team1_point: 92,
      team1_result: "Win",
      team2_point: 89,
      team2_result: "Loss",
      round_status: "Completed",
    },
    {
      game_id: 3,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 1,
      team2_id: 2,
      game_date: new Date("2023-08-15"),
      team1_point: 85,
      team1_result: "Win",
      team2_point: 78,
      team2_result: "Loss",
      round_status: "Completed",
    },
    {
      game_id: 4,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 1,
      team2_id: 2,
      game_date: new Date("2023-08-16"),
      team1_point: 92,
      team1_result: "Win",
      team2_point: 89,
      team2_result: "Loss",
      round_status: "Completed",
    },
    {
      game_id: 5,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 1,
      team2_id: 2,
      game_date: new Date("2023-08-15"),
      team1_point: 85,
      team1_result: "Win",
      team2_point: 78,
      team2_result: "Loss",
      round_status: "Completed",
    },
    {
      game_id: 6,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 3,
      team2_id: 4,
      game_date: new Date("2023-08-16"),
      team1_point: 92,
      team1_result: "Win",
      team2_point: 89,
      team2_result: "Loss",
      round_status: "Completed",
    },
    {
      game_id: 7,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 1,
      team2_id: 2,
      game_date: new Date("2023-08-15"),
      team1_point: 85,
      team1_result: "Win",
      team2_point: 78,
      team2_result: "Loss",
      round_status: "Completed",
    },
    {
      game_id: 8,
      season_id: 2023,
      game_type: "Regular Season",
      game_round: 1,
      team1_id: 3,
      team2_id: 4,
      game_date: new Date("2023-08-16"),
      team1_point: 92,
      team1_result: "Win",
      team2_point: 89,
      team2_result: "Loss",
      round_status: "Completed",
    }
  ];

</script>


<div class="overflow-auto">
  <div class="flex w-full h-full">
    <div class="lg:w-3/4 p-8">
      <!--  Start of Table  -->
      <div class="px-4 sm:px-6 lg:px-8">

        <div class="mt-8 flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">게임 날짜
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">유형</th>
                  <th scope="col" class="px-3 py-3.5 text-center w-full text-sm font-semibold text-gray-900">게임</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">

                {#each sampleGames as game}
                  <tr class="even:bg-gray-50">
                    <td
                      class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0">{game.game_date.toLocaleDateString("ko")}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{game.game_type}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                      {game.team1_result} {game.team1_id} {game.team2_point}
                      : {game.team2_point} {game.team2_id} {game.team2_result}</td>
                  </tr>
                {/each}
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <!-- End of Table-->
      </div>
    </div>
    <!-- Start of Team Ranks -->
    <div class="lg:w-1/4 p-8">
      <div class="flex flex-col justify-center items-center">
        <Ranking/>
      </div>
    </div>
  </div>
</div>