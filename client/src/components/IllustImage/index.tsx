import React from 'react'
import { EmptyInfo } from './EmptyInfo'

type IllustType = 'EmptyInfo'

type Props = {
  type: IllustType
}

export const IllustImage: React.FC<Props> = ({ type }) => {
  if (type === 'EmptyInfo') {
    return <EmptyInfo />
  }
}
