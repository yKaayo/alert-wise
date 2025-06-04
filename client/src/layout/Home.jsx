import { Canvas } from "@react-three/fiber";
import { useEffect, useRef } from "react";
import { useChat } from "../hooks/useChat";
import lottie from "lottie-web";
import { motion } from "framer-motion";

// Components
import { Experience } from "../components/Experience";
import BlurText from "../components/BlurText";
import Silk from "../components/Silk";

const Home = () => {
  const containerRef = useRef();
  const animInstance = useRef();
  const userPrompt = useRef();

  const { chat, loading, message, urlApi } = useChat();

  console.log(message);
  

  const choices = message?.choices;

  const audio = new Audio(`data:audio/mp3;base64,${message?.audio}`);
  audio.addEventListener("loadedmetadata", () => {});

  function sendMessage() {
    const text = userPrompt.current.value;
    if (!loading) {
      chat(text);
      userPrompt.current.value = "";
    }
  }

  function sendChoiceMessage(choice) {
    if (!loading) {
      chat(String(choice));
    }
  }

  // Lottie
  useEffect(() => {
    if (!containerRef.current) return;

    if (!animInstance.current) {
      animInstance.current = lottie.loadAnimation({
        container: containerRef.current,
        renderer: "svg",
        loop: true,
        autoplay: false,
        path: "/lottie/anim.json",
      });

      animInstance.current.addEventListener("DOMLoaded", () => {
        if (loading) {
          animInstance.current.play();
        }
      });
    }

    if (animInstance.current) {
      if (loading) {
        animInstance.current.play();
      } else {
        animInstance.current.stop();
      }
    }

    return () => {
      if (animInstance.current) {
        animInstance.current.destroy();
        animInstance.current = null;
      }
    };
  }, [loading]);

  return (
    <>
      {message?.video_url ? (
        <motion.video
          className="absolute h-full w-full object-cover"
          initial={{ opacity: 0 }}
          animate={{ opacity: 0.25 }}
          transition={{ duration: 5 }}
          autoPlay
          muted
          loop
        >
          <source src={`${urlApi}/${message.video_url}`} type="video/mp4" />
          Seu navegador não suporta o elemento de vídeo.
        </motion.video>
      ) : null}

      <div className="absolute -z-[1] h-full w-full">
        <Silk
          speed={6}
          scale={0.9}
          color="#27276d"
          noiseIntensity={1.8}
          rotation={0}
        />
      </div>

      <main className="relative flex h-dvh flex-col items-center">
        {/* Text */}
        {loading ? (
          <div
            ref={containerRef}
            className="absolute top-5 h-[20%] w-full"
          ></div>
        ) : (
          <BlurText
            text={message?.text}
            delay={120}
            animateBy="words"
            direction="top"
            className="absolute top-5 mx-auto px-10 text-2xl text-balance text-zinc-100"
          />
        )}

        {/* 3D Model */}
        <div className="relative z-[1] h-full w-full">
          <Canvas shadows camera={{ position: [0, 0, 1.2], fov: 30 }}>
            <Experience />
          </Canvas>
        </div>

        {/* Choices */}
        <div className="absolute bottom-5 z-[1] container mx-auto px-5 sm:px-0">
          <div className="flex gap-3 md:gap-5">
            {choices?.length > 0 ? (
              choices.map((choice, i) => (
                <button
                  key={i}
                  onClick={() => {
                    sendChoiceMessage(choice);
                  }}
                  className={`btn w-full font-bold ${
                    loading ? "cursor-not-allowed opacity-30" : ""
                  }`}
                >
                  {choice.toUpperCase()}
                </button>
              ))
            ) : (
              <div className="pointer-events-auto mx-auto flex w-full max-w-screen-sm items-center gap-2">
                <input
                  className="input"
                  placeholder="Escreva sua mensagem..."
                  ref={userPrompt}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") {
                      sendMessage();
                    }
                  }}
                />
                <button
                  disabled={loading}
                  onClick={sendMessage}
                  className={`btn font-bold ${
                    loading ? "cursor-not-allowed opacity-30" : ""
                  }`}
                >
                  ENVIAR
                </button>
              </div>
            )}
          </div>
        </div>
      </main>
    </>
  );
};

export default Home;
