import type { Meta, StoryObj } from '@storybook/react'

import { Button } from './'

const meta = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
} satisfies Meta<typeof Button>

export default meta
type Story = StoryObj<typeof meta>

const mockFn = () => console.log('clicked')

export const FillGreen: Story = {
  args: {
    color: 'green',
    type: 'Fill',
    label: 'Submit',
    onClick: mockFn,
  },
}
export const OutlineGreen: Story = {
  args: {
    color: 'green',
    type: 'Outline',
    label: 'Submit',
    onClick: mockFn,
  },
}
export const FillRed: Story = {
  args: {
    color: 'red',
    type: 'Fill',
    label: 'Submit',
    onClick: mockFn,
  },
}
export const OutlineRed: Story = {
  args: {
    color: 'red',
    type: 'Outline',
    label: 'Submit',
    onClick: mockFn,
  },
}
export const Gray: Story = {
  args: {
    color: 'gray',
    type: 'Fill',
    label: 'Submit',
    onClick: mockFn,
  },
}
export const DisabledFill: Story = {
  args: {
    color: 'gray',
    type: 'Fill',
    label: 'Submit',
    disabled: true,
    onClick: mockFn,
  },
}
export const DisabledOutline: Story = {
  args: {
    color: 'gray',
    type: 'Outline',
    label: 'Submit',
    disabled: true,
    onClick: mockFn,
  },
}
