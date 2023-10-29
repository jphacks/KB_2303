import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  width: 320px;
  height: 430px;
  border-radius: 16px;
  box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.25);
`

export const AvaterWrapper = styled('div')`
  padding-top: 32px;
  padding-left: 24px;
  padding-bottom: 40px;
`

export const Name = styled('div')`
  color: ${Color.gray[900]};
  font-size: 40px;
  padding-left: 24px;
`
export const Row = styled('div')`
  padding: 0px 24px;
  margin-top: 8px;
  display: flex;
  justify-content: space-between;
`

export const ReportTitle = styled('div')`
  color: ${Color.gray[900]};
  font-size: 16px;
`
export const DateText = styled('div')`
  color: ${Color.gray[400]};
  font-size: 16px;
`

export const Hr = styled('div')`
  width: 100%;
  height: 1px;
  background: ${Color.gray[300]};
  margin-top: 32px;
`

export const Column = styled('div')`
  margin-top: 32px;
`

export const Text = styled('div')<{ isBold: boolean }>`
  font-size: 24px;
  margin-left: 24px;
  color: ${Color.gray[900]};
  font-weight: ${({ isBold }) => (isBold ? 'Regular' : 'Bold')};
`
