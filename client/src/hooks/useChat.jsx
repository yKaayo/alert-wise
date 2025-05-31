import { useContext } from "react";
import { ChatContext } from "./ChatContext";

export const useChat = () => {
  const context = useContext(ChatContext);
  return context;
};
