import { Color } from '../../utils/Color'
import { DisabledFill, DisabledOutline, Fill, Outline } from './Styles'

type ButtonType = 'Fill' | 'Outline'
type ButtonColor = 'green' | 'red' | 'gray'

type ButtonProps = {
  type: ButtonType
  color: ButtonColor
  label: string
  disabled?: boolean
  onClick: () => void
}

export const Button: React.FC<ButtonProps> = ({
  type,
  color,
  label,
  disabled = false,
  onClick,
}) => {
  const colors = getColors(color)

  if (disabled) {
    if (type === 'Fill') {
      return <DisabledFill>{label}</DisabledFill>
    } else {
      return <DisabledOutline>{label}</DisabledOutline>
    }
  }

  if (type === 'Outline' || color === 'gray') {
    return (
      <Outline
        type="button"
        activeColor={colors.active}
        textColor={color}
        onClick={onClick}>
        {label}
      </Outline>
    )
  }
  return (
    <Fill
      type="button"
      activeColor={colors.active}
      backgroundColor={color}
      onClick={onClick}>
      {label}
    </Fill>
  )
}

const getColors = (color: ButtonColor) => {
  if (color === 'green') {
    return {
      background: Color.green.main,
      active: Color.green.active,
    }
  } else if (color === 'red') {
    return {
      background: Color.red.main,
      active: Color.red.active,
    }
  } else {
    return {
      background: Color.gray[850],
      active: Color.gray[850],
    }
  }
}
