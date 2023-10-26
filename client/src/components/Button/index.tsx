import { Root } from './Styles'

type Props = {
  backgroundColor: string
}

export const Button: React.FC<Props> = ({ backgroundColor }) => {
  return <Root backgroundColor={backgroundColor}>BUTTON</Root>
}
