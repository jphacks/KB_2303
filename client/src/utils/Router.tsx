import { lazy } from 'react'
import { Route, Routes, Navigate } from 'react-router-dom'
import { Result } from 'result-type-ts'

const HomePage = lazy(() => import('../pages/Home'))
const SignInPage = lazy(() => import('../pages/SignIn'))
const SignUpPage = lazy(() => import('../pages/SignUp'))

export const Router: React.FC<{ user: Result<boolean> }> = ({ user }) => {
  if (user.error === 'INIT') {
    throw new Promise((resolve) => {
      resolve(null)
    })
  }
  if (user.isSuccess) {
    return (
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/sign-in" element={<Navigate replace to="/" />} />
        <Route path="/sign-up" element={<Navigate replace to="/" />} />
      </Routes>
    )
  }
  return (
    <Routes>
      <Route path="/sign-in" element={<SignInPage />} />
      <Route path="/sign-up" element={<SignUpPage />} />
      <Route path="/*" element={<Navigate replace to="/sign-in" />} />
    </Routes>
  )
}
