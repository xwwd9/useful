import React, {Component, Fragment} from 'react'
import {
    Addition,
    Button,
    HeaderWrapper,
    Logo,
    Nav,
    NavItem,
    NavSearch,
    SearchInfo,
    SearchInfoItem,
    SearchInfoSwitch,
    SearchInfoTitle,
    SearchWrapper
} from "./style";
import {IconGlobal} from "../../statics/iconfont/iconfont";
import {CSSTransition} from 'react-transition-group';
import {connect} from "react-redux"
import {getList, mouseEnter, search_focus} from "./store/actionCreators";


class Header extends Component {

    constructor(props) {
        super(props);
        this.state = {
            focused: false
        }
    }


    render() {
        console.log("updata")
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
                                in={this.props.focused}
                                timeout={200}
                                classNames="slide"
                            >
                                <NavSearch
                                    className={this.props.focused ? 'focused' : ''}
                                    onFocus={this.props.handleInputFocus}
                                    onBlur={this.props.handleInputBlur}
                                >

                                </NavSearch>
                            </CSSTransition>
                            <i className={this.props.focused ? 'focused iconfont zoom' : 'iconfont zoom'}>&#xe6cf;</i>
                            {
                                this.props.focused || this.props.mouseIn ?
                                    <SearchInfo onMouseEnter={this.props.handleMouseIn}
                                                onMouseLeave={this.props.handleMouseLeave}>
                                        <SearchInfoTitle>
                                            热门搜索
                                            <SearchInfoSwitch onClick={() => this.props.handleSwitch(this.spin)}>
                                                <i ref={(ref) => this.spin = ref}
                                                   className="iconfont spin">&#xe7eb;</i>
                                                换一换
                                            </SearchInfoSwitch>
                                        </SearchInfoTitle>
                                        <div>
                                            {
                                                this.props.list.map((item, index) => {
                                                    return <SearchInfoItem key={item}>{item}</SearchInfoItem>
                                                })
                                            }
                                        </div>
                                    </SearchInfo> : null
                            }

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


const mapStateToProps = (state) => {
    return {
        focused: state.get("header").get("focused"),
        list: state.get("header").get("list"),
        mouseIn: state.get("header").get("mouseIn")
    }
};


const mapDispatchToProps = (dispatch) => {
    return {
        handleInputFocus() {
            const action = search_focus(true);
            const ac = getList();
            dispatch(ac);
            dispatch(action)
        },


        handleInputBlur() {
            const action = search_focus(false);
            dispatch(action)
        },

        handleSwitch(spin) {

            const angle = spin.style.transform.replace(/[^0-9]/ig,'');
            if (angle === "360"){
                spin.style.transform = 'rotate(0deg)'
            }
            else{
                spin.style.transform = 'rotate(360deg)'
            }

            console.log(spin, angle, spin.style.transform);
            // this.spin
            // console.log("handle switch");
            const action = getList(true);
            dispatch(action)
        },

        handleMouseIn() {
            // console.log("**************************")
            const action = mouseEnter(true);
            dispatch(action)
        },

        handleMouseLeave() {
            // console.log("**************************")
            const action = mouseEnter(false);
            dispatch(action)
        }
    }
};


export default connect(mapStateToProps, mapDispatchToProps)(Header);

