import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
import { login } from "../api/authApi"

function Login() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const navigate = useNavigate()

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault()
    await login(email, password)
    navigate("/dashboard")
  }

  return (
    <div className="container">
      <h2 className="title">Log In</h2>
      <form onSubmit={handleLogin} style={{ marginTop: "20px" }}>
        <div className="inline-inputs">
          <div>
            <label>Email</label>
            <input value={email} onChange={(e) => setEmail(e.target.value)} />
          </div>
          <div>
            <label>Password</label>
            <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" />
          </div>
        </div>
        <button type="submit">Log In</button>
      </form>
    </div>
  )
}

export default Login
