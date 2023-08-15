<script lang="ts">
  export let disabled = false;
  export let onClick: (() => void) | undefined = undefined;
</script>

<button type="button"
        disabled={disabled}
        on:click={onClick}
        class="rounded-md bg-primary-600 px-2 py-1 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600 disabled:bg-gray-200 disabled:hover:bg-gray-200 disabled:text-gray-600 disabled:text-gray-400">
  <slot></slot>
</button>