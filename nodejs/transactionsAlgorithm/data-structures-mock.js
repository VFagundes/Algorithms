const BASE_NUMBER = 100
const randomDecimalNumber = (base = BASE_NUMBER) => Math.random() * base
const randomInteger = ()=> parseInt(randomDecimalNumber())
const buildMany = (n, buildFunction) => {
    return [...Array(n).keys()].
        map(x => { return buildFunction() })
}
module.exports = { buildMany, randomDecimalNumber, randomInteger}
