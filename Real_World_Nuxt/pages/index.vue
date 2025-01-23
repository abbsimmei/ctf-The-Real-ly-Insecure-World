<template>
    <div class="h-screen flex bg-gray-800 text-white">
        <!-- Sidebar -->
        <Sidebar></Sidebar>

        <!-- Friends & Active Now Section -->
        <div class="flex-1 flex">
            <!-- Friends List -->
            <div class="w-3/5 bg-gray-900 flex flex-col">
                <div class="p-4 bg-gray-800 font-bold flex items-center justify-between h-16">
                    <span>Friends</span>
                    <div class="flex space-x-2">
                        <button class="px-4 py-1 bg-gray-700 text-sm rounded-sm hover:bg-gray-600">Online</button>
                        <button class="px-4 py-1 bg-gray-700 text-sm rounded-sm hover:bg-gray-600">All</button>
                        <button class="px-4 py-1 bg-gray-700 text-sm rounded-sm hover:bg-gray-600">Pending</button>
                        <button class="px-4 py-1 bg-green-600 text-sm rounded-sm hover:bg-green-500">Add Friend</button>
                    </div>
                </div>
                <div class="p-4">
                    <input type="text" placeholder="Search"
                        class="w-full px-4 py-2 bg-gray-800 rounded-sm focus:outline-none">
                </div>
                <div class="flex flex-col p-4 space-y-2">
                    <FriendList></FriendList>
                </div>
            </div>

            <!-- Active Now Section -->
            <div class="w-2/5 bg-gray-800 flex flex-col">
                <div class="p-4 font-bold text-lg">Active Now</div>
                <div class="p-4 space-y-4">
                    <!-- Active Friend 1 -->
                    <div class="flex items-center space-x-4 p-3 bg-gray-900 rounded-lg hover:bg-gray-850">
                        <img :src="`/images/friendLogos/swinceball.png`" alt="Swinceball Avatar"
                            class="h-12 w-12 rounded-full border border-gray-700">
                        <div>
                            <p class="text-white font-semibold">Swinceball</p>
                            <p class="text-sm text-gray-400">Playing <span class="text-blue-500 font-semibold">Hearts of
                                    Iron</span> - 37h</p>
                        </div>
                    </div>
                    <!-- Placeholder for more active friends -->
                    <div class="text-sm text-gray-400">
                        When a friend starts an activity – like playing a game or hanging out on voice – we'll show it
                        here!
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import ServerHead from '~/components/serverHead.vue'
import FriendList from '~/components/friendList.vue'
</script>

<style>
@import 'tailwindcss/tailwind.css';

/* Custom hover color for "Active Now" section items */
.hover\:bg-gray-850:hover {
    background-color: #2b2d31;
}
</style>
