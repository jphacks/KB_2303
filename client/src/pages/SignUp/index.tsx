import { useState } from 'react'
import { Input } from '../../components/Input'
import { Root } from './Styles'
import { Button } from '../../components/Button'
import { useNavigate } from 'react-router'
import { signup } from '../../utils/api/signup'
import { createGroup } from '../../utils/api/createGroup'
import { joinGroup } from '../../utils/api/joinGroup'

const Page: React.FC = () => {
  const [step, setStep] = useState(1)
  const [groupCode, setGroupCode] = useState('')
  const [groupName, setGroupName] = useState('')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navi = useNavigate()
  const signUp = () => {
    signup(name, email, password).then(() => {
      if (groupCode === '') {
        createGroup(groupName).then(() => {
          console.log('create group')
          navi('/')
        })
      } else {
        joinGroup(groupCode).then(() => {
          console.log('join group')
          navi('/')
        })
      }
    })
  }

  if (step === 2) {
    return (
      <Root>
        <Input
          placeHolder={'plese input invite code'}
          label={'invite code'}
          value={groupCode}
          setValue={setGroupCode}
          type={'text'}
        />
        <div>OR</div>
        <Input
          placeHolder={'plese input group name'}
          label={'group name'}
          value={groupName}
          setValue={setGroupName}
          type={'text'}
        />
        <Button
          type={'Fill'}
          color={'green'}
          label={'SIGN-UP'}
          onClick={signUp}
        />
      </Root>
    )
  }
  return (
    <Root>
      <Input
        placeHolder={'plese input name'}
        label={'name'}
        value={name}
        setValue={setName}
        type={'text'}
      />
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
        label={'NEXT'}
        onClick={() => setStep(2)}
      />
    </Root>
  )
}

export default Page
