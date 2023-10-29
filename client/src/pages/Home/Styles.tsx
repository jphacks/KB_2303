import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
`

export const UserListWrapper = styled('div')`
  width: 240px;
  height: 100vh;
`
export const PanelWrapper = styled('div')`
  flex-grow: 1;
  height: 100vh;
`
export const Hr = styled('div')`
  width: 1px;
  height: 100vh;
  background: ${Color.gray[300]};
`
export const Center = styled('div')`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
  justify-content: center;
`

export const Text = styled('div')`
  font-size: 16px;
  color: ${Color.gray[900]};
`