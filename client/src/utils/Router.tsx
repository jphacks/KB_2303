import { ReactNode, lazy } from 'react'
import { Route, Routes } from 'react-router-dom'
import { Result } from 'result-type-ts'

const HomePage = lazy(() => import('../pages/Home'))
const SignInPage = lazy(() => import('../pages/SignIn'))
const SignUpPage = lazy(() => import('../pages/SignUp'))

type Props = {
  user: Result<boolean>
  redirect: (to: string) => ReactNode
}

export const Router: React.FC<Props> = ({ user, redirect }) => {
  if (user.error === 'INIT') {
    throw new Promise((resolve) => {
      resolve(null)
    })
  }
  console.log('router')
  if (user.isSuccess) {
    return (
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/sign-in" element={redirect('/')} />
        <Route path="/sign-up" element={redirect('/')} />
      </Routes>
    )
  }
  return (
    <Routes>
      <Route path="/sign-in" element={<SignInPage />} />
      <Route path="/sign-up" element={<SignUpPage />} />
      <Route path="/*" element={redirect('/sign-in')} />
    </Routes>
  )
}

// const Redirect: React.FC<{ to: string }> = ({ to }) => {
//   const navi = useNavigate()
//   useEffect(() => {
//     loginCheck().then((data) => {
//       if (data === null) {
//         navi('/sign-in')
//       } else {
//         navi('/')
//       }
//     })
//   }, [])

//   return <Navigate replace to={to} />
// }
