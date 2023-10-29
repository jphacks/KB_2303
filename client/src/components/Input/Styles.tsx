import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const TextField = styled('input')<{ isError: boolean }>`
  width: 200px;
  height: 32px;
  border: none;
  border-bottom: 1px solid
    ${({ isError }) => (isError ? Color.red.main : Color.black)};
  padding: 4px;
  background: transparent;
  outline: none;
  &:focus {
    border-bottom: 1px solid
      ${({ isError }) => (isError ? Color.red.main : Color.green.main)};
  }
`
export const Root = styled('div')`
  display: flex;
  flex-direction: column;
  margin: 8px;
`

export const Label = styled('div')`
  font-size: 10px;
`
export const Error = styled('div')`
  font-size: 12px;
  margin-top: 4px;
  color: red;
`
