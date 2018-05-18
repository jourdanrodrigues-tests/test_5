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

const Anchor = styled.a`
  color: inherit;
  cursor: pointer;
  text-decoration: none;
  
  &:hover {
    text-decoration: underline;
  }
`

const HideButton = styled(Anchor)`
  display: flex;
  
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

const HostLink = styled(Anchor)`
  font-size: 9pt;
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

  const {comments} = props
  const commentsPlural = comments !== 1 ? 's' : ''

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
          <Anchor>{comments} comment{commentsPlural}</Anchor>
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
  comments: PropTypes.number,
}

export default StoryRow
