import type { Meta, StoryObj } from '@storybook/react'

import { Navigater } from './';


const meta = {
  title: 'Components/Navigater',
  component: Navigater,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
} satisfies Meta<typeof Navigater>

export default meta
type Story = StoryObj<typeof meta>

const mockFn = () => console.log('clicked')

export const Default: Story = {
  args: {
    navigations: [{
      icon: 'user',
      action: mockFn
    },{
      icon: 'setting',
      action: mockFn
    },{
      icon: 'negative',
      action: mockFn
    }]
  },
}
