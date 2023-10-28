import React from 'react'
import { SettingIcon } from './SettingIcon'
import { UserIcon } from './UserIcon'
import { PositiveFaceIcon } from './PositiveFaceIcon'
import { NegativeFaceIcon } from './NegativeFaceIcon'
import { NeutralFaceIcon } from './NeutralFaceIcon'
import { GroupIcon } from './GroupIcon'

type IconType =
  | 'setting'
  | 'user'
  | 'group'
  | 'positive'
  | 'neutral'
  | 'negative'

type Props = {
  children: IconType | string
  color: string
  size: number
}

export const Icon: React.FC<Props> = ({ children, color, size }) => {
  if (children === 'setting') {
    return <SettingIcon color={color} size={size} />
  }
  if (children === 'user') {
    return <UserIcon color={color} size={size} />
  }
  if (children === 'group') {
    return <GroupIcon color={color} size={size} />
  }
  if (children === 'positive') {
    return <PositiveFaceIcon color={color} size={size} />
  }
  if (children === 'neutral') {
    return <NeutralFaceIcon color={color} size={size} />
  }
  if (children === 'negative') {
    return <NegativeFaceIcon color={color} size={size} />
  }
  return null
}
