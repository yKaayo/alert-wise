export async function getUser(email, password, urlApi) {
  const res = await fetch(`${urlApi}/entrar`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  const data = await res.json();

  if (!res.ok) {
    return { error: true, detail: data.detail };
  }

  return data;
}

export async function createUser(name, email, password, urlApi) {
  const res = await fetch(`${urlApi}/cadastrar`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, password }),
  });

  const data = await res.json();

  if (!res.ok) {
    return { error: true, detail: data.detail };
  }

  return data;
}
