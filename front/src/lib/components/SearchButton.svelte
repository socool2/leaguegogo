<script lang="ts">
  export let disabled = false;
  export let onClick: (() => void) | undefined = undefined;
</script>

<button type="button"
        disabled={disabled}
        on:click={onClick}
        class="rounded-md bg-white px-2 py-1 text-sm font-semibold text-black shadow-sm hover:bg-primary-400 hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600 disabled:bg-gray-200 disabled:hover:bg-gray-200 disabled:text-gray-600 disabled:text-gray-400">
  <slot></slot>
</button>