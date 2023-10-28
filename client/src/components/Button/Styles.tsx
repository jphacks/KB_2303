import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Fill = styled('div')`
  width: 100px;
  height: 32px;
  border-radius: 8px;
  color: ${Color.white};
  background: ${({ color }) => color};
  display: flex;
  justify-content: center;
  align-items: center;
`