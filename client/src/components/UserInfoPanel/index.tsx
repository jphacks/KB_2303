import React, { useState } from 'react'
import { Center, Root, Text } from './Styles'
import { GroupUser } from '../../models/GroupUser'
import { AvaterCard } from '../AvaterCard'
import { IllustImage } from '../IllustImage'

type Props = {
  user: GroupUser
}

export const UserInfoPanel: React.FC<Props> = ({ user }) => {
  const [select, setSelect] = useState<'report' | 'request'>('report')
  return (
    <Root>
      <AvaterCard
        name={user.name}
        createDate={user.joined_at.toLocaleDateString()}
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
      <Center>
        <IllustImage type={'EmptyInfo'} />
        <Text>まだレポートがありません。</Text>
      </Center>
    </Root>
  )
}
