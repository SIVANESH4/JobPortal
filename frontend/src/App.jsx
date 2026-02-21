import './App.css'
import ApplyJob from './ApplyJob'
import JobList from './JobList'
import LoginPage from './LoginPage'
import RegisterPage from './RegisterPage'
import { BrowserRouter, Routes, Route } from "react-router-dom"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/register' element={<RegisterPage />} />
        <Route path='/login' element={<LoginPage />} />
        <Route path='/jobs' element={<JobList />} />
        <Route path='/apply/:jobId' element={<ApplyJob />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
