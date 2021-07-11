export {}

function test(a: string, b?: number, ...rest: number[]): string {
    return 'ok'
}


// 可选参数用?:


const test2: (a: number, b: string) => string = function (a: number, b: string): string {
    return 'ok'
}

