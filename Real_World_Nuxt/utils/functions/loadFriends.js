export function findSingleFriend(slug, friends) {
    
    const currentFriend = ref([])
    for (let i = 0; i < friends.value["friends"].length; i++) {
        const friend = friends.value["friends"][i];

        if (friend["name"] == slug) {
            currentFriend.value = friend
            return currentFriend
        }
}

}