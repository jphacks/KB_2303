import styled from '@emotion/styled'

export const TextField = styled('input')`
  width: 200px;
  height: 32px;
  border: 1px solid black;
  border-radius: 4px;
  padding: 4px;
  background: transparent;
`
export const Root = styled('div')`
  display: flex;
  flex-direction: column;
  margin: 8px;
`

export const Label = styled('div')`
  font-size: 12px;
  margin-bottom: 8px;
`
export const Error = styled('div')`
  font-size: 12px;
  margin-top: 4px;
  color: red;
`
