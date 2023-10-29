import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  display: flex;
  justify-content: center;
  align-items: center;
`

export const UserView = styled('div')<{ isSelected: boolean }>`
  display: flex;
  justify-content: start;
  align-items: center;
  width: 240px;
  background: ${({ isSelected }) =>
    isSelected ? Color.gray[200] : 'transparent'};
  &:hover {
    background: ${({ isSelected }) =>
      isSelected ? Color.gray[200] : Color.gray[300]};
  }
`

export const UserListView = styled('div')`
  height: 100vh;
`

export const IconView = styled('div')`
  width: 24px;
  height: 24px;
  margin: 8px 12px;
`

export const NameView = styled('div')`
  display: flex;
  align-items: center;
  justify-content: start;
  font-size: 16px;
  color: ${Color.gray[850]};
`

export const DateView = styled('div')`
  display: flex;
  justify-content: end;
  align-items: start;
  font-size: 8px;
  color: ${Color.gray[400]};
  height: 40px;
  margin-right: 4px;
  flex-grow: 1;
`


