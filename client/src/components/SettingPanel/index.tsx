import React from 'react'
import { Root } from './Styles'
import { signout } from '../../utils/api/signout'
import { useNavigate } from 'react-router'
import { Button } from '../Button'

type Props = {}

export const SettingPanel: React.FC<Props> = ({}) => {
  const navi = useNavigate()
  const signOut = () => {
    signout().then(() => {
      navi('/sign-in')
    })
  }
  return (
    <Root>
      <Button
        type={'Fill'}
        color={'gray'}
        label={'ログアウト'}
        onClick={signOut}
      />
    </Root>
  )
}
