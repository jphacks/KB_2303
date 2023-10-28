import { Dispatch, SetStateAction, Suspense, useEffect, useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { Router } from './utils/Router'
import { Result } from 'result-type-ts'
import { Grid } from 'react-loader-spinner'
import styled from '@emotion/styled'
import { Color } from './utils/Color'
import { loginCheck } from './utils/api/loginCheck'
import { GroupAdmin } from './models/GroupAdmin'

const sleep = (ms: number) => {
  return new Promise((resolve) => setTimeout(resolve, ms))
}
function App() {
  const [user, setUser] = useState<Result<GroupAdmin>>(Result.failure('INIT'))

  useEffect(() => {
    sleep(500).then(() => {
      loginCheck()
        .then((data) => {
          if (data === null) {
            setUser(Result.failure('NULL'))
          } else {
            setUser(
              Result.success({
                name: data.name,
                id: data.id,
                email: data.email,
                updated_at: data.update_at,
              })
            )
          }
        })
        .catch(console.error)
    })
  }, [])

  return (
    <Suspense
      fallback={
        <Center>
          <Grid
            height="80"
            width="80"
            color={Color.green.main}
            ariaLabel="grid-loading"
            radius="12.5"
            wrapperStyle={{}}
            wrapperClass=""
            visible={true}
          />
        </Center>
      }>
      <Router
        user={user}
        redirect={(to: string) => <Redirect to={to} setUser={setUser} />}
      />
    </Suspense>
  )
}

export default App

const Redirect: React.FC<{
  to: string
  setUser: Dispatch<SetStateAction<Result<GroupAdmin>>>
}> = ({ to, setUser }) => {
  const navi = useNavigate()
  useEffect(() => {
    setUser(Result.failure('INIT'))
    sleep(500).then(() => {
      loginCheck().then((data) => {
        if (data === null) {
          setUser(Result.failure('NULL'))
          navi('/sign-in')
        } else {
          setUser(
            Result.success({
              name: data.name,
              id: data.id,
              email: data.email,
              updated_at: data.update_at,
            })
          )
          navi('/')
        }
      })
    })
  }, [])

  return <Navigate replace to={to} />
}

const Center = styled('div')`
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`
