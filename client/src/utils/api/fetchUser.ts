import { Config } from '../Config'

export const fetchUsers = async (id: string) => {
  const data = await fetch(`${Config.ApiEndPoint}/user/${id}`, {
    credentials: 'include',
    headers: {
      accept: 'application/json',
    },
  })
  const json = await data.json()
  return json.map((d: any) => {
    return {
      ...d,
      achieved_score: d.achieved_score === null ? 0 : d.achieved_score,
    }
  })
}
