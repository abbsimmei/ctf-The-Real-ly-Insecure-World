<template>
    <div class="w-1/5 bg-gray-900 flex flex-col">
        <div class="p-4 bg-gray-800 font-bold h-16">Servers</div>
        <div class="p-4 border-gray-950 border-r-4">
            <NuxtLink :to="`/`">
                <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="Direct messages"
                    :image="'discord'" :isActive="true"></ServerHead>
            </NuxtLink>
            <div class="border-4 border-gray-950 border-dashed rounded-sm"></div>
            <ServerHead class="p-2 rounded-sm hover:bg-gray-700 cursor-pointer" title="Cozy home" :image="'house'"
                :isActive="false"></ServerHead>
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
    </div>
</template>