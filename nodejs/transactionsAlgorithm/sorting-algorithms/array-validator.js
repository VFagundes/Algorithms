
const isSortedCorrectly = (assertedArray, expectedArray) => {
    
    if(assertedArray.length !== expectedArray.length)
    {
        return false
    }

    let isValid = true
    
    for (let i = 0; i < assertedArray.length; i++) {
        const assertedElement = assertedArray[i];
        const expectedElement = expectedArray[i]

        if (assertedElement !== expectedElement) {
            isValid = false
            break
        }
    }
    return isValid
}

module.exports = {
    isSortedCorrectly
}