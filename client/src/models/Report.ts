export type Report = {
  target: string
  scheduled_hearing_date: Date
  id: string
  user_id: string
  no: number
  emotion_score: number
  emotion_magnitude: number
  impression: string
  impression_feedback: string
  achieved_score: number | null
  reason: string
  reason_feedback: string
  problem: string
  problem_feedback: string
  hearing_date: Date
  created_at: Date
  updated_at: Date
}
