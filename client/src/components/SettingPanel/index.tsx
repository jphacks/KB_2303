import React from 'react'
import { HeightMargin, IDView, PanelTitle, Root, SettingTitle } from './Styles'
import { signout } from '../../utils/api/signout'
import { useNavigate } from 'react-router'
import { Button } from '../Button'

type Props = {
  groupId:string
  inviteId:string
}

export const SettingPanel: React.FC<Props> = ({groupId, inviteId}) => {
  const navi = useNavigate()
  const signOut = () => {
    const result = window.confirm('本当にログアウトしますか？');
      if(result){
        signout().then(() => {
        navi('/sign-in')
      })
    }
  }
  return (
    <Root>
      <PanelTitle>グループ情報</PanelTitle>
      <SettingTitle>グループID(LINE登録用)</SettingTitle>
      <IDView>{groupId}</IDView>
      <HeightMargin/>
      <SettingTitle>インバイトID(管理者ログイン用)</SettingTitle>
      <IDView>{inviteId}</IDView>
      <HeightMargin/>
      <HeightMargin/>
      <HeightMargin/>
      <Button
        type={'Fill'}
        color={'gray'}
        label={'ログアウト'}
        onClick={signOut}
      />
    </Root>
  )
}
