import React, { useEffect, useState } from 'react'
import { Center, Hr, Root, Text, Wrapper } from './Styles'
import { GroupUser } from '../../models/GroupUser'
import { AvaterCard } from '../AvaterCard'
import { IllustImage } from '../IllustImage'
import { ReportView } from '../ReportView'
import { Report } from '../../models/Report'
import { fetchUsers } from '../../utils/api/fetchUser'

type Props = {
  user: GroupUser
}

export const UserInfoPanel: React.FC<Props> = ({ user }) => {
  const [select, setSelect] = useState<'レポート' | 'リクエスト'>('レポート')

  const [reports, setReports] = useState<Report[]>([])

  useEffect(() => {
    console.log('fetch user', user.id)
    fetchUsers(user.id).then((data) => {
      console.log('user', data)
      setReports(data.reports)
    })
  }, [user])
  return (
    <Root>
      <AvaterCard
        name={user.name}
        createDate={user.joined_at.toLocaleDateString()}
        selected={select}
        selects={[
          {
            title: 'report',
            action: () => setSelect('レポート'),
          },
          {
            title: 'request',
            action: () => setSelect('リクエスト'),
          },
        ]}
      />
      {reports.length === 0 ? (
        <Center>
          <IllustImage type={'EmptyInfo'} />
          <Text>まだレポートがありません。</Text>
        </Center>
      ) : (
        <Wrapper>
          {reports.map((r, i) => {
            if (i === 0) {
              return (
                <ReportView report={r} ownerName={user.name} prevTarget="-" />
              )
            } else {
              return (
                <ReportView
                  report={r}
                  ownerName={user.name}
                  prevTarget={reports[i - 1].target}
                />
              )
            }
          })}
          {reports.map((_, i) => {
            if (i === reports.length) {
              return null
            } else {
              return <Hr />
            }
          })}
        </Wrapper>
      )}
    </Root>
  )
}
