import instance from "./axiosConfig"

export async function registerUser(data: { email: string; username: string; password: string }) {
  await instance.post("/users/register", data)
}

export async function getMe() {
  const res = await instance.get("/users/me")
  return res.data
}

export async function updateUser(username: string, password: string) {
  await instance.patch("/users", { username, password })
}

export async function deleteUserAccount() {
  await instance.delete("/users")
}
