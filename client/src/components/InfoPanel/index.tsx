import React from 'react'
import { InfoText, InfoTitle, Root } from './Styles'

type Props = {

}

export const InfoPanel: React.FC<Props> = ({}) => {
  return (
    <Root>
      <InfoTitle>アプリバージョン</InfoTitle>
      <InfoText>v0.0.1</InfoText>
      <InfoTitle>使用技術</InfoTitle>
      <InfoText>React / FastAPI / PostgreSQL / LINEBot(LINE Messaging API SDK for Python) / ChatGPT API
      </InfoText>
      <InfoTitle>コピーライト</InfoTitle>
      <InfoText>©︎ 2023 This code</InfoText>
    </Root>
  )
}
