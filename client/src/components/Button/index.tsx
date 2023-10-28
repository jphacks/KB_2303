import { Fill } from './Styles'

type Props = {
  type: 'Fill' | 'Outline'
  color: 'green' | 'red' | 'gray'
  onClick: () => void
}

export const Button: React.FC<Props> = ({ type, color, onClick }) => {
  return (
    <Fill color={color} onClick={onClick}>
      BUTTON
    </Fill>
  )
}
