import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  display: flex;
  flex-direction: column;
  align-items: start;
  padding: 24px;
`

export const PanelTitle = styled('div')`
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 20px;
  margin-top: 15px;
`

export const SettingTitle = styled('div')`
  font-size: 12px;
`

export const IDView = styled('div')`
  font-size: 28px;
  border: 1px solid ${Color.gray[850]};
  border-radius: 4px;
  padding: 4px 10px;
`

export const HeightMargin = styled('div')`
  height: 15px
`