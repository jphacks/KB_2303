import React from 'react'
import { Flame, IconRooter, Root, RootText } from './Styles'
import { Icon } from '../Icon'
import { Color } from '../../utils/Color'

const LOW_MAGNITUDE = 2.0;
const ABS_NEUTRAL_BORDER = 4.0;

type Props = {
  score:number
  magnitude:number
}

function fetchCondition(score:number, magnitude:number){
  if(magnitude < LOW_MAGNITUDE) return 'neutral';
  if(score < -ABS_NEUTRAL_BORDER) return 'negative';
  if(score > ABS_NEUTRAL_BORDER) return 'positive';
  return 'neutral';
}

function fetchIconColor(condition:string){
  if(condition === 'positive') return Color.green.main;
  if(condition === 'negative') return Color.red.main;
  return Color.navy[900];
}

export const Condition: React.FC<Props> = ({score, magnitude}) => {
  const condition = fetchCondition(score, magnitude);
  const iconColor = fetchIconColor(condition);
  return (
    <Root>
      <RootText>コンディション</RootText>
      <Flame/>
      <IconRooter>
        <Icon color={iconColor} size={80}>
          {condition}
        </Icon>
      </IconRooter>
    </Root>
  )
}
