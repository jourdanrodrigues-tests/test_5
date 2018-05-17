import React from 'react'
import styled from 'styled-components'

import logo from './logo.png'
import StoryRow from './containers/StoryRow'

const Header = styled.div`
  padding: 3px;
  display: flex;
  align-items: center;
  background-color: #FF6503;
`

const Title = styled.span`
  font-weight: bold;
  margin-left: .5em;
`

const Logo = styled.img`
  width: 18px;
  height: 18px;
  border: 1px solid white;
`

const menuItemMargin = '.5em'

const Menu = styled.ul`
  margin: 0;
  display: flex;
  list-style: none;
  padding-left: .5em;
  
  li {
    display: flex;
    
    &:not(:last-child):after {
      content: '|';
      display: block;
      margin-left: ${menuItemMargin};
      margin-right: ${menuItemMargin};
    }
  }
`

const Body = styled.div`
  padding: .5em 0 1em .5em;
  background-color: #F6F6F0;
`

const App = () => (
  <div>
    <Header>
      <Logo src={logo}/>
      <Title>Hacker News</Title>
      <Menu>
        <li>welcome</li>
        <li>new</li>
        <li>threads</li>
        <li>comments</li>
        <li>show</li>
        <li>ask</li>
        <li>jobs</li>
        <li>submit</li>
      </Menu>
    </Header>
    <Body>
      <StoryRow/>
    </Body>
  </div>
)

export default App
