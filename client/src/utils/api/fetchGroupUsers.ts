import { Config } from '../Config'

export const fetchGroupUsers = async () => {
  const data = await fetch(`${Config.ApiEndPoint}/group/users`, {
    headers: {
      accept: 'application/json',
    },
  })
  return await data.json()
}
