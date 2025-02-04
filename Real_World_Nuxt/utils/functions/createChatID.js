function isEven(number) {
    return number % 2 === 0; // True if even
}

export async function combine(id1) {
    const { data: APIroute } = await useFetch("/api/ipAdress");
    //const { data: friends } = await useFetch("/api/friends");

    const { data: you } = await useFetch(`${APIroute.value}/you/`)
    const youID  = you.value["you"][0]["id"]
    let newID = ""

    let youNum = 0
    let idNum = 0
    for (let i = 0; i < (youID.length + id1.length); i++) {
        const check = isEven(i)
        if (check == true) {
            newID = newID + id1[idNum]
            idNum += 1
        } else {
            newID = newID + youID[youNum]
            youNum += 1
        }
    }
    return newID;
}