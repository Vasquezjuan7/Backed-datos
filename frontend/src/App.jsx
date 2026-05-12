import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Layout from './components/Layout';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route element={<Layout />}>
            <Route path="/" element={<Dashboard />} />
            <Route path="/members" element={<div className="p-4 text-xl">Módulo de Miembros (En desarrollo)</div>} />
            <Route path="/payments" element={<div className="p-4 text-xl">Módulo de Pagos (En desarrollo)</div>} />
            <Route path="/attendance" element={<div className="p-4 text-xl">Módulo de Asistencia (En desarrollo)</div>} />
          </Route>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
