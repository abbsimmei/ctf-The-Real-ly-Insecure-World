<template>
    <!-- Chat messages -->
    <div class="flex items-start space-x-4" v-for="chatI in chat['chat']">
        <img :src="`/images/friendLogos/${chatI['sender']}.png`" class="w-10 h-10 rounded-full">
        <div>
            <p class="font-bold">{{ chatI['sender'] }} <span class="text-sm text-gray-500">{{ chatI['time'] }}</span>
            </p>
            <p>{{ chatI['message'] }}</p>
        </div>
    </div>

</template>

<script setup>
import { useFetch } from "#app";

// ########################
// #        API           #
// ########################
const { data: friends } = await useFetch("http://127.0.0.1:8000/friends/")

import { useRoute } from 'vue-router';

const route = useRoute();
const slug = route.params.slug; // Access the slug from route params

import { findSingleFriend } from "~/utils/functions/loadFriends";
const currentFriend = findSingleFriend(slug, friends)

const { data: chat } = await useFetch("/api/chatar/test");


</script>