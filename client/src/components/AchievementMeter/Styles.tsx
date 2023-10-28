import styled from '@emotion/styled'
import { Color } from '../../utils/Color'

export const Root = styled('div')`
  width: 102px;
  height: 102px;
  position: relative;
  display: flex;
  justify-content: center;
`

export const RootText = styled('div')`
  text-align: center;
  font-size: 12px;
  color: ${Color.gray[850]};
  position: absolute;
  transform: translate(0, -50%);
  z-index: 4;
`

export const RootTextBack = styled('div')`
  text-align: center;
  font-size: 12px;
  font-color: ${Color.white};
  background-color: ${Color.white};
  position: absolute;
  transform: translate(0, -50%);
  z-index: 2;
`

export const Flame = styled('div')`
  width: 100px;
  height: 100px;
  position: absolute;
  border: 1px solid ${Color.gray[850]};
  border-radius: 4px;
  z-index: 1;
`

export const Meter = styled('div')<{
  par: number
}>`
  width: 100px;
  max-height: 100px;
  height: ${({ par }) => par}px;
  position: absolute;
  background: ${({ par }) => (par < 40 ? Color.red.main : Color.green.main)};
  border-radius: 3px;
  top: 100%;
  transform: translate(0, calc(-100% - 1px));
  z-index: 3;
`

export const MeterText = styled('div')`
  font-size: 32px;
  text-align: center;
  color: ${Color.gray[900]};
  width: 100px;
  position: absolute;
  border-radius: 4px;
  top: 50%;
  transform: translate(0, -50%);
  z-index: 4;
`
