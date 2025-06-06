import { Loader } from "@react-three/drei";
import { Leva } from "leva";
import Home from "./layout/Home";
import Auth from "./layout/Auth";

const App = () => {
  return (
    <>
      <Loader />
      <Leva hidden />
      <Auth />
      <Home />
    </>
  );
};

export default App;
