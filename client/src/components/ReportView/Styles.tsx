import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  display: flex;
  justify-content: center;
  flex-direction: column;
  gap: 8px;
  width: 600px;
`

export const Label = styled('div')`
  color: ${Color.gray[400]};
  font-size: 10px;
`
export const Text = styled('div')`
  color: ${Color.gray[850]};
  font-size: 16px;
`
