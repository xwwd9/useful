export {}

enum mytypes {
    first= 2,
    second,
}


// 通过枚举值获取枚举键
console.log(mytypes[2])

const enum mytypes2 {
    first= 2,
    second,
}
// const开头的字符串不能通过枚举值类确定key


