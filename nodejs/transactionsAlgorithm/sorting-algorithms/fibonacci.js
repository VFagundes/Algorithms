const fibonacci = (num) => {
    if (num < 2) return 1;
    let a = 1, b = 0, temp;

    while (num >= 0) {
        temp = a;
        a = a + b;
        b = temp;
        num--;
    }

    return b;
}


const recursiveFibonacci = (num) => {
    
    return fibonacci(num - 1) + fibonacci(num - 2);
}