const BASE_NUMBER = 100
const getRandomArrayItem = arr => arr[parseInt(Math.random() * BASE_NUMBER % arr.length)]
const accounts = ['my_account', 'their_account', 'other_account']
const targetAccounts = ['coffee_shop', 'pub', 'hotel']
const categories = ['eating_out', 'music', 'sporting']

const buildArray = (n, obj) => { return [...Array(n).keys()].map(x => { return obj }) }


const transactionMock = (amount, date, category, account, targetAccount) => ({
    id: parseInt(Math.random() * BASE_NUMBER),
    sourceAccount: account,
    targetAccount: targetAccount,
    amount: amount,
    category: category,
    time: date.toISOString()
})

module.exports = {
    transactionMock,
    getRandomArrayItem,
    buildArray,
    categories,
    targetAccounts,
    accounts
}