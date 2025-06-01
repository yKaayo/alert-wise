import { Canvas } from "@react-three/fiber";
import { useEffect, useRef, useState } from "react";
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
  const input = useRef();

  const { chat, loading, message, urlApi } = useChat();

  console.log(message);

  const sendMessage = () => {
    const text = input.current.value;
    if (!loading && !message) {
      chat(text);
      input.current.value = "";
    }
  };

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

  useEffect(() => {
    if (animInstance.current) {
      if (loading) {
        animInstance.current.play();
      } else {
        animInstance.current.stop();
      }
    }
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

      <main className="relative flex h-screen flex-col items-center">
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
            className="absolute top-5 mx-auto px-10 text-center text-2xl text-balance text-zinc-100"
          />
        )}

        <div className="relative z-[1] h-full w-full pe-16">
          <Canvas shadows camera={{ position: [0, 0, 1], fov: 30 }}>
            <Experience />
          </Canvas>
        </div>

        <div className="absolute bottom-5 z-[1] w-full">
          <div className="pointer-events-auto mx-auto flex w-full max-w-screen-sm items-center gap-2">
            <input
              className="input"
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
    </>
  );
};

export default Home;
