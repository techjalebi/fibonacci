function fibonacci(n) {
    if (n < 0) {
        throw new Error("Input must be a non-negative integer");
    }
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

const numbers = [0, 1, 2, 3, -4, 5, 6, 7, 8, 9];
numbers.forEach(n => {
    try {
        const result = fibonacci(n);
        console.log(`fibonacci(${n}) = ${result}`);
    } catch (e) {
        console.log(`Error for n=${n}: ${e.message}`);
    }
});