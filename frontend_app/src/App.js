import React from 'react'
import styled from 'styled-components'

import logo from './logo.png'

const Wrapper = styled.div`
  padding: 3px;
  display: flex;
  align-items: center;
  background-color: #ff6503;
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
      margin-left: .5em;
      margin-right: .5em;
    }
  }
`

class App extends React.Component {
  render() {
    return (
      <Wrapper>
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
      </Wrapper>
    )
  }
}

export default App
