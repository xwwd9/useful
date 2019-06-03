import React, {Component, Fragment} from 'react'
import {
    Addition,
    Button,
    HeaderWrapper,
    Logo,
    Nav,
    NavItem,
    NavSearch, SearchWrapper
} from "./style";
import {IconGlobal} from "../../statics/iconfont/iconfont";
import {CSSTransition} from 'react-transition-group';

class Header extends Component {

    constructor(props) {
        super(props);
        this.state = {
            focused: false
        }
    }


    handleInputFocus = () => {
        this.setState((preState) => ({
            focused: true
        }))
    };


    handleInputBlur = () => {
        this.setState((preState) => ({
            focused: false
        }))
    }

    render() {
        return (
            <Fragment>
                <IconGlobal/>
                <HeaderWrapper>
                    <Logo/>
                    <Nav>
                        <NavItem className='left active'>首页</NavItem>
                        <NavItem className='left'>下载App</NavItem>
                        <NavItem className='right'>登录</NavItem>
                        <NavItem className='right'>
                            <i className="iconfont">&#xe636;</i>
                        </NavItem>
                        <SearchWrapper>
                            <CSSTransition
                                in={this.state.focused}
                                timeout={200}
                                classNames="slide"
                            >
                                <NavSearch
                                    className={this.state.focused ? 'focused' : ''}
                                    onFocus={this.handleInputFocus}
                                    onBlur={this.handleInputBlur}
                                >

                                </NavSearch>
                            </CSSTransition>
                            <i className={this.state.focused ? 'focused iconfont' : 'iconfont'}>&#xe6cf;</i>

                        </SearchWrapper>
                    </Nav>
                    <Addition>

                        <Button className='writting'>
                            <i className="iconfont">&#xe61b;</i>
                            写文章
                        </Button>
                        <Button className='reg'>注册</Button>
                    </Addition>
                </HeaderWrapper>
            </Fragment>
        )

    }
}


export default Header