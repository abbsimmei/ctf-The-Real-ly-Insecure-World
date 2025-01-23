<template>
    <div class="flex items-center">
        <div v-if="isActive" class="w-2 h-8 mr-2 bg-white rounded-r-full"></div>
        <div v-if="!isActive" class="w-2 h-8 mr-2"></div>
        <img class=" rounded-full w-14" :src="`/images/serverLogos/${image}.png`" alt="Server Logo">
        <div class="ml-4 text-mg">{{ title }}</div>
    </div>

</template>

<script setup>

const props = defineProps({
  title: String,
  image: String,
  isActive: Boolean // Added the boolean prop

});</script>