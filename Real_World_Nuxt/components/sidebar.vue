<template>
    <div class="w-1/5 h-screen bg-gray-900 flex flex-col">
        <!-- Top Header -->
        <div class="p-4 bg-gray-800 font-bold h-16">Servers</div>

        <!-- Server List (Expandable with Scroll) -->
        <div class="p-4 border-gray-950 border-r-4 flex-grow overflow-y-auto">
            <NuxtLink :to="`/`">
                <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="Direct messages"
                    :image="'discord'" :isActive="true"></ServerHead>
            </NuxtLink>
            <div class="border-4 border-gray-950 border-dashed rounded-sm"></div>
            <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="Beluga's server"
                :image="'beluga'" :isActive="false"></ServerHead>
            <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="AMONG US" :image="'among'"
                :isActive="false"></ServerHead>
            <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="JS-help" :image="'javascript'"
                :isActive="false"></ServerHead>
            <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="Official Minecraft Server"
                :image="'minecraft'" :isActive="false"></ServerHead>
            <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="Only for TOP G" :image="'tate'"
                :isActive="false"></ServerHead>
            <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="Swinceball's server"
                :image="'swinceball'" :isActive="false"></ServerHead>
        </div>

        <!-- User Profile Section (Stays at Bottom) -->
        <div class="flex bg-gray-800 p-4 justify-center items-center mt-auto">
            <img class="rounded-full w-10 h-10 mr-4" :src="`/images/friendLogos/Average_Spetsare.png`">
            <div class="mr-2">
                <p>Average_Spetsare</p>
                <p class="text-gray-400">Online</p>
            </div>
            <img class="rounded-full w-8 h-8" :src="`/images/symbol/mic.png`">
            <img class="rounded-full w-8 h-8" :src="`/images/symbol/headphone.png`">
            <img class="rounded-full w-8 h-8" :src="`/images/symbol/setting.png`">
        </div>
    </div>
</template>
