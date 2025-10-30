function fib(n) {
    if (n < 0) {
        throw new Error("Input must be a non-negative integer");
    }
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

const numbers = [0, 1, 2, 3, -4, 5, 6, 7, 8, 9];
numbers.forEach(n => {
    try {
        const result = fib(n);
        console.log(`fib(${n}) = ${result}`);
    } catch (e) {
        console.log(`Error for n=${n}: ${e.message}`);
    }
});