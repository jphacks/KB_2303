import type { Meta, StoryObj } from '@storybook/react'

import { UserInfoPanel } from './';


const meta = {
  title: 'Components/UserInfoPanel',
  component: UserInfoPanel,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
} satisfies Meta<typeof UserInfoPanel>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    user: {
      name: 'いなたつ',
      id: '1',
      joined_at: new Date(),
    },
  },
}
