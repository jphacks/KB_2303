import type { Meta, StoryObj } from '@storybook/react'

import { ReportView } from './'

const meta = {
  title: 'Components/ReportView',
  component: ReportView,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {},
} satisfies Meta<typeof ReportView>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    ownerName: 'いなたつ',
    prevTarget: '生き延びること',
    report: {
      target: 'target',
      scheduled_hearing_date: new Date(),
      id: '1',
      user_id: 'user_id',
      no: 1,
      emotion_score: 0.2,
      emotion_magnitude: 0.6,
      impression: 'impression',
      impression_feedback: 'impression_feedback',
      archived_score: 100,
      reason: 'reason',
      reason_feedback: 'reason_feedback',
      problem: 'problem',
      problem_feedback: 'problem_feedback',
      hearing_date: new Date(),
      created_at: new Date(),
      updated_at: new Date(),
    },
  },
}
