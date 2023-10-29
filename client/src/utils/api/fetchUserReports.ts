import { Report } from '../../models/Report'
const sleep = (ms: number) => {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

export const fetchUserReports = async (id: string) => {
  await sleep(100)
  const report: Report = {
    target: 'target',
    scheduled_hearing_date: new Date(),
    id: id,
    user_id: 'user_id',
    no: 1,
    emotion_score: 0.2,
    emotion_magnitude: 0.6,
    impression: 'impression',
    impression_feedback: 'impression_feedback',
    achieved_score: 100,
    reason: 'reason',
    reason_feedback: 'reason_feedback',
    problem: 'problem',
    problem_feedback: 'problem_feedback',
    hearing_date: new Date(),
    created_at: new Date(),
    updated_at: new Date(),
  }
  return report
}
