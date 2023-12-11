<template>
    <div class="
        px-3
        py-1
        w-min
        text-sm
        font-semibold
        bg-warm-gray-200 bg-opacity-50
        dark:bg-dark-700
        text-warm-gray-600
        dark:text-light-900
        rounded-md
        mr-2
      ">
        <!-- <slot></slot> -->
        <a :href="`https://github.com/${author}`" rel="noreferrer" target="_blank">
            {{ author }}
        </a>
    </div>
</template>
<script lang="ts">
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
    props: {
        author: {
            type: String,
            required: true,
        },
    },
})
</script>
