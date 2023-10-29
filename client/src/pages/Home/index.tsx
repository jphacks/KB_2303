import { useNavigate } from 'react-router'
import { signout } from '../../utils/api/signout'
import { Center, Hr, PanelWrapper, Root, UserListWrapper, Text } from './Styles'
import { useEffect, useState } from 'react'
import { fetchGroup } from '../../utils/api/fetchGroup'
import { fetchGroupUsers } from '../../utils/api/fetchGroupUsers'
import { Result } from 'result-type-ts'
import { Group } from '../../models/Group'
import { GroupUser } from '../../models/GroupUser'
import { Navigater } from '../../components/Navigater'
import { IllustImage } from '../../components/IllustImage'

const Page: React.FC = () => {
  const navi = useNavigate()

  const [userInfo, setUserInfo] = useState<GroupUser | null>(null)
  const [group, setGroup] = useState<Result<Group>>(Result.failure('INIT'))
  const [groupUsers, setGroupUsers] = useState<Result<GroupUser[]>>(
    Result.failure('INIT')
  )

  const signOut = () => {
    signout().then(() => {
      navi('/sign-in')
    })
  }

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
      action: () => console.log('user'),
    },
    {
      icon: 'setting',
      action: () => console.log('setting'),
    },
    {
      icon: 'info',
      action: () => console.log('info'),
    },
  ]

  return (
    <Root>
      <Navigater navigations={navigations} />
      <UserListWrapper></UserListWrapper>
      <Hr />
      <PanelWrapper>
        {userInfo === null && (
          <Center>
            <IllustImage type={'EmptyInfo'} />
            <Text>受講者の情報が確認できます</Text>
          </Center>
        )}
        {userInfo !== null && (
          <Center>
            <Text>受講者の情報をここに表示</Text>
          </Center>
        )}
      </PanelWrapper>
    </Root>
  )
}

export default Page
