import { Canvas } from "@react-three/fiber";
import { Experience } from "../components/Experience";
import { useRef } from "react";
import { useChat } from "../hooks/useChat";

const Home = () => {
  const input = useRef();

  const { chat, loading, message } = useChat();

  const sendMessage = () => {
    const text = input.current.value;
    if (!loading && !message) {
      chat(text);
      input.current.value = "";
    }
  };

  return (
    <main className="h-screen relative flex flex-col items-center">
      <div className="h-full cursor-grab">
        <Canvas shadows camera={{ position: [0, 0, 1], fov: 30 }}>
          <Experience />
        </Canvas>
      </div>

      <div className="absolute bottom-5">
        <div className="flex items-center gap-2 pointer-events-auto max-w-screen-sm w-full mx-auto">
          <input
            className="w-full placeholder:text-gray-800 placeholder:italic p-4 rounded-md bg-opacity-50 bg-white backdrop-blur-md"
            placeholder="Escreva sua mensagem..."
            ref={input}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
          />
          <button
            disabled={loading || message}
            onClick={sendMessage}
            className={`btn font-bold ${
              loading || message ? "cursor-not-allowed opacity-30" : ""
            }`}
          >
            ENVIAR
          </button>
        </div>
      </div>
    </main>
  );
};

export default Home;
