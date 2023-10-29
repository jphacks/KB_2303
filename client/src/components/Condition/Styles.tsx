import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  width: 100px;
  height: 100px;
  position: relative;
  display: flex;
  justify-content: center;
`

export const Flame = styled('div')`
  width: 98px;
  height: 98px;
  position: absolute;
  border: 1px solid ${Color.gray[850]};
  border-radius: 4px;
  z-index: 1;
`

export const RootText = styled('div')`
  text-align: center;
  font-size: 12px;
  color: ${Color.gray[850]};
  background-color: ${Color.white};
  position: absolute;
  transform: translate(0, -50%);
  z-index: 4;
`

export const IconRooter = styled('div')`
  height: 80px;
  position: absolute;
  top: 50%;
  transform: translate(0, -50%);
  z-index: 3;
`

