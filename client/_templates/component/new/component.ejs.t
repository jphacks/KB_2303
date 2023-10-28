---
to: src/components/<%= h.changeCase.pascal(component_name) %>/index.tsx
---

import React from 'react'
import { Root } from './Styles'

type Props = {

}

export const <%= h.changeCase.pascal(component_name) %>: React.FC<Props> = ({}) => {
  return (
    <Root><%= h.changeCase.pascal(component_name) %> component</Root>
  )
}
