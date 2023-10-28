import React from 'react'
import Avatar from 'boring-avatars'
import { Color } from '../../utils/Color'

type Props = {
  name: string
  size: number
}

export const Avater: React.FC<Props> = ({ name, size }) => {
  return (
    <Avatar
      size={size}
      name={name}
      variant="beam"
      colors={[Color.green.active, Color.red.active, Color.navy[900]]}
    />
  )
}
