import React, { useState } from 'react'
import { Root } from './Styles'
import { GroupUser } from '../../models/GroupUser'
import { AvaterCard } from '../AvaterCard'

type Props = {
  user: GroupUser
}

export const UserInfoPanel: React.FC<Props> = ({ user }) => {
  const [select, setSelect] = useState<'report' | 'request'>('report')
  return (
    <Root>
      <AvaterCard
        name={user.name}
        createDate={user.joined_at.toString()}
        selected={select}
        selects={[
          {
            title: 'report',
            action: () => setSelect('report'),
          },
          {
            title: 'request',
            action: () => setSelect('request'),
          },
        ]}
      />
    </Root>
  )
}
