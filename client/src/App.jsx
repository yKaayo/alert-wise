import { Loader } from "@react-three/drei";
import { Leva } from "leva";
import Home from "./layout/Home";

const App = () => {
  return (
    <>
      <Loader />
      <Leva hidden />
      <Home />
    </>
  );
};

export default App;
