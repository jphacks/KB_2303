import React, { Dispatch, SetStateAction } from 'react'
import { Label, Root, TextField, Error } from './Styles'

type Props = {
  placeHolder: string
  label: string
  value: string
  error?: string
  setValue: Dispatch<SetStateAction<string>>
}

export const Input: React.FC<Props> = ({
  placeHolder,
  label,
  value,
  error = '',
  setValue,
}) => {
  return (
    <Root>
      <Label>{label}</Label>
      <TextField
        type="text"
        placeholder={placeHolder}
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      {error !== '' && <Error>{error}</Error>}
    </Root>
  )
}
