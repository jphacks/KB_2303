import { lazy } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

const HomePage = lazy(() => import('./pages/Home'))
const SignInPage = lazy(() => import('./pages/SignIn'))
const SignUpPage = lazy(() => import('./pages/SignUp'))

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/sign-in" element={<SignInPage />} />
        <Route path="/sign-up" element={<SignUpPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
