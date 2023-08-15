<script lang="ts">
  type Team = {
    id: number;
    name: string;
    logo: string;
    win: number;
    lose: number;
    draw: number;
    point: number;
    rank: number;
  }

  const sampleTeams: Team[] = [
    {
      id: 1,
      name: '팀1',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 1,
    },
    {
      id: 2,
      name: '팀2',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 2,
    },
    {
      id: 3,
      name: '팀3',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 3,
    },
    {
      id: 4,
      name: '팀4',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 4,
    },
    {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    },
    {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    }, {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    }, {
      id: 1,
      name: '팀1',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 1,
    },
    {
      id: 2,
      name: '팀2',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 2,
    },
    {
      id: 3,
      name: '팀3',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 3,
    },
    {
      id: 4,
      name: '팀4',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 4,
    },
    {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    },
    {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    }, {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    }, {
      id: 1,
      name: '팀1',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 1,
    },
    {
      id: 2,
      name: '팀2',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 2,
    },
    {
      id: 3,
      name: '팀3',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 3,
    },
    {
      id: 4,
      name: '팀4',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 4,
    },
    {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    },
    {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    }, {
      id: 5,
      name: '팀5',
      logo: 'https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      win: 1,
      lose: 1,
      draw: 1,
      point: 1,
      rank: 5,
    },
  ]

</script>
<div class="overflow-clip">
  <table class="min-w-full divide-gray-300 divide-y">
    <thead class="">
    <tr class="block py-4">
      <th class="w-8 pl-0 text-left font-semibold">순위</th>
      <th class="px-2 text-left w-20 font-semibold">팀</th>
      <th class="px-2 w-40 text-right font-semibold">성적</th>
    </tr>
    </thead>

    <tbody class="block h-[40rem] overflow-y-auto overflow-x-hidden">
    {#each sampleTeams as team, i}
      <tr class="flex even:bg-gray-50">
        <td class="w-8 pl-0 py-4 text-left">{i + 1}</td>
        <td class="w-20 px-2 py-4 text-left">{team.name}</td>
        <td class="w-40 px-2 py-4 text-right">{team.win}승 {team.draw}무 {team.lose}패</td>
      </tr>
    {/each}
    </tbody>
  </table>
</div>