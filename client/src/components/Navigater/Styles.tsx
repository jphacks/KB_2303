import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  height: 100vh;
  width: 80px;
  display: flex;
  align-items: start;
  position: relative;
  background: ${Color.navy[900]};
`

export const IconList = styled('div')`
  width: 80px;
  margin-top: 8px;
`

export const NavigationIcon = styled('div')`
  width: 48px;
  height: 48px;
  margin: 16px;
`
