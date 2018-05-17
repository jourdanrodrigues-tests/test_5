import React from 'react'
import styled from 'styled-components'

const Wrapper = styled.div`
  display: flex;
`

const hideButtonMargin = '.3em'
const secondaryTextColor = '#878987'

const HideButton = styled.span`
  display: flex;
  cursor: pointer;
  
  &:after, &:before {
    content: '|';
    display: block;
    margin-left: ${hideButtonMargin};
    margin-right: ${hideButtonMargin};
  }
`

const Counter = styled.span`
  width: 2em;
  color: #99999A;
`

const Content = styled.div`
  display: flex;
  flex-direction: column;
`

const Title = styled.span`
  font-size: 11pt;
`

const HostLink = styled.span`
  font-size: 9pt;
  margin-left: .25em;
  color: ${secondaryTextColor};
`

const BottomSection = styled.div`
  display: flex;
  font-size: 8pt;
  color: ${secondaryTextColor};
`

const StoryRow = () => (
  <Wrapper>
    <Counter>1.</Counter>
    <Content>
      <div>
        <Title>A very big and descriptive title about some sort of random subject</Title>
        <HostLink>(web.site)</HostLink>
      </div>
      <BottomSection>
        <span>62 points by <a>user</a> 3 hours ago</span>
        <HideButton>hide</HideButton>
        <span>14 comments</span>
      </BottomSection>
    </Content>
  </Wrapper>
)

export default StoryRow
