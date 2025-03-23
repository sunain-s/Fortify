import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
import { registerUser } from "../api/userApi"

function getPasswordStrength(password: string) {
  let score = 0
  if (password.match(/[a-z]/)) score++
  if (password.match(/[A-Z]/)) score++
  if (password.match(/[0-9]/)) score++
  if (password.match(/[^a-zA-Z0-9]/)) score++
  if (password.length >= 12) score++
  if (score <= 1) return { label: "Weak", color: "red" }
  if (score <= 3) return { label: "Medium", color: "orange" }
  return { label: "Strong", color: "green" }
}

function Signup() {
  const navigate = useNavigate()
  const [email, setEmail] = useState("")
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")
  const strength = getPasswordStrength(password)

  async function handleSignup(e: React.FormEvent) {
    e.preventDefault()
    setError("")
    try {
      await registerUser({ email, username, password })
      navigate("/login")
    } catch (err: any) {
      if (err.response && err.response.status === 422) {
        setError("Invalid input. Check your email or password requirements.")
      } else {
        setError("Error occurred during sign up.")
      }
    }
  }

  return (
    <div className="container">
      <h2 className="title">Sign Up</h2>
      {error && <div style={{ color: "red", marginTop: "10px" }}>{error}</div>}
      <form onSubmit={handleSignup} style={{ marginTop: "20px" }}>
        <label>Username</label>
        <input value={username} onChange={(e) => setUsername(e.target.value)} />
        <label>Email</label>
        <input value={email} onChange={(e) => setEmail(e.target.value)} />
        <label>Password</label>
        <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" />
        <div style={{ marginBottom: "15px", color: strength.color, fontWeight: "bold" }}>
          {password && strength.label}
        </div>
        <button type="submit">Sign Up</button>
      </form>
    </div>
  )
}

export default Signup
