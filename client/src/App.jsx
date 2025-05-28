import { Loader } from "@react-three/drei";
import { Leva } from "leva";
import Home from "./layout/Home";
import Pao from "./layout/Pao";

const App = () => {
  return (
    <>
      <Loader />
      <Leva hidden />
      <Home />
      <Pao />
    </>
  );
};

export default App;
