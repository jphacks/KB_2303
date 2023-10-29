import type { Meta, StoryObj } from '@storybook/react'

import { InfoPanel } from './';


const meta = {
  title: 'Components/InfoPanel',
  component: InfoPanel,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
} satisfies Meta<typeof InfoPanel>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
  },
}
