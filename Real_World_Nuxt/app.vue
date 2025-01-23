<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>


<script setup lang="ts">

//Documentation: https://nuxt.com/docs/getting-started/seo-meta
useHead({
  title: 'The Real(ly insecure) World',
  meta: [
    { name: 'The Real World', content: 'My amazing site.' }
  ],
  bodyAttrs: {
    class: 'test'
  },
  script: [{}]
})
</script>