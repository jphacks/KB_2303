import type { Meta, StoryObj } from '@storybook/react'

import { Avater } from './'

const meta = {
  title: 'Components/Avater',
  component: Avater,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {},
} satisfies Meta<typeof Avater>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    name: 'Default',
    size: 64,
  },
}
