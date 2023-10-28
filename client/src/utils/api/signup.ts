import { Config } from '../Config'

export const signup = async (name: string, email: string, password: string) => {
  const data = await fetch(`${Config.ApiEndPoint}/admin/`, {
    credentials: 'include',
    method: 'POST',
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name,
      email,
      password,
    }),
  })
  return await data.json()
}
