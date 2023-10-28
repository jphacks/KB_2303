import { Config } from '../Config'

export const joinGroup = (invitationCode: string) => {
  return fetch(`${Config.ApiEndPoint}/group/join/`, {
    method: 'POST',
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/json',
    },
    // body: '{\n  "admin_invite_token": " 111111"\n}',
    body: JSON.stringify({
      admin_invite_token: invitationCode,
    }),
  })
}
