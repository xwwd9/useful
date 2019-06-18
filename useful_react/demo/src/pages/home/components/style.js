import styled from "styled-components"


export const TopicWraper = styled.div`
    padding: 20px 0px 10px 0px;
    overflow:hidden;
    margin-left:-18px;
    border-bottom:1px solid #dcdcdc;
`;


export const TopicItem = styled.div`
    margin-left:18px; 
    float:left;
    height:32px;
    line-height:32px;
    font-size:12px;
    padding-right:10px;
    coloe:#000;
    background:#f7f7f7;
    border: 1px solid #dcdcdc;
    border-radius:4px;
    margin-bottom:18px;
    
    .topic-pic{
        display:block;
        float:left;
        width:32px;;
        height:32px;
        margin-right:10px;
    }
`;


export const ListItem = styled.div`
    padding:20px 0;
    overflow:hidden;
    border-bottom:1px solid #dcdcdc;
    .list-pic{
        width:125px;
        height:100px;
        display:block;
        float:right;
        border-radius:10px;
    }
    
    
`;


export const ListInfo = styled.div`
    width:500px;
    float:left;
    .title{
        line-height:27px;
        font-size:18px;
        font-weight:bold;
        color:#
    }
    .desc{
        line-height:24px;
        font-size:13px;
        color:#999;
    }
`;


export const RecommList = styled.div`
    
    padding: 30px 0 0;
    .rec-pic{
        width: 100%;
        min-height: 50px;
        margin-bottom: 6px;
        border-radius: 4px;
    }
`

