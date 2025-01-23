<template>
    <div v-for="friend in friends['friends']">
        <NuxtLink :to="`/chat/${friend['name']}`">
            <div class="flex items-center justify-between p-2 hover:bg-gray-700 rounded-sm">
                <div class="flex items-center space-x-4">
                    <img class="w-12 h-12 bg-gray-600 rounded-full" :src="`/images/friendLogos/${friend['image']}.png`">
                    <div>
                        <div class="font-bold">{{ friend['name'] }}</div>
                        <div class="text-sm text-gray-400">{{ friend['status'] }}</div>
                    </div>
                </div>
                <div class="flex space-x-2">
                    <button class="w-8 h-8 bg-gray-800 rounded-full"><img class="rounded-full"
                            :src="`/images/symbol/talk.png`"></button>
                    <button class="w-8 h-8 bg-gray-800 rounded-full test"><img class="rounded-full"
                            :src="`/images/symbol/dots.png`"></button>
                </div>
            </div>
        </NuxtLink>
    </div>
</template>

<script setup>
import { NuxtLink } from '#components'

//Change to fetching from api
import { useFetch } from "#app";
const { data: friends } = await useFetch("/api/friends");


</script>