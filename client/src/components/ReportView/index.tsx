import React from 'react'
import { Label, Root, Text } from './Styles'
import { Report } from '../../models/Report'
import { AchievementMeter } from '../AchievementMeter'

type Props = {
  ownerName: string
  prevTarget: string
  report: Report
}

export const ReportView: React.FC<Props> = ({
  ownerName,
  prevTarget,
  report,
}) => {
  return (
    <Root>
      <Text>
        {ownerName}さん第{report.no}回レポート
      </Text>
      <Label>
        {report.achieved_score && (
          <AchievementMeter par={report.achieved_score} />
        )}
      </Label>
      <div>
        <Label>前回の目標</Label>
        <Text>{prevTarget}</Text>
      </div>
      <div>
        <Label>所感</Label>
        <Text>{report.impression}</Text>
      </div>
      <div>
        <Label>理由</Label>
        <Text>{report.reason}</Text>
      </div>
      <div>
        <Label>困っていること</Label>
        <Text>{report.problem}</Text>
      </div>
      <div>
        <Label>次の目標</Label>
        <Text>{report.target}</Text>
      </div>
    </Root>
  )
}
