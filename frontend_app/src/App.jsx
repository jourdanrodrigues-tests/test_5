import axios from 'axios'
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

class App extends React.Component {
  state = {
    stories: [],
  }

  async componentWillMount() {
    const response = await axios.get(`${process.env.API_URL}/stories/`)
    this.setState({
      stories: response.data.data,
    })
  }

  render() {
    return (
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
          {this.state.stories.map((story, i) => <StoryRow key={story.id} number={i + 1} {...story}/>)}
        </Body>
      </div>
    )
  }
}

export default App
