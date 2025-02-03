<template>
    <div class="p-4 font-bold text-lg">User Info</div>
    <div class="p-4 mt-4 flex flex-col items-center space-y-4">
        <!-- Profile Picture -->
        <img :src="`/images/friendLogos/${currentFriend['name']}.png`" alt="User" class="w-20 h-20 rounded-full">

        <!-- Username -->
        <p class="text-xl font-bold">{{ currentFriend['name'] }}</p>
        <p class="text-md text-gray-400">{{ currentFriend['status'] }}</p>

        <!-- About Me -->
        <div class="w-3/4">
            <div class="bg-gray-700 p-6 mt-4 rounded-xl">
                <div class="">
                    <p class="text-sm font-semibold pb-2">About Me:</p>
                    <p class="text-sm text-gray-300 pb-2">{{ currentFriend["about"] }}</p>
                </div>

                <div class="text-sm text-gray-400">
                    <p class="pb-2">Member Since</p>
                    <p class="text-gray-300">{{ currentFriend["since"] }}</p>
                </div>
            </div>

            <!-- Mutual Info -->
            <div class="bg-gray-700 p-6 mt-4 rounded-xl">
                <div class="w-full text-center divide-y divide-gray-700">
                    <div class="py-2">
                        <p class="text-sm">Mutual Servers — <span class="text-gray-300">{{ currentFriend["mutser"]
                                }}</span></p>
                    </div>
                    <div class="py-2">
                        <p class="text-sm">Mutual Friends — <span class="text-gray-300">{{ currentFriend["mutfri"]
                                }}</span></p>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
//Change to fetching from api
import { useFetch } from "#app";

// ########################
// #        API           #
// ########################
const { data: APIroute } = await useFetch("/api/ipAdress");
//const { data: friends } = await useFetch("/api/friends");
const { data: friends } = await useFetch(`${APIroute.value}/friends/`)


import { useRoute } from 'vue-router';

const route = useRoute();
const slug = route.params.slug; // Access the slug from route params

import { findSingleFriend } from "~/utils/functions/loadFriends";
const currentFriend = findSingleFriend(slug, friends)

</script>
