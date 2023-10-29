import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  display: flex;
  gap: 40px
  align-items: center;
  margin: 24px
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

export const Wrapper = styled('div')`
  display: flex;
  flex-direction: column;
  gap: 4px;
`

export const Hr = styled('div')`
  width: 100%;
  height: 1px;
  background: ${Color.gray[300]};
`