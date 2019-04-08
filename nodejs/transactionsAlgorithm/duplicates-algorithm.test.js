const { assert } = require("chai")
const { getBalanceByCategoryInPeriod } = require('./algorithm')
const { transactionMock, buildArray, categories, getRandomArrayItem } = require('./algorithm-mock')
const {findDuplicateTransactions} =require('./algorithm')

const mockWithValidDuplicates = [{ id: 6,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-03-01T22:16:57.000Z' },
                                { id: 7,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-03-01T22:16:40.000Z' },{ id: 96,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-02-01T22:16:40.000Z' }]

const expectedValidDuplicates = [[{ id:7 ,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-03-01T22:16:40.000Z' },
                                { id: 6,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-03-01T22:16:57.000Z' }]]

const mockWithNoDuplicates = [
  { id: 6,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-03-01T21:11:57.000Z' },
  { id: 7,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-03-01T21:14:57.000Z' },
  { id: 42,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-03-01T20:16:57.000Z' },
  { id: 8,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-04-01T21:16:57.000Z' },
  { id: 33,
      sourceAccount: 'my_account',
      targetAccount: 'gym',
      amount: -251,
      category: 'other',
      time: '2018-05-01T21:16:57.000Z' }]

describe("findDuplicateTransactions()", function() {
  it("returns empty array if there are no transactions", function() {
    assert.deepEqual(findDuplicateTransactions([]), []);
  });
  
  it("test should return duplicated transactions correctly", function() {
    assert.deepEqual(findDuplicateTransactions(mockWithValidDuplicates), expectedValidDuplicates);
  });
  
  it("test should return an empty array because there are no duplicates", function() {
    assert.deepEqual(findDuplicateTransactions(mockWithNoDuplicates), []);
  })})