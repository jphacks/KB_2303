import { Config } from '../Config'

export const changePassword = async (
  name: string,
  email: string,
  password: string,
  new_password: string
) => {
  const data = await fetch(`${Config.ApiEndPoint}/admin/`, {
    method: 'PATCH',
    credentials: 'include',
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name,
      email,
      password,
      new_password,
    }),
  })
  return await data.json()
}
