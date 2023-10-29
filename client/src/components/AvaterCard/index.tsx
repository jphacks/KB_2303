import React from 'react'
import {
  AvaterWrapper,
  Column,
  DateText,
  Hr,
  Name,
  ReportTitle,
  Root,
  Row,
  Text,
} from './Styles'
import { Avater } from '../Avater'

type Props = {
  name: string
  createDate: string
  selected: string
  reportCount: number
  selects: {
    title: string
    action: () => void
  }[]
}

export const AvaterCard: React.FC<Props> = ({
  name,
  createDate,
  reportCount,
  selects,
  selected,
}) => {
  return (
    <Root>
      <AvaterWrapper>
        <Avater name={name} size={108} />
      </AvaterWrapper>
      <Name>{name}</Name>
      <Row>
        <ReportTitle>レポート{reportCount}件</ReportTitle>
        <DateText>{createDate}</DateText>
      </Row>
      <Hr />
      <Column>
        {selects.map((s) => {
          return (
            <Text
              key={s.title}
              isBold={s.title === selected}
              onClick={s.action}>
              {s.title}
            </Text>
          )
        })}
      </Column>
    </Root>
  )
}
