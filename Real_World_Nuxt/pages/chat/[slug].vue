<template>
    <div class="h-screen flex bg-gray-800 text-white">
        <!-- Sidebar -->
        <Sidebar></Sidebar>

        <!-- Main Content -->
        <div class="flex-1 flex">
            <!-- Chat Section -->
            <div class="w-3/5 bg-gray-900 flex flex-col">
                <div class="p-4 bg-gray-800 font-bold flex items-center justify-between h-16">
                    <span>Chat</span>
                </div>
                <div class="flex-1 overflow-y-auto p-4 space-y-4">
                    <ChatMessages></ChatMessages>
                </div>
                <!-- Input Box -->
                <div class="bg-gray-800 p-4">
                    <input type="text" placeholder="Message #general"
                        class="w-full p-2 bg-gray-700 rounded-sm text-white">
                </div>
            </div>

            <!-- Info Section -->
            <div class="w-2/5 bg-gray-800 flex flex-col">
                <ChatInfo></ChatInfo>
            </div>
        </div>
    </div>
</template>

<script setup>
import ServerHead from '~/components/serverHead.vue'

//Change to fetching from api
import { useFetch } from "#app";
const { data: friends } = await useFetch("/api/friends");

import { useRoute } from 'vue-router';

const route = useRoute();
const slug = route.params.slug; // Access the slug from route params

const currentFriend = ref([])
for (let i = 0; i < friends.value["friends"].length; i++) {
    const friend = friends.value["friends"][i];

    if (friend["name"] == slug) {
        currentFriend.value = friend
    }
}

</script>

<style>
@import 'tailwindcss/tailwind.css';
</style>
