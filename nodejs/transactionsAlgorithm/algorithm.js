const { getRandomArrayItem, transactionMock, accounts, categories, targetAccounts } = require('./algorithm-mock')

const filterTransactions = ({ time, category }, start, end, selectedCategory) => {
    return Date.parse(time) > start && Date.parse(time) <= end && category === selectedCategory
}

const getBalanceByCategoryInPeriod = (transactions = [], category, start, end) => {

    if (!transactions.length) {
        return 0
    }

    const validTransactions = transactions.filter(transaction => filterTransactions(transaction, start, end, category))
    const totalBalance = validTransactions.reduce((currentTransaction, nextTransaction) => currentTransaction + nextTransaction.amount, 0)
    return totalBalance

}

const groupTransactionsByType = (transactions) => {
    transactions.sort((a, b) => { return new Date(a.time) - new Date(b.time) })

    const groupedTransactions = {}
    transactions.forEach((transaction) => {
        const month = new Date(transaction.time).getMonth()
        const { targetAccount} = transaction
        
        
        if (targetAccount+month in groupedTransactions) {
            groupedTransactions[targetAccount+month].push(transaction)
        }
        else {
            groupedTransactions[targetAccount+month] = [transaction]
        }
    })
    return groupedTransactions
}
const lessThanAMinute = (date1, date2) => {
    const differenceTravel = date2.getTime() - date1.getTime();
    const seconds = Math.floor((differenceTravel) / 1000);
    const timeLimit = 60
    return seconds <= timeLimit
}

const isDuplicatedTransaction = (firstTransaction, secondTransaction) => {
    const date1 = new Date(firstTransaction.time)
    const date2 = new Date(secondTransaction.time)
    return firstTransaction.sourceAccount === secondTransaction.sourceAccount &&
        firstTransaction.targetAccount === secondTransaction.targetAccount &&
        firstTransaction.category === secondTransaction.category &&
        firstTransaction.amount === secondTransaction.amount &&
        lessThanAMinute(date1, date2)
}


const findDuplicates = (transactions) => {
    const copiedTransactions = [...transactions]
    const duplicates = []
    while (copiedTransactions.length) {
        const firstTransaction = copiedTransactions[0]
        const secondTransaction = copiedTransactions[1]
        if (!secondTransaction) {
            if (firstTransaction)
                break
        }
        if (isDuplicatedTransaction(firstTransaction, secondTransaction)) {
            if (!duplicates.includes(firstTransaction)) {
                duplicates.push(firstTransaction)
            }
            if (!duplicates.includes(secondTransaction)) {
                duplicates.push(secondTransaction)
            }
        }
        copiedTransactions.shift()
    }
    return duplicates
}

const findDuplicateTransactions = (transactions) => {
    const groupedTransactions = groupTransactionsByType(transactions)
    const duplicates = []
    for (const i in groupedTransactions) {
        const transactions = groupedTransactions[i]
        const duplicatedTransactions = findDuplicates(transactions)
        if (duplicatedTransactions.length) {
            duplicates.push(duplicatedTransactions)
        }
    }
    return duplicates
}



module.exports = {
    getBalanceByCategoryInPeriod,
    findDuplicateTransactions
}

const transactions = [transactionMock(11, new Date(2011, 0, 1, 9, 25, 10, 33), 'cat1', 'account2', 'targetAccount25'),
transactionMock(21, new Date(2011, 0, 1, 9, 23, 10, 33), 'cat1', 'account1', 'targetAccount2'),
transactionMock(21, new Date(2011, 0, 1, 9, 23, 10, 33), 'cat1', 'account1', 'targetAccount2'),
transactionMock(33, new Date(2011, 0, 1, 9, 24, 10, 33), 'cat3', 'account1', 'targetAccount2'),
transactionMock(33, new Date(2011, 0, 1, 9, 24, 10, 33), 'cat3', 'account1', 'targetAccount2'),
transactionMock(33, new Date(2011, 0, 1, 9, 24, 10, 33), 'cat3', 'account1', 'targetAccount2'),
transactionMock(33, new Date(2011, 0, 1, 9, 24, 10, 33), 'cat5', 'account1', 'targetAccount2'),
transactionMock(33, new Date(2011, 0, 1, 9, 24, 10, 33), 'cat5', 'account1', 'targetAccount2'),
transactionMock(33, new Date(2011, 0, 1, 9, 24, 10, 33), 'cat5', 'account1', 'targetAccount2')
]

const anotherTransactions = [
    {
        id: 6,
        sourceAccount: 'my_account',
        targetAccount: 'internet_shop',
        amount: -250,
        category: 'other',
        time: '2018-03-01T22:16:40.000Z'
    },
    {
        id: 102,
        sourceAccount: 'my_account',
        targetAccount: 'internet_shop',
        amount: -250,
        category: 'other',
        time: '2018-03-01T22:16:50.000Z'
    },
    {
        id: 13,
        sourceAccount: 'my_account',
        targetAccount: 'coffee_shop',
        amount: -50,
        category: 'eating_out',
        time: '2018-04-01T10:24:00.000Z'
    },
    {
        id: 14,
        sourceAccount: 'my_account',
        targetAccount: 'coffee_shop',
        amount: -50,
        category: 'eating_out',
        time: '2018-04-01T10:24:40.000Z'
    },
    {
        id: 15,
        sourceAccount: 'my_account',
        targetAccount: 'coffee_shop',
        amount: -50,
        category: 'eating_out',
        time: '2018-04-01T10:25:10.000Z'
    },
    {
        id: 30,
        sourceAccount: 'my_account',
        targetAccount: 'coffee_shop',
        amount: -90,
        category: 'eating_out',
        time: '2018-05-07T09:54:21.000Z'
    },
    {
        id: 31,
        sourceAccount: 'my_account',
        targetAccount: 'coffee_shop',
        amount: -90,
        category: 'eating_out',
        time: '2018-05-07T09:55:10.000Z'
    },
    {
        id: 32,
        sourceAccount: 'my_account',
        targetAccount: 'coffee_shop',
        amount: -90,
        category: 'eating_out',
        time: '2018-05-07T09:56:09.000Z'
    },
    {
        id: 33,
        sourceAccount: 'my_account',
        targetAccount: 'coffee_shop',
        amount: -90,
        category: 'eating_out',
        time: '2018-05-07T09:57:05.000Z'
    }
    ]

findDuplicateTransactions(anotherTransactions).forEach(x => x.forEach(y => console.log(y.time, y.id)))