import React, { Dispatch, SetStateAction } from 'react'
import { Label, Root, TextField, Error } from './Styles'

type Props = {
  placeHolder: string
  label: string
  value: string
  error?: string
  type: 'text' | 'password'
  setValue: Dispatch<SetStateAction<string>>
}

export const Input: React.FC<Props> = ({
  placeHolder,
  label,
  value,
  error = '',
  type,
  setValue,
}) => {
  return (
    <Root>
      <Label>{label}</Label>
      <TextField
        type={type}
        placeholder={placeHolder}
        value={value}
        isError={error !== ''}
        onChange={(e) => setValue(e.target.value)}
      />
      {error !== '' && <Error>{error}</Error>}
    </Root>
  )
}
