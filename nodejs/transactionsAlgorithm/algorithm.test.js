const { assert } = require("chai")
const { getBalanceByCategoryInPeriod } = require('./algorithm')
const { transactionMock, buildArray, categories, getRandomArrayItem, accounts, targetAccounts } = require('./algorithm-mock')

describe("getBalanceByCategoryInPeriod() tests", function () {
    it("test should return 0 if there are no transactions", function () {
        assert.equal(
            getBalanceByCategoryInPeriod(
                [],
                "groceries",
                new Date("2018-03-01"),
                new Date("2018-03-31")
            ),
            0
        );
    });
    it("test should return the transactions value by period correctly on success business scenario", function () {

        const expected = -100
        const selectedCategory = getRandomArrayItem(categories)
        const amount = -50
        const time = new Date(2011, 0, 2)
        const targetAccount = getRandomArrayItem(targetAccounts)
        const account = getRandomArrayItem(accounts)

        const transactions = buildArray(2, transactionMock(amount, time, selectedCategory,account,targetAccount))
        const balanceByCategory = getBalanceByCategoryInPeriod(transactions, selectedCategory, new Date(2011, 0, 1), new Date(2011, 0, 11))
        assert.equal(balanceByCategory, expected);
    });
    it("test should return 0 because there are no transaction in the period", function () {

        const expected = 0
        const selectedCategory = getRandomArrayItem(categories)
        const amount = -503
        const time = new Date(2013, 5, 12)
        const transactions = buildArray(5, transactionMock(amount, time, selectedCategory))
        const balanceByCategory = getBalanceByCategoryInPeriod(transactions, selectedCategory, new Date(2011, 0, 1), new Date(2011, 0, 11))

        assert.equal(balanceByCategory, expected);
    });
    it("test should return 2 of three transactions to enforce the criteria of the filter", function () {

        const expected = -500
        const validCategory = categories[0]
        const invalidCategory = categories[1]
        const validAmount = -100
        const invalidAmount = -132
        const validTime = new Date(2015, 2, 5)
        const invalidTime = new Date(2008, 10, 1)
        const validTransactions = buildArray(5, transactionMock(validAmount, validTime, validCategory))
        const invalidTransactions = buildArray(3, transactionMock(invalidAmount, invalidTime, invalidCategory))
        const allTransactions = validTransactions.concat(invalidTransactions)
        const balanceByCategoryInPeriod = getBalanceByCategoryInPeriod(
            allTransactions,
            validCategory,
            new Date(2015, 0, 1),
            new Date(2015, 4, 11))
        assert.equal(balanceByCategoryInPeriod, expected);
    });

});
