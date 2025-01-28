function isEven(number) {
    return number % 2 === 0; // True if even
}

export async function combine(id1) {
    const { data: you } = await useFetch("http://127.0.0.1:8000/you/")
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