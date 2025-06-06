import { createContext, useState } from "react";

const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [message, setMessage] = useState();
  const [loading, setLoading] = useState(false);
  const [userData, setUserData] = useState({ id: "", email: "" });

  // const urlApi = "http://localhost:8000";
  const urlApi = 'https://alert-wise.onrender.com'

  const chat = async (userPrompt) => {
    console.log(userPrompt);
    console.log(userData);

    setLoading(true);
    const data = await fetch(`${urlApi}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "user-id": userData.id,
        "user-email": userData.email,
      },
      body: JSON.stringify({ message: userPrompt }),
    });

    if (!data.ok) {
      const err = await data.json();
      console.error("Backend error:", err);
      setLoading(false);
      return;
    }

    const json = await data.json();
    const res = json.messages;

    setMessage(res[0]);
    setLoading(false);
  };

  const onMessagePlayed = () => {
    message;
  };

  return (
    <ChatContext.Provider
      value={{
        chat,
        urlApi,
        message,
        onMessagePlayed,
        loading,
        setUserData,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export { ChatContext };
