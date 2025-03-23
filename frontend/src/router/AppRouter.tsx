import React from "react"
import { Routes, Route } from "react-router-dom"
import Navbar from "../components/Shared/Navbar"
import Home from "../pages/Home"
import Signup from "../pages/Signup"
import Login from "../pages/Login"
import Dashboard from "../pages/Dashboard"
import Profile from "../pages/Profile"

function AppRouter() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </>
  )
}

export default AppRouter
