<script lang="ts">
  import { page } from '$app/stores';

  type Menu = {
    name: string
    href: string
    children?: Menu[]
  }
  const centerMenu: Menu[] = [
    {
      name: '초기화면',
      href: '/main'
    },
    {
      name: '경기현황',
      href: '/match'
    },
    {
      name: '팀 목록',
      href: '/teams'
    },
    {
      name: '시즌 게시판',
      href: '/'
    },
    {
      name: '리그 관리',
      href: '/'
    },

  ]

  const endMenu = [
    {
      name: '마이페이지',
      href: '/'
    },
    {
      name: '로그아웃',
      href: '/'
    },
    {
      name: '도움말',
      href: '/'
    },
  ]

</script>

<header class="bg-white border-b border-2 border-gray-300">
  <nav class="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global">
    <div class="flex lg:flex-1">
      로고 자리
    </div>
    <div class="flex lg:hidden">
      <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700">
        <span class="sr-only">Open main menu</span>
        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
             aria-hidden="true">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
        </svg>
      </button>
    </div>
    <div class="hidden lg:flex lg:gap-x-12 ">
      {#each centerMenu as menu}
        <a href="{menu.href}"
           class:text-gray-900={$page.url.pathname === menu.href}
           class="flex text-sm font-semibold leading-6 text-gray-500 text-center hover:text-gray-900">{menu.name}</a>
      {/each}
    </div>
    <div class="hidden lg:flex lg:flex-1 lg:justify-end lg:gap-x-8">
      {#each endMenu as menu}
        <a href="{menu.href}"
           class:text-gray-900={$page.url.pathname === menu.href}
           class="text-sm font-semibold leading-6 text-gray-500 hover:text-gray-900">{menu.name}</a>
      {/each}
    </div>
  </nav>
  <!-- Mobile menu, show/hide based on menu open state. -->
  <div class="lg:hidden" role="dialog" aria-modal="true">
    <!-- Background backdrop, show/hide based on slide-over state. -->
    <div class="fixed inset-0 z-10"></div>
    <div
      class="fixed inset-y-0 right-0 z-10 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
      <div class="flex items-center justify-between">
        <a href="/" class="-m-1.5 p-1.5">
          <span class="sr-only">Your Company</span>
          <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="">
        </a>
        <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700">
          <span class="sr-only">Close menu</span>
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
               aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
      <div class="mt-6 flow-root">
        <div class="-my-6 divide-y divide-gray-500/10">
          <div class="space-y-2 py-6">
            {#each centerMenu as menu}
              <a href="{menu.href}"
                 class:text-gray-900={$page.url.pathname === menu.href}
                 class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-500 hover:bg-gray-50">{menu.name}</a>
              {/each}

          </div>
          <div class="py-6">
            {#each endMenu as menu}
              <a href="{menu.href}"
                 class:text-gray-900={$page.url.pathname === menu.href}
                 class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-500 hover:bg-gray-50">{menu.name}</a>
              {/each}

          </div>
        </div>
      </div>
    </div>
  </div>
</header>