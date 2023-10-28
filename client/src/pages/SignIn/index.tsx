import { useState } from 'react'
import { Input } from '../../components/Input'
import { Root } from './Styles'
import { Button } from '../../components/Button'

const apiEndPoint = 'https://api.thiscode.proj.ukwhatn.com/api'

const Page: React.FC = () => {
  const [mail, setMail] = useState('')
  const [password, setPassword] = useState('')

  const signIn = () => {
    console.log('sign-in')
    fetch(`${apiEndPoint}/session`, {
      method: 'POST',
      headers: {
        accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: 'tatsuhiro.9699+01@gmail.com',
        password: 'password',
      }),
    })
      .then((d) => d.json())
      .then((data) => console.log(data.data))
  }
  return (
    <Root>
      <Input
        placeHolder={'plese input mail address'}
        label={'mail'}
        value={mail}
        setValue={setMail}
      />
      <Input
        placeHolder={'plese input password'}
        label={'password'}
        value={password}
        setValue={setPassword}
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
