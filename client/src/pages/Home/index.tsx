import { useNavigate } from 'react-router'
import { Button } from '../../components/Button'
import { signout } from '../../utils/api/signout'
import { Root } from './Styles'
import { useEffect, useState } from 'react'
import { fetchGroup } from '../../utils/api/fetchGroup'
import { fetchGroupUsers } from '../../utils/api/fetchGroupUsers'
import { Result } from 'result-type-ts'
import { Group } from '../../models/Group'
import { GroupUser } from '../../models/GroupUser'

const Page: React.FC = () => {
  const navi = useNavigate()

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
      const d = data.map((u: any) => {
        return {
          id: u.id,
          name: u.name,
          email: u.email,
          updated_at: u.updated_at,
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

  return (
    <Root>
      HOME
      <Button
        type={'Fill'}
        color={'green'}
        label={'SIGN OUT'}
        onClick={signOut}
      />
    </Root>
  )
}

export default Page
