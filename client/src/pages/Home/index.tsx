import { useNavigate } from 'react-router'
import { Button } from '../../components/Button'
import { signout } from '../../utils/api/signout'
import { Root } from './Styles'

const Page: React.FC = () => {
  const navi = useNavigate()
  const signOut = () => {
    signout().then(() => {
      navi('/sign-in')
    })
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
