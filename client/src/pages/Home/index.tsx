import { Center, Hr, PanelWrapper, Root, UserListWrapper, Text } from './Styles'
import { useEffect, useState } from 'react'
import { fetchGroup } from '../../utils/api/fetchGroup'
import { fetchGroupUsers } from '../../utils/api/fetchGroupUsers'
import { Result } from 'result-type-ts'
import { Group } from '../../models/Group'
import { GroupUser } from '../../models/GroupUser'
import { Navigater } from '../../components/Navigater'
import { IllustImage } from '../../components/IllustImage'
import { SettingPanel } from '../../components/SettingPanel'
import { InfoPanel } from '../../components/InfoPanel'
import { UserList } from '../../components/UserList'

const Page: React.FC = () => {
  const [panelType, setPanelType] = useState<'users' | 'setting' | 'info'>(
    'users'
  )

  const [userInfo, setUserInfo] = useState<GroupUser | null>(null)
  const [group, setGroup] = useState<Result<Group>>(Result.failure('INIT'))
  const [groupUsers, setGroupUsers] = useState<Result<GroupUser[]>>(
    Result.failure('INIT')
  )

  useEffect(() => {
    fetchGroup().then((data) => {
      console.log('group', data)
      const g = {
        id: data.id,
        name: data.name,
        user_invite_token: data.user_invite_token,
        admin_invite_token: data.admin_invite_token,
        created_at: data.created_at,
      }
      setGroup(Result.success(g))
    })
    fetchGroupUsers().then((data) => {
      console.log('group users', data)
      const d = data.map((u: any) => {
        return {
          id: u.id,
          name: u.name,
          joined_at: u.joined_at,
        }
      })
      setGroupUsers(d)
    })
  }, [])

  if (group.isFailure) {
    return <div>GROUP GET FAILER</div>
  }
  if (groupUsers.isFailure) {
    return <div>GROUP USERS GET FAILER</div>
  }

  const navigations = [
    {
      icon: 'user',
      action: () => setPanelType('users'),
    },
    {
      icon: 'setting',
      action: () => setPanelType('setting'),
    },
    {
      icon: 'info',
      action: () => setPanelType('info'),
    },
  ]

  const userListViewInfo = groupUsers.value.map((u, i) => {
    return {
      name: u.name,
      date: u.joined_at,
      action: () => {
        setUserInfo(groupUsers.value[i])
      },
    }
  })

  return (
    <Root>
      <Navigater navigations={navigations} />
      <UserListWrapper>
        <UserList
          userListViewInfo={userListViewInfo}
          selectedItem={`${userInfo?.name}`}
        />
      </UserListWrapper>
      <Hr />
      <PanelWrapper>
        {panelType === 'setting' && <SettingPanel />}
        {panelType === 'info' && <InfoPanel />}

        {panelType === 'users' && userInfo === null && (
          <Center>
            <IllustImage type={'EmptyInfo'} />
            <Text>受講者の情報が確認できます</Text>
          </Center>
        )}

        {panelType === 'users' && userInfo !== null && (
          <Center>
            <Text>受講者の情報をここに表示</Text>
          </Center>
        )}
      </PanelWrapper>
    </Root>
  )
}

export default Page
