import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  display: flex;
  gap: 40px
  align-items: center;
`

export const Center = styled('div')`
  flex-grow: 1;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`

export const Text = styled('div')`
  font-size: 16px;
  color: ${Color.gray[900]};
`