


const defalutState = {
    inputValue:'123',
    list:[1,2]
}

export default (state=defalutState, action) => {
    console.log("****")
    if(action.type === "change_input_value"){
        // 拷贝对象
        const newState = JSON.parse(JSON.stringify(state))
        newState.inputValue = action.value
        return newState
    }
    return state
}