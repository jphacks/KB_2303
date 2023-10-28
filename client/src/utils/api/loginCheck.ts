import { Config } from '../Config'

export const loginCheck = async () => {
  const data = await fetch(`${Config.ApiEndPoint}/admin/`, {
    credentials: 'include',
    headers: {
      accept: 'application/json',
    },
  })
  return await data.json()
}
