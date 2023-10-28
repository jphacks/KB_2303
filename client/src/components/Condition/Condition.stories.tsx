import type { Meta, StoryObj } from '@storybook/react'

import { Condition } from '.';


const meta = {
  title: 'Components/Condition',
  component: Condition,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
} satisfies Meta<typeof Condition>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    score: 5.0,
    magnitude: 4.0
  },
}

export const Positive: Story = {
  args: {
    score: 6.0,
    magnitude: 6.0
  },
}

export const Negative: Story = {
  args: {
    score: -6.0,
    magnitude: 6.0
  },
}

export const Neutral: Story = {
  args: {
    score: -1.0,
    magnitude: 6.0
  },
}

export const LowMagnitude: Story = {
  args: {
    score: 6.0,
    magnitude: 1.0
  },
}