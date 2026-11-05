import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

// {{APP_NAME}} — 3D/viz surface shell.
// Boundary rule: this layer RENDERS core results; it never computes the science.
// Fetch results from api/ (src/io), drive params from src/controls, render in src/scene,
// chart in src/viz. Replace the placeholder cube with the app's real scene.
export function App() {
  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas camera={{ position: [3, 3, 3] }}>
        <ambientLight intensity={0.6} />
        <directionalLight position={[5, 5, 5]} />
        <mesh>
          <boxGeometry />
          <meshStandardMaterial color="hotpink" />
        </mesh>
        <OrbitControls />
      </Canvas>
    </div>
  );
}
