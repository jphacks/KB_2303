import type { Meta, StoryObj } from '@storybook/react'

import { Button } from './'

const meta = {
  title: 'Component/Button',
  component: Button,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
    backgroundColor: { control: 'color' },
  },
} satisfies Meta<typeof Button>

export default meta
type Story = StoryObj<typeof meta>

export const Large: Story = {
  args: {
    backgroundColor: 'blue',
  },
}
