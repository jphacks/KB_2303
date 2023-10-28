import type { Meta, StoryObj } from '@storybook/react'

import { Icon } from './';
import { Color } from '../../utils/Color'

const meta = {
  title: 'Components/Icon',
  component: Icon,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {},
} satisfies Meta<typeof Icon>

export default meta
type Story = StoryObj<typeof meta>

export const User: Story = {
  args: {
    children: 'user',
    color: Color.green.main,
    size: 24,
  },
}
export const Group: Story = {
  args: {
    children: 'group',
    color: Color.green.main,
    size: 24,
  },
}
export const Setting: Story = {
  args: {
    children: 'setting',
    color: Color.green.main,
    size: 24,
  },
}
export const NegativeFace: Story = {
  args: {
    children: 'negative',
    color: Color.green.main,
    size: 24,
  },
}
export const NeutralFace: Story = {
  args: {
    children: 'neutral',
    color: Color.green.main,
    size: 24,
  },
}
export const PositiveFace: Story = {
  args: {
    children: 'positive',
    color: Color.green.main,
    size: 24,
  },
}

export const Big: Story = {
  args: {
    children: 'setting',
    color: Color.green.main,
    size: 80,
  },
}