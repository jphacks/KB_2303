import type { Meta, StoryObj } from '@storybook/react'

import { IllustImage } from './'

const meta = {
  title: 'Components/IllustImage',
  component: IllustImage,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {},
} satisfies Meta<typeof IllustImage>

export default meta
type Story = StoryObj<typeof meta>

export const EmptyInfo: Story = {
  args: {
    type: 'EmptyInfo',
  },
}
