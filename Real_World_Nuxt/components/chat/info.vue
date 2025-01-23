<template>
    <div class="p-4 font-bold text-lg">User Info</div>
    <div class="p-4 flex flex-col items-center space-y-4">
        <!-- Profile Picture -->
        <img :src="`/images/friendLogos/swinceball.png`" alt="User" class="w-20 h-20 rounded-full">

        <!-- Username -->
        <p class="text-xl font-bold">Swinceball</p>

        <!-- About Me -->
        <div class="w-3/4">
            <div class="bg-gray-700 p-6 mt-4 rounded-xl">
                <div class="">
                    <p class="text-sm font-semibold pb-2">About Me:</p>
                    <p class="text-sm text-gray-300 pb-2">"I am happy because everyone loves me"</p>
                </div>

                <div class="text-sm text-gray-400">
                    <p class="pb-2">Member Since</p>
                    <p class="text-gray-300">1 Dec 2018</p>
                </div>
            </div>

            <!-- Mutual Info -->
            <div class="bg-gray-700 p-6 mt-4 rounded-xl">
                <div class="w-full text-center divide-y divide-gray-700">
                    <div class="py-2">
                        <p class="text-sm">Mutual Servers — <span class="text-gray-300">2</span></p>
                    </div>
                    <div class="py-2">
                        <p class="text-sm">Mutual Friends — <span class="text-gray-300">2</span></p>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
