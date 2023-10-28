import { useState } from 'react'
import { Input } from '../../components/Input'
import { Root } from './Styles'
import { Button } from '../../components/Button'
import { signin } from '../../utils/api/signin'
import { useNavigate } from 'react-router'

const Page: React.FC = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navi = useNavigate()
  const signIn = () => {
    signin(email, password).then(() => {
      navi('/')
    })
  }
  return (
    <Root>
      <Input
        placeHolder={'plese input mail address'}
        label={'mail'}
        value={email}
        setValue={setEmail}
        type={'text'}
      />
      <Input
        placeHolder={'plese input password'}
        label={'password'}
        value={password}
        setValue={setPassword}
        type={'password'}
      />
      <Button
        type={'Fill'}
        color={'green'}
        label={'SIGN-IN'}
        onClick={signIn}
      />
    </Root>
  )
}

export default Page
