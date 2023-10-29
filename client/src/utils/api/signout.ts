import { Config } from '../Config'

export const signout = async () => {
  const data = await fetch(`${Config.ApiEndPoint}/session/`, {
    credentials: 'include',
    method: 'DELETE',
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/json',
    },
  })
  return await data.json()
}
