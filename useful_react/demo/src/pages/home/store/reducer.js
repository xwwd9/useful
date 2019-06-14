import {fromJS} from "immutable"

const defaultState = fromJS({
    topics:[{
        id:1,
        title:"热点新闻",
        url:"//upload-images.jianshu.io/upload_images/124665-2489ecf120f0c5e6?imageMogr2/auto-orient/strip|imageView2/1/w/360/h/240"
    },{
        id:2,
        title:"百度关注",
        url:"//upload-images.jianshu.io/upload_images/124665-2489ecf120f0c5e6?imageMogr2/auto-orient/strip|imageView2/1/w/360/h/240"
    }]
});


export default (state = defaultState, action) => {


    switch (action.type) {


        default:
            return state
    }

}



