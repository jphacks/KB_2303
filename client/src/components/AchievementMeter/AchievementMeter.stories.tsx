import type { Meta, StoryObj } from '@storybook/react'

import { AchievementMeter } from '.';


const meta = {
  title: 'Components/AchievementMeter',
  component: AchievementMeter,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
} satisfies Meta<typeof AchievementMeter>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    par: 70
  },
}

export const Max: Story = {
  args: {
    par: 100
  },
}

export const Low: Story = {
  args: {
    par: 39
  },
}

export const Border: Story = {
  args: {
    par: 40
  },
}

export const Min: Story = {
  args: {
    par: 0
  },
}
