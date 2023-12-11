<template>
  <div
    class="
      relative
      bg-white
      dark:bg-dark-400
      shadow-md shadow-warm-gray-600
      transition
      p-4
      h-full
      rounded-md
      flex flex-col
      justify-between
      hover:shadow-lg
    "
  >
    <div class="flex flex-col">
      <h1 class="text-transparent text-xl bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600 
                                                                        hover:from-purple-500 hover:to-pink-700 
                                                                        dark:from-cyan-400 dark:to-emerald-200
                                                                        dark:hover:from-cyan-500 dark:hover:to-emerald-400
                                                                        font-medium">
        {{ item.category }}
      </h1>
      <h2 class="font-semibold text-xl text-dark-900 dark:text-white">
        {{ item.title }}
      </h2>
      <p class="py-3 text-warm-gray-700 dark:text-light-900">
        {{ item.description }}
      </p>
    </div>
    <!-- <div class="flex items-center md:col-span-2">
      {{ item.tags }}
    </div> -->
    
    <div class="flex items-center md:col-span-2">
      <div v-for="(tag, index) in item.tags" :key="index" class="inline-block 
                                                                  py-1.5 px-3 
                                                                  mr-2 mb-2 
                                                                  rounded-md 
                                                                  bg-gray-100 
                                                                  hover:bg-gray-200 
                                                                  text-sm text-gray-600 
                                                                  dark:text-light-900 
                                                                  dark:bg-dark-300 
                                                                  dark:hover:bg-dark-100
                                                                  truncate">
          {{ tag }}
      </div>
    </div>
    <!-- <Link
          href={`/articles/tags/${slugify(tag.title)}`}
          key={tag.title}
          className="inline-block py-1.5 px-3 mr-2 mb-2 rounded-md bg-gray-100 hover:bg-gray-200 text-sm text-gray-600 dark:bg-zinc-800 dark:hover:bg-zinc-700 dark:text-zinc-100 truncate"
        > -->
        <!-- </Link> -->
    <!-- <div
      class="bottom-0 right-0 absolute"
      v-if="checkNew(item.createdAt, item.updatedAt)"
    >
      new
    </div> -->
  </div>
</template>

<script lang="ts">
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const checkNew = (createdAt: string, updatedAt: string) => {
      const localeCreatedAt = new Date(createdAt).toLocaleDateString();
      const localeUpdatedAt = new Date(updatedAt).toLocaleDateString();

      if (localeCreatedAt == localeUpdatedAt) {
        return true;
      } else {
        false;
      }
    };

    return {
      checkNew,
    };
  },
});
</script>
