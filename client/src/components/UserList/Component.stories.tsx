import type { Meta, StoryObj } from '@storybook/react'

import { UserList } from './';


const meta = {
  title: 'Components/UserList',
  component: UserList,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
} satisfies Meta<typeof UserList>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    userListViewInfo:[{
      name:"いょむ",
      date: new Date(),
      action: () => console.log('いょむ clicked')
    }]
    
  }
}
