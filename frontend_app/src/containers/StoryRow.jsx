import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import {getHost, getHoursDifferenceFromNow} from '../utils'

const Wrapper = styled.div`
  display: flex;
  
  &:not(:first-child) {
    margin-top: .5em;
  }
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

const Number = styled.span`
  width: 2em;
  display: flex;
  color: #99999A;
  align-items: center;
`

const Content = styled.div`
  display: flex;
  flex-direction: column;
`

const Title = styled.span`
  font-size: 11pt;
`

const Anchor = styled.a`
  color: inherit;
  text-decoration: none;
  
  &:hover {
    text-decoration: underline;
  }
`

const HostLink = styled(Anchor)`
  font-size: 9pt;
  cursor: pointer;
  margin-left: .25em;
  color: ${secondaryTextColor};
`

const BottomSection = styled.div`
  display: flex;
  font-size: 8pt;
  color: ${secondaryTextColor};
`

const StoryRow = props => {
  const host = getHost(props.url)
  const hours = getHoursDifferenceFromNow(props.time)
  const hoursPlural = hours !== 1 ? 's' : ''
  return (
    <Wrapper>
      <Number>{props.number}.</Number>
      <Content>
        <div>
          <Title>{props.title}</Title>
          <HostLink>({host})</HostLink>
        </div>
        <BottomSection>
          <span>
            {props.points} points by&nbsp;
            <Anchor href="#">{props.author}</Anchor>&nbsp;
            <Anchor>{hours} hour{hoursPlural} ago</Anchor>
          </span>
          <HideButton>hide</HideButton>
          <span>14 comments</span>
        </BottomSection>
      </Content>
    </Wrapper>
  )
}

StoryRow.propTypes = {
  url: PropTypes.string,
  title: PropTypes.string,
  author: PropTypes.string,
  number: PropTypes.number,
  points: PropTypes.number,
}

export default StoryRow
