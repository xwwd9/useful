import {fromJS} from "immutable"

const defaultState = fromJS({
        topics: [{
            id: 1,
            title: "热点新闻",
            url: "//upload-images.jianshu.io/upload_images/124665-2489ecf120f0c5e6?imageMogr2/auto-orient/strip|imageView2/1/w/360/h/240"
        }, {
            id: 2,
            title: "百度关注",
            url: "//upload-images.jianshu.io/upload_images/124665-2489ecf120f0c5e6?imageMogr2/auto-orient/strip|imageView2/1/w/360/h/240"
        }],
        artists: [
            {
                id: 1,
                title: "我靠这27点从170斤瘦到了139斤，现在就手把手教给你",
                url: "https://upload-images.jianshu.io/upload_images/3026386-5f3de68c8e149ed8?imageMogr2/auto-orient/strip|imageView2/1/w/360/h/240",
                desc: "0.抛弃月瘦二三十斤的想法。 这一点是基础，如果你总是执念于一个月减掉几十斤的体重，那你就别往下看了。 1.制定合理的计划。 计划包括两个方面，..."
            },
            {
                id: 2,
                title:
                    "贾玲救场关晓彤：高情商，一个人的终极性感",
                url:
                    "//upload-images.jianshu.io/upload_images/9276238-7923fcae67354688?imageMogr2/auto-orient/strip|imageView2/1/w/360/h/240",
                desc: "“不知道自己多有魅力，才是你的魅力。” 迷人而不自知的人很多，贾玲就是其中之一。 最近，豆瓣鹅组评选出“最喜爱女明星TOP20榜单，贾玲夺得第..."
            }
        ]
    })
;


export default (state = defaultState, action) => {


    switch (action.type) {


        default:
            return state
    }

}



