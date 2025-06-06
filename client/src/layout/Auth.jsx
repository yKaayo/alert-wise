import { useState } from "react";
import { Eye, EyeOff, Mail, Lock, User, ArrowRight } from "lucide-react";
import { useChat } from "../hooks/useChat";

// API
import { getUser, createUser } from "../services/api";

// Component
import Divider from "../components/Divider";

const Auth = () => {
  const { urlApi, setUserData } = useChat();

  const [isLogin, setIsLogin] = useState(true);
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const [loginData, setLoginData] = useState({
    email: "",
    password: "",
  });
  const [login, setLogin] = useState(false);

  const [signupData, setSignupData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const handleLogin = async (e) => {
    e?.preventDefault();
    setIsLoading(true);

    try {
      const res = await getUser(loginData.email, loginData.password, urlApi);

      if (res?.login) {
        setLogin(true);
        setIsLoading(false);
        setUserData({ id: res.user_id, email: res.user_email });
        alert(res.message);
      } else if (res?.error) {
        setIsLoading(false);
        alert(res.detail);
      }
    } catch (error) {
      setIsLoading(false);
      alert("Erro na requisição: " + error.message);
    }
  };

  const handleSignup = async (e) => {
    e?.preventDefault();
    setIsLoading(true);

    try {
      const res = await createUser(
        signupData.name,
        signupData.email,
        signupData.password,
        urlApi,
      );

      if (res) {
        setIsLoading(false);
        alert(res.messages);
        switchMode();
      } else if (res?.error) {
        setIsLoading(false);
        alert(res.detail);
      }
    } catch (error) {
      setIsLoading(false);
      alert("Erro na requisição: " + error.message);
    }
  };

  const switchMode = () => {
    setIsLogin(!isLogin);
    setLoginData({ email: "", password: "" });
    setSignupData({ name: "", email: "", password: "" });
    setShowPassword(false);
  };

  return (
    <div
      className={`fixed z-[2] flex h-screen w-full items-center justify-center bg-zinc-300/30 p-4 ${login ? "hidden" : ""}`}
    >
      <div className="relative z-10 w-full max-w-md">
        {/* Card */}
        <div className="flex h-full transform flex-col justify-center rounded-3xl border border-white/20 bg-white/80 p-8 shadow-2xl backdrop-blur-xl transition-all duration-500 hover:scale-[1.02]">
          {/* Header */}
          <div className="mb-8 text-center">
            <h1 className="mb-2 bg-gradient-to-r from-gray-800 to-gray-600 bg-clip-text text-3xl font-bold text-transparent">
              {isLogin ? "Bem-vindo!" : "Criar Conta"}
            </h1>
            <p className="text-gray-500">
              {isLogin
                ? "Entre na sua conta para continuar"
                : "Preencha os dados para começar"}
            </p>
          </div>

          {/* Form */}
          <div className="space-y-6">
            {/* Name field (only for signup) */}
            {!isLogin && (
              <div className="animate-in slide-in-from-top-2 transform transition-all duration-300">
                <div className="relative">
                  <User className="absolute top-1/2 left-3 h-5 w-5 -translate-y-1/2 transform text-gray-400 transition-colors duration-200" />
                  <input
                    type="text"
                    placeholder="Nome completo"
                    value={signupData.name}
                    onChange={(e) =>
                      setSignupData({ ...signupData, name: e.target.value })
                    }
                    className="auth-input"
                    required
                  />
                </div>
              </div>
            )}

            {/* Email field */}
            <div className="transform transition-all duration-300">
              <div className="relative">
                <Mail className="absolute top-1/2 left-3 h-5 w-5 -translate-y-1/2 transform text-gray-400 transition-colors duration-200" />
                <input
                  type="email"
                  placeholder="Email"
                  value={isLogin ? loginData.email : signupData.email}
                  onChange={(e) => {
                    if (isLogin) {
                      setLoginData({ ...loginData, email: e.target.value });
                    } else {
                      setSignupData({ ...signupData, email: e.target.value });
                    }
                  }}
                  className="auth-input"
                  required
                />
              </div>
            </div>

            {/* Password field */}
            <div className="transform transition-all duration-300">
              <div className="relative">
                <Lock className="absolute top-1/2 left-3 h-5 w-5 -translate-y-1/2 transform text-gray-400 transition-colors duration-200" />
                <input
                  type={showPassword ? "text" : "password"}
                  placeholder="Senha"
                  value={isLogin ? loginData.password : signupData.password}
                  onChange={(e) => {
                    if (isLogin) {
                      setLoginData({ ...loginData, password: e.target.value });
                    } else {
                      setSignupData({
                        ...signupData,
                        password: e.target.value,
                      });
                    }
                  }}
                  className="auth-input"
                  required
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute top-1/2 right-3 -translate-y-1/2 transform text-gray-400 transition-colors duration-200 hover:text-gray-600"
                >
                  {showPassword ? (
                    <EyeOff className="h-5 w-5" />
                  ) : (
                    <Eye className="h-5 w-5" />
                  )}
                </button>
              </div>
            </div>

            {/* Submit button */}
            <button
              type="button"
              onClick={isLogin ? handleLogin : handleSignup}
              disabled={isLoading}
              className="auth-btn"
            >
              {isLoading ? (
                <div className="h-6 w-6 animate-spin rounded-full border-2 border-white border-t-transparent"></div>
              ) : (
                <>
                  <span>{isLogin ? "Entrar" : "Criar Conta"}</span>
                  <ArrowRight className="h-5 w-5 transition-transform duration-200 group-hover:translate-x-1" />
                </>
              )}
            </button>
          </div>

          <Divider />

          {/* Switch mode */}
          <div className="text-center">
            <p className="mb-4 text-gray-600">
              {isLogin ? "Não tem uma conta?" : "Já tem uma conta?"}
            </p>
            <button
              type="button"
              onClick={switchMode}
              className="transform font-semibold text-blue-600 transition-all duration-200 hover:scale-105 hover:text-blue-700 hover:underline"
            >
              {isLogin ? "Criar conta" : "Fazer login"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Auth;
