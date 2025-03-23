import instance from "./axiosConfig"

export async function getPasswords() {
  const res = await instance.get("/passwords")
  return res.data
}

export async function createPassword(site_name: string, encrypted_password: string) {
  await instance.post("/passwords", { site_name, encrypted_password })
}

export async function generateRandomPassword(length: number) {
  const res = await instance.get(`/passwords/generate/random?length=${length}`)
  return res.data
}
