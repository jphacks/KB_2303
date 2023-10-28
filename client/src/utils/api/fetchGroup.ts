import { Config } from '../Config'

export const fetchGroup = async () => {
  const data = await fetch(`${Config.ApiEndPoint}/group/`, {
    headers: {
      accept: 'application/json',
    },
  })
  return await data.json()
}
