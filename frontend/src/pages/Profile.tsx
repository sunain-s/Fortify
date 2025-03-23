import React, { useState, useEffect } from "react"
import { getMe, updateUser, deleteUserAccount } from "../api/userApi"
import { useNavigate } from "react-router-dom"

function Profile() {
  const [username, setUsername] = useState("")
  const [email, setEmail] = useState("")
  const [newUsername, setNewUsername] = useState("")
  const [newPassword, setNewPassword] = useState("")
  const [error, setError] = useState("")
  const navigate = useNavigate()

  async function loadProfile() {
    setError("")
    try {
      const me = await getMe()
      setUsername(me.username)
      setEmail(me.email)
    } catch (err: any) {
      if (err.response && err.response.status === 401) {
        setError("You are not authorized. Please log in first.")
        navigate("/login")
      } else {
        setError("Failed to load profile.")
      }
    }
  }

  async function handleUpdate() {
    setError("")
    try {
      await updateUser(newUsername || username, newPassword)
      setNewUsername("")
      setNewPassword("")
      loadProfile()
    } catch (err) {
      setError("Failed to update user.")
    }
  }

  async function handleDelete() {
    setError("")
    try {
      await deleteUserAccount()
      navigate("/")
    } catch (err) {
      setError("Failed to delete user.")
    }
  }

  useEffect(() => {
    loadProfile()
  }, [])

  return (
    <div className="container">
      <h2 className="title">Profile</h2>
      <p style={{ marginTop: "20px", fontSize: "1.1rem" }}>
        This page displays your account details. Your current username and email appear below. 
        Enter a new username or password in the fields provided if you wish to update them. 
        You can also delete your account entirely.
      </p>
      {error && <div style={{ color: "red", marginTop: "10px" }}>{error}</div>}
      <div style={{ marginTop: "20px", fontSize: "1rem" }}>
        <div>Username: {username}</div>
        <div style={{ marginTop: "10px" }}>Email: {email}</div>
      </div>
      <div style={{ marginTop: "30px" }}>
        <label>New Username</label>
        <input
          value={newUsername}
          onChange={(e) => setNewUsername(e.target.value)}
        />
        <label>New Password</label>
        <input
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
          type="password"
        />
        <button onClick={handleUpdate}>Update</button>
      </div>
      <div style={{ marginTop: "30px" }}>
        <button onClick={handleDelete} style={{ backgroundColor: "#ff4d4f" }}>
          Delete Account
        </button>
      </div>
    </div>
  )
}

export default Profile
