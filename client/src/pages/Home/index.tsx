import { useNavigate } from 'react-router'
import { Button } from '../../components/Button'
import { signout } from '../../utils/api/signout'
import { Root } from './Styles'
import { useEffect } from 'react'
import { fetchGroup } from '../../utils/api/fetchGroup'
import { fetchGroupUsers } from '../../utils/api/fetchGroupUsers'

const Page: React.FC = () => {
  const navi = useNavigate()
  const signOut = () => {
    signout().then(() => {
      navi('/sign-in')
    })
  }

  useEffect(() => {
    fetchGroup().then(console.log)
    fetchGroupUsers().then(console.log)
  }, [])

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
