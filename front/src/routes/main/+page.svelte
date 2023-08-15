<script lang="ts">

  type Post = {
    id: number;
    season: string;
    title: string;
    date: Date;
    viewCount: number;

  }

  const samplePosts: Post[] = [
    {
      id: 1,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    },
    {
      id: 2,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    },
    {
      id: 3,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    },
    {
      id: 4,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    },
    {
      id: 5,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    },
    {
      id: 6,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    },
    {
      id: 7,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    },
    {
      id: 8,
      season: '2021-1',
      title: '리그 시작합니다.',
      date: new Date(),
      viewCount: 100,
    }
  ]

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


<div class="overflow-auto">
  <div class="flex w-full h-full">
    <div class="lg:w-3/4 p-8">
      <!-- Start of League Banner   -->
      <div class="relative isolate overflow-hidden bg-gray-900 py-24 sm:py-32 rounded-lg">
        <div class="absolute inset-0 -z-10 h-full w-full object-cover">
          <img
            src="https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            alt="" class="absolute inset-0 -z-10 h-full w-full object-cover">
          <div class="absolute inset-0 -z-10 h-full w-full object-cover bg-black bg-opacity-50"></div>
        </div>
        <div class="hidden sm:absolute sm:-top-10 sm:right-1/2 sm:-z-10 sm:mr-10 sm:block sm:transform-gpu sm:blur-3xl"
             aria-hidden="true">
          <div class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-tr from-[#ff4694] to-[#776fff] opacity-20"
               style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"></div>
        </div>
        <div
          class="absolute -top-52 left-1/2 -z-10 -translate-x-1/2 transform-gpu blur-3xl sm:top-[-28rem] sm:ml-16 sm:translate-x-0 sm:transform-gpu"
          aria-hidden="true">
          <div class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-tr from-[#ff4694] to-[#776fff] opacity-20"
               style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"></div>
        </div>
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
          <div class="mx-auto max-w-2xl lg:mx-0">
            <h2 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">리그 이름은 여기에 나와야지.</h2>
            <p class="mt-6 text-lg leading-8 text-gray-300 font-semibold">추운 겨울에는 따뜻한 커피와 티를 마셔야지요, 다람쥐 헌 쳇바퀴에 타고파. 콩고물과
              우유가 들어간 빙수는 차게
              먹어야 특별한 맛이 잘 표현된다.추운 겨울에는 따뜻한 커피와 티를 마셔야지요, 다람쥐 헌 쳇바퀴에 타고파. 콩고물과 우유가 들어간 빙수는 차게 먹어야 특별한 맛이 잘 표현된다 추운 겨울에는
              따뜻한
              커피와 티를 마셔야지요, 다람쥐 헌 쳇바퀴에 타고파. 콩고물과 우유가 들어간 빙수는 차게 먹어야 특별한 맛이 잘 표현된다 추운 겨울에는 따뜻한 커피와 티를 마셔야지요, 다람쥐 헌 쳇바퀴에
              타고파.
              콩고물과 우유가 들어간 빙수는 차게 먹어야 특별한 맛이 잘 표현된다 추운 겨울에는 따뜻한 커피와 티를 마셔야지요, 다람쥐 헌 쳇바퀴에 타고파. 콩고물과 우유가 들어간 빙수는 차게 먹어야
              특별한
              맛이
              잘 표현된다 추운 겨울에는 따뜻한 커피와 티를 마셔야지요, 다람쥐 헌 쳇바퀴에 타고파. 콩고물과 우유가 들어간 빙수는 차게 먹어야 특별한 맛이 잘 표현된다 추운 겨울에는 따뜻한 커피와 티를
              마셔야지요, 다람쥐 헌 쳇바퀴에 타고파. 콩고물과 우유가 들어간 빙수는 차게 먹어야 특별한 맛이 잘 표현된다 </p>
          </div>
        </div>
      </div>
      <!-- End of League Banner -->
      <div class="flex my-4">
        <div class="w-1/3 h-40 relative isolate overflow-clip rounded-lg">
          <img
            src="https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            alt="" class="absolute inset-0 -z-10 h-full w-full object-cover">
          <div class="absolute inset-0 -z-10 h-full w-full object-cover bg-black bg-opacity-50"></div>
          <div class="flex text-white w-full h-full justify-center items-center">
            <p>
              시즌 이름은 여기에
            </p>
          </div>
        </div>
        <div class="w-2/3 flex justify-center items-center">
          시즌 소개글은 링크인가?
        </div>
      </div>

      <!--  Start of Table  -->
      <div class="px-4 sm:px-6 lg:px-8">
        <div class="sm:flex sm:items-center">
          <div class="flex w-full justify-end items-end">
            <button type="button"
                    class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              글쓰기
            </button>
          </div>
        </div>
        <div class="mt-8 flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">id</th>
                  <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">시즌</th>
                  <th scope="col" class="px-3 py-3.5 text-left w-full text-sm font-semibold text-gray-900">제목</th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">날짜</th>
                  <th scope="col" class="py-3.5 text-right text-sm font-semibold text-gray-900 sm:pr-0">조회</th>
                  <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
                    <span class="sr-only">Edit</span>
                  </th>
                </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">

                {#each samplePosts as post}
                  <tr>
                    <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-0">{post.id}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{post.season}</td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"><a href="/">{post.title}</a></td>
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{post.date.toLocaleDateString("ko")}</td>
                    <td
                      class="whitespace-nowrap px-3 py-4 text-left text-sm text-gray-500 sm:pr-0">{post.viewCount}</td>

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
        <div class="overflow-clip">
          <table class="min-w-full divide-gray-300 divide-y">
            <thead class="">
            <tr class="block py-4">
              <th class="w-8 pl-0 text-left font-semibold">순위</th>
              <th class="px-2 text-left w-20 font-semibold">팀</th>
              <th class="px-2 w-40 text-right font-semibold">성적</th>
            </tr>
            </thead>

            <tbody class="block h-60 max-h-60 overflow-y-auto overflow-x-hidden">
            {#each sampleTeams as team, i}
              <tr class="flex ">
                <td class="w-8 pl-0 py-4 text-left">{i + 1}</td>
                <td class="w-20 px-2 py-4 text-left">{team.name}</td>
                <td class="w-40 px-2 py-4 text-right">{team.win}승 {team.draw}무 {team.lose}패</td>
              </tr>
            {/each}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>