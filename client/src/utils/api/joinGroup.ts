import { Config } from '../Config'

export const joinGroup = () => {
  return fetch(`${Config.ApiEndPoint}/group/`, {
    headers: {
      accept: 'application/json',
    },
  }).then((data) => data.json())
}
