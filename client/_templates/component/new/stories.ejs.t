---
to: src/components/<%= h.changeCase.pascal(component_name) %>/Component.stories.tsx
---

import type { Meta, StoryObj } from '@storybook/react'

import { <%= h.changeCase.pascal(component_name) %> } from './';


const meta = {
  title: 'Components/<%= h.changeCase.pascal(component_name) %>',
  component: <%= h.changeCase.pascal(component_name) %>,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
} satisfies Meta<typeof <%= h.changeCase.pascal(component_name) %>>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
  },
}
