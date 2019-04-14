const { defaultComparator } = require('./array-comparator')


const selectionSort = (unsortedArray) => {
    const sortedArray = [...unsortedArray]
    for (let i = 0; i < sortedArray.length; i++) {
        let current = sortedArray[i];
        for (let j = i + 1; j < sortedArray.length; j++) {
            let next = sortedArray[j];
            if (next < current) {
                current ^= next
                next ^= current
                current ^= next
                sortedArray[i]= current
                sortedArray[j] = next
            }
        }
    }
    return sortedArray
}


module.exports = { selectionSort }