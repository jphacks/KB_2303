import styled from '@emotion/styled'

export const Root = styled('div')<{ backgroundColor: string }>`
  width: 100px;
  height: 32px;
  border-radius: 8px;
  background: ${({ backgroundColor }) => backgroundColor};
  display: flex;
  justify-content: center;
  align-items: center;
`
