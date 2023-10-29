import type { Meta, StoryObj } from '@storybook/react'

import { AvaterCard } from '.'

const meta = {
  title: 'Components/AvaterCard',
  component: AvaterCard,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {},
} satisfies Meta<typeof AvaterCard>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    name: 'inatatsu',
    createDate: '2023/10/25~',
    selected: 'レポート',
    selects: [
      { title: 'レポート', action: () => '' },
      { title: 'リクエスト', action: () => '' },
    ],
  },
}
