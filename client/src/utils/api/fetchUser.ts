import { Config } from '../Config'

export const fetchUsers = async (id: number) => {
  const data = await fetch(`${Config.ApiEndPoint}/group/user/${id}`, {
    headers: {
      accept: 'application/json',
    },
  })
  return await data.json()
}
