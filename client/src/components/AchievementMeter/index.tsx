import React from 'react'
import { Flame, Meter, MeterText, Root, RootText, RootTextBack } from './Styles'

type Props = {
  par: number
}

export const AchievementMeter: React.FC<Props> = ({par}) => {
  const titleStr:string = "目標達成率";
  return (
    <Root>
      <RootText>{titleStr}</RootText>
      <RootTextBack>{titleStr}</RootTextBack>
      <Flame/>
      <Meter par={par}></Meter>
      <MeterText>{par}%</MeterText>
    </Root>
  )
}
