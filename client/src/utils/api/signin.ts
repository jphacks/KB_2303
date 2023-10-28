import { Config } from '../Config'

export const signin = async (email: string, password: string) => {
  const data = await fetch(`${Config.ApiEndPoint}/session/`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email,
      password,
    }),
  })
  return await data.json()
}
