const a: Array<number> = [1, 2, 3, 4]
const b: number[] = [1, 2, 3, 45]

function test(...args: number[]){
    return args.reduce(((previousValue, currentValue) => previousValue+currentValue), 0)
}

test(1,2,3,4)
export {}

