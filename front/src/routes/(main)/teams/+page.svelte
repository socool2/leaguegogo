<script lang="ts">
  import TableButton from "$lib/components/teams/TableButton.svelte";
  import MemberList from "$lib/components/teams/MemberList.svelte";

  type Team = {
    team_id: string
    team_name: string
    team_creator: string
    introduce_team?: string | null
    team_image_link?: string | null
    team_create_date: Date
    team_close_date?: Date | null
    remark?: string | null
  }

  const sampleTeams: Team[] = [
    {
      team_id: "1",
      team_name: "팀1",
      team_creator: "1",
      introduce_team: "팀1 소개",
      team_image_link: "https://picsum.photos/200/300",
      team_create_date: new Date(),
      team_close_date: new Date(),
      remark: "팀1 비고"
    },
    {
      team_id: "2",
      team_name: "팀2",
      team_creator: "2",
      introduce_team: "팀2 소개",
      team_image_link: "https://picsum.photos/200/300",
      team_create_date: new Date(),
      team_close_date: new Date(),
      remark: "팀2 비고"
    },
    {
      team_id: "3",
      team_name: "팀3",
      team_creator: "3",
      introduce_team: "팀3 소개",
      team_image_link: "https://picsum.photos/200/300",
      team_create_date: new Date(),
      team_close_date: new Date(),
      remark: "팀3 비고"
    },
    {
      team_id: "4",
      team_name: "팀4",
      team_creator: "4",
      introduce_team: "팀4 소개",
      team_image_link: "https://picsum.photos/200/300",
      team_create_date: new Date(),
      team_close_date: new Date(),
      remark: "팀4 비고"
    },
    {
      team_id: "5",
      team_name: "팀5",
      team_creator: "5",
      introduce_team: "팀5 소개",
      team_image_link: "https://picsum.photos/200/300",
      team_create_date: new Date(),
      team_close_date: new Date(),
      remark: "팀5 비고"
    },
    {
      team_id: "6",
      team_name: "팀6",
      team_creator: "6",
      introduce_team: "팀6 소개",
      team_image_link: "https://picsum.photos/200/300",
      team_create_date: new Date(),
      team_close_date: new Date(),
      remark: "팀6 비고"
    },
  ]

  $: detailTeamId = ""

  $: memberTeamId = ""
  const openDetail = (teamId: string) => {
    console.log("teamId", teamId);
  }

  const openTeamMember = (teamId: string) => {
    memberTeamId = teamId;
  }


</script>


<div class="overflow-auto">
  <div class="flex w-full h-full">
    <div class="w-full p-8">
      <!-- Start of Table -->
      <div class="px-4 sm:px-6 lg:px-8">
        <div class="mt-8 flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-left w-16 text-sm font-semibold text-gray-900 break-keep">팀
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">창단일</th>
                  <th scope="col" class="px-3 py-3.5 text-left w-full text-sm font-semibold text-gray-900">소개 글</th>
                  <th scope="col" class="px-3 py-3.5 text-center  text-sm font-semibold text-gray-900">함께하기</th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                {#each sampleTeams as team, i}
                  <tr class="even:bg-gray-50">
                    <td
                      class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0">{i + 1}
                    </td>
                    <td class="whitespace-nowrap w-20 px-3 py-4 text-sm text-gray-500">{team.team_name}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-center">
                      {team.team_create_date.toLocaleDateString("ko")}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 text-left truncate">
                      {team.introduce_team}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                      <div class="flex gap-2">
                        <TableButton onClick={() => openDetail(team.team_id)}>성적 보기</TableButton>
                        <TableButton onClick={() => openTeamMember(team.team_id)}>팀원 보기</TableButton>
                        <TableButton disabled={true}>팀원 신청</TableButton>
                        <TableButton disabled={true}>서포터즈 가입</TableButton>
                      </div>
                    </td>
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
  </div>
</div>

{#if memberTeamId !== ""}
  <MemberList teamId={memberTeamId} close={() => openTeamMember("")}/>

{/if}