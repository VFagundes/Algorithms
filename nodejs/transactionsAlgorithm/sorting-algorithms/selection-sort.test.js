const {selectionSort} = require('./selection-sort.js')
const {assert} = require('chai')
const { buildMany, randomInteger } = require('../data-structures-mock')
const { isSortedCorrectly } = require('./array-validator')
describe('tests on selectionSort Algorithm',() => {
    it("test should sort array correctly", () => {
        const unsortedArray = buildMany(100, randomInteger)
        const asserted = selectionSort(Object.assign([], unsortedArray))
        const expected = Object.assign([], unsortedArray).sort((a, b) => a - b)
        assert.equal(true,isSortedCorrectly(asserted,expected))
        
    })
    it("test should do nothing because the array is empty", () => {
        const unsortedArray = buildMany(0, randomInteger)
        const asserted = selectionSort(Object.assign([], unsortedArray))
        const expected = Object.assign([], unsortedArray).sort((a, b) => a - b)
        assert.equal(true,isSortedCorrectly(asserted,expected))
    });
    it("test should return only one item", () => {
        const unsortedArray = buildMany(1, randomInteger)
        const asserted = selectionSort(Object.assign([], unsortedArray))
        const expected = Object.assign([], unsortedArray).sort((a, b) => a - b)
        assert.equal(true,isSortedCorrectly(asserted,expected))
    });

})