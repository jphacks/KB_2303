import type { Meta, StoryObj } from '@storybook/react'

import { Input } from './'

const meta = {
  title: 'Components/Input',
  component: Input,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {},
} satisfies Meta<typeof Input>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    value: '',
    label: 'ラベル',
    placeHolder: '入力してください',
    type: 'text',
  },
}
export const Inputed: Story = {
  args: {
    value: '入力しました',
    label: '名前',
    placeHolder: '',
    type: 'text',
  },
}
export const Password: Story = {
  args: {
    value: '入力しました',
    label: 'パスワード',
    placeHolder: '',
    type: 'password',
  },
}
export const Error: Story = {
  args: {
    value: '',
    label: '名前',
    placeHolder: '名前を入力してください',
    error: '名前が入力されていません。',
    type: 'text',
  },
}
