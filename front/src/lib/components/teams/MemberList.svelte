<script lang="ts">

  import {onMount} from "svelte";
  import {getTeam} from "$lib/request/teams";

  export let teamId = "";
  export let close: () => void;
  let data;
  onMount(async () => {
    data = await getTeam(teamId)
  })

  type TeamMember = {
    team_member_id: number;
    team_id: string;
    member_id: string;
    team_reg_date: Date;
    team_with_date: Date;
    team_member_grade: number
    remark?: string | null
  }

  type Team = {
    team_id: string;
    team_name: string;
    team_create_date: Date;
    introduce_team: string;
    team_member: TeamMember[];
  }


  const sampleTeamMember: TeamMember[] = [{
    team_id: "1",
    team_member_id: 1,
    member_id: "1",
    team_reg_date: new Date(),
    team_with_date: new Date(),
    team_member_grade: 1
  },
    {
      team_id: "1",
      team_member_id: 1,
      member_id: "1",
      team_reg_date: new Date(),
      team_with_date: new Date(),
      team_member_grade: 1
    },
    {
      team_id: "1",
      team_member_id: 1,
      member_id: "1",
      team_reg_date: new Date(),
      team_with_date: new Date(),
      team_member_grade: 1
    },
    {
      team_id: "1",
      team_member_id: 1,
      member_id: "1",
      team_reg_date: new Date(),
      team_with_date: new Date(),
      team_member_grade: 1
    },]

  const team = {
    team_id: "1",
    team_name: "팀1",
    team_create_date: new Date(),
    introduce_team: "팀1 소개글",
    team_member: sampleTeamMember
  }


</script>


<div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <button
    on:click={close}
    class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"/>
  <div class="fixed inset-0 z-10 overflow-y-auto">

    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

      <div
        class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg lg:max-w-2xl sm:p-6">
        <div>
          <div class="mt-3 text-center sm:mt-5">
            <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">{team.team_id}</h3>
            <div class="mt-2">
              <table>
                <thead>
                <tr class="">
                  <th scope="col" class="px-2 py-3.5 text-center text-sm font-semibold text-gray-900">아이디</th>
                  <th scope="col" class="px-2 py-3.5 text-center text-sm font-semibold text-gray-900">닉네임</th>
                  <th scope="col" class="px-2 py-3.5 text-center w-full text-sm font-semibold text-gray-900">자기 소개</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                {#each team.team_member as member}
                  <tr class="even:bg-gray-50">
                    <td class="whitespace-nowrap w-20 px-3 py-4 text-sm text-gray-500">
                      아이디
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                      닉네임
                      <!--{member.ninckname}-->
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-left truncate">
                      자기소개에요. 자기소개에요. 자기소개에요.
                      <!--{member.description}-->
                    </td>
                  </tr>
                {/each}
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="mt-5 sm:mt-6">
          <button
            on:click={close}
            type="button"
            class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            돌아가기
          </button>
        </div>
      </div>
    </div>
  </div>
</div>