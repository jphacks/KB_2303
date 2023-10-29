import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  display: flex;
  justify-content: center;
  align-items: center;
`

export const UserListView = styled('div')`
  display: flex;
  justify-content: center;
  align-items: start;
  width: 240px;
`

export const UserView = styled('div')`
  width: 240px;
  height: 40;
  align-items: center;
  position: relative;
  &:hover {
    background: ${Color.gray[150]};
  }
`

export const IconView = styled('div')`
  width: 24px;
  height: 24px;
  margin: 8px 12px;
`

export const NameView = styled('div')`
  display: flex;
  align-items: center;
  position: absolute;
  font-size: 16px;
  color: ${Color.gray[850]};
  transform: translate(12px, 0);
`

export const DateView = styled('div')`
  // display: flex;
  justify-content: end;
  // align-items: end;
  font-size: 8px;
  color: ${Color.gray[400]};
  left: 100%;
  transform: translate(100%, 0);
`


