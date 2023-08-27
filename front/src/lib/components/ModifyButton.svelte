<script lang="ts">
  export let disabled = false;
  export let onClick: (() => void) | undefined = undefined;
</script>

<button type="button"
        disabled={disabled}
        on:click={onClick}
        class="inline-flex w-full justify-center rounded-md bg-yellow-300 px-3 py-2 text-sm font-semibold text-black shadow-sm hover:bg-yellow-600 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-yellow-600">
  <slot></slot>
</button>