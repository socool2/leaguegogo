<script lang="ts">
  export let onClick: (() => void) | undefined = undefined;
</script>

<td
    on:click={onClick}
    class="font-bold">
  <slot></slot>
</td>