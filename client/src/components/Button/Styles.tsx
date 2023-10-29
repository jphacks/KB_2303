import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Fill = styled('button')<{
  backgroundColor: string
  activeColor: string
}>`
  padding: 14px 24px;
  border-radius: 5px;
  color: ${Color.white};
  background: ${({ backgroundColor }) => backgroundColor};
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border: none;
  &:active {
    background: ${({ activeColor }) => activeColor};
  }
`
export const Outline = styled('button')<{
  textColor: string
  activeColor: string
}>`
  padding: 14px 24px;
  border-radius: 5px;
  border: 1px solid ${({ textColor }) => textColor};
  color: ${({ textColor }) => textColor};
  background: ${Color.white};
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  &:active {
    background: ${Color.gray[150]};
  }
`
export const DisabledFill = styled('button')`
  padding: 14px 24px;
  border-radius: 5px;
  color: ${Color.white};
  background: ${Color.gray[250]};
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: not-allowed;
  border: none;
`
export const DisabledOutline = styled('button')`
  padding: 14px 24px;
  border-radius: 5px;
  border: 1px solid ${Color.gray[250]};
  border-radius: 5px;
  background: ${Color.white};
  color: ${Color.gray[250]};
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: not-allowed;
`