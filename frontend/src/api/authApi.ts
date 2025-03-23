import instance from "./axiosConfig"

export async function login(email: string, password: string) {
  await instance.post("/auth/login", { email, password })
}

export async function logout() {
  await instance.post("/auth/logout")
}

export async function refreshToken(refresh_token: string) {
  await instance.post("/auth/refresh", { refresh_token })
}
