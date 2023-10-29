import { Config } from '../Config'

export const fetchUsers = async (id: string) => {
  const data = await fetch(`${Config.ApiEndPoint}/group/user/${id}`, {
    credentials: 'include',
    headers: {
      accept: 'application/json',
    },
  })
  return await data.json()
}
