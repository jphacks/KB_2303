import { Suspense, useEffect, useState } from 'react'
import { BrowserRouter } from 'react-router-dom'
import { Router } from './utils/Router'
import { Result } from 'result-type-ts'
import { Config } from './utils/Config'
import { Grid } from 'react-loader-spinner'
import styled from '@emotion/styled'
import { Color } from './utils/Color'
import { loginCheck } from './utils/api/loginCheck'

function App() {
  const [user, setUser] = useState<Result<boolean>>(Result.failure('INIT'))

  const sleep = (ms: number) => {
    return new Promise((resolve) => setTimeout(resolve, ms))
  }

  useEffect(() => {
    sleep(500).then(() => {
      loginCheck()
        .then((data) => {
          if (data === null) {
            setUser(Result.failure('NULL'))
          } else {
            setUser(Result.success(true))
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
      <BrowserRouter>
        <Router user={user} />
      </BrowserRouter>
    </Suspense>
  )
}

export default App

const Center = styled('div')`
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`
