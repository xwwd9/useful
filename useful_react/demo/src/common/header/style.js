import styled from 'styled-components'
import logoPic from '../../statics/logo.png'


export const HeaderWrapper = styled.div`
    height:58px;
    border-bottom:1px solid #f0f0f0;
    position:relative;
    
`;

export const Logo = styled.a.attrs({
    href: '/'
})`
    height:56px;
    width:100px;
    display:block;
    position:absolute;
    top:0;
    left:0;
    background:url(${logoPic});
    // background:url(${(props) => props.imaUrl}); 直接从主键传过来的参数
    background-size:contain
`;

export const Nav = styled.div`
    width:960px;
    margin:0 auto;
    height:100%; 
`;

export const NavItem = styled.div`
    line-height:56px;
    padding:0 15px;
    font-sizt:17px;
    color:#333;
    &.left{
        float:left;
    }
    &.right{
        float:right;
        color:#969696;
    }
    &.active{
        color: #ea6f5a
    }
    
`;


export const SearchWrapper = styled.div`
    float:left;
    position:relative;
    
    
    
    .zoom{
        position:absolute;
        right:5px;
        bottom:5px;
        width:30px;
        line-height:30px;
        border-radius : 15px;
        text-align:center;
        &.focused{
            background:#777;
            color:#fff;
        }
    }
`;

export const SearchInfo = styled.div`
    position: absolute;
    left:0;
    top:56px;
    width:240px;
    padding:0 20px;
    box-shadow: 0 0 8px rgba(0,0,0,.2);
    background:#fff;
`;


export const SearchInfoTitle = styled.div`
    margin-top:20px;
    margin-bottom:15px;
    color:#969696;
    line-height:20px;
    font-size:14px;
`;

export const SearchInfoSwitch = styled.span`
    float:right;
    font-size:13px;
    cursor:pointer;
    .spin{
        float:left;
        font-size:12px;
        margin-right:5px;
        transition:all .2s ease-in;
        transform:rotate(0deg);
        transfrom-origin:center center;
    }
`;


export const SearchInfoItem = styled.a`
    display:block;
    float:left; 
    line-height:20px;
    padding:0 5px;
    font-size:12px;
    border: 1px solid #ddd;
    color:#969696;
    border-radius:2px;
    margin-right:10px;
    margin-bottom:10px;
`;

export const NavSearch = styled.input.attrs({
    placeholder: 'search'
})`
      width:160px;
      height:38px;
      border:none;
      outline:none;
      border-radius:19px;
      background:#eee;
      margin-top:9px;
      margin-left:20px;
      padding:0 30px 0 20px;
      box-sizing:border-box;
      font-size:14px;
      color:#666;
      &::placeholder{
        color:#11;
      }
      &.focused{
        width:250px;
        .iconfont{
                
        }
      }
      
      
    &.slide-enter{
        transition: all .2s ease-out;
    }
    &.slide-enter-active{
        width: 250px;
    }
    
    &.slide-exit{
        transition: all .2s ease-out;
    }
    &.slide-exit-active{
        width: 160px;
    }
`;

export const Addition = styled.div`
    position:absolute;
    right:0;
    top:0;
    height:56px;

`;


export const Button = styled.div`
    float:right;
    line-height:38px;
    border-radius:19px;
    margin-top:9px;
    border:1px solid #ec6149;
    padding: 0 20px;
    margin-right:20px;
    &.reg{
        color: #ec6149;
    }
    &.writting{
        color:#fff;
        background: #ec6149;
    }
`;





