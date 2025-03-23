import React, { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"
import { getPasswords, createPassword, generateRandomPassword } from "../api/passwordApi"

function Dashboard() {
  const [passwords, setPasswords] = useState<any[]>([])
  const [siteName, setSiteName] = useState("")
  const [rawPassword, setRawPassword] = useState("")
  const [generated, setGenerated] = useState("")
  const [error, setError] = useState("")
  const navigate = useNavigate()

  async function loadPasswords() {
    try {
      const data = await getPasswords()
      setPasswords(data)
    } catch (err: any) {
      if (err.response && err.response.status === 401) {
        setError("You are not authorized. Please log in first.")
        navigate("/login")
      } else {
        setError("Could not fetch passwords.")
      }
    }
  }

  async function handleCreate() {
    if (!siteName || !rawPassword) return
    try {
      await createPassword(siteName, rawPassword)
      setSiteName("")
      setRawPassword("")
      loadPasswords()
    } catch (e) {
      setError("Failed to create password.")
    }
  }

  async function handleGenerate() {
    try {
      const result = await generateRandomPassword(12)
      setGenerated(result.generated_password)
    } catch (e) {
      setError("Failed to generate password.")
    }
  }

  useEffect(() => {
    loadPasswords()
  }, [])

  return (
    <div className="container">
      <h2 className="title">Dashboard</h2>
      <p style={{ marginTop: "20px", fontSize: "1.1rem" }}>
        This is your personal password vault. Below is a list of your saved passwords. Use the form to add
        a new password by specifying the site or service name (e.g., "gmail.com") and the password itself.
        You can also generate a random password.
      </p>
      {error && <div style={{ color: "red", marginTop: "20px" }}>{error}</div>}
      <div style={{ marginTop: "20px" }}>
        {passwords.map((p) => (
          <div
            key={p.id}
            style={{
              marginBottom: "10px",
              border: "1px solid #ccc",
              padding: "10px",
              backgroundColor: "#fff"
            }}
          >
            <div>Site: {p.site_name}</div>
            <div>Password: {p.encrypted_password}</div>
          </div>
        ))}
      </div>
      <div style={{ marginTop: "30px" }}>
        <label>Site Name</label>
        <input value={siteName} onChange={(e) => setSiteName(e.target.value)} />
        <label>Password</label>
        <input value={rawPassword} onChange={(e) => setRawPassword(e.target.value)} />
        <button onClick={handleCreate}>Add</button>
      </div>
      <div style={{ marginTop: "40px" }}>
        <h3>Password Generator</h3>
        <button onClick={handleGenerate}>Generate Random Password</button>
        <div style={{ marginTop: "10px", fontSize: "1rem", fontWeight: "bold" }}>
          {generated}
        </div>
      </div>
    </div>
  )
}

export default Dashboard
