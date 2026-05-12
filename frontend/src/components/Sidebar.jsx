import React from 'react';
import { NavLink } from 'react-router-dom';
import { Home, Users, CreditCard, CalendarCheck, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const Sidebar = () => {
  const { logout } = useAuth();

  return (
    <div className="w-64 bg-white shadow-lg h-full flex flex-col">
      <div className="p-6">
        <h2 className="text-2xl font-bold text-primary-red">Gimnasio</h2>
      </div>
      <nav className="flex-1 px-4 space-y-2">
        <NavLink to="/" className={({isActive}) => `flex items-center gap-3 p-3 rounded-lg transition-colors ${isActive ? 'bg-primary-red text-white' : 'text-gray-600 hover:bg-red-50 hover:text-primary-red'}`}>
          <Home size={20} /> Dashboard
        </NavLink>
        <NavLink to="/members" className={({isActive}) => `flex items-center gap-3 p-3 rounded-lg transition-colors ${isActive ? 'bg-primary-red text-white' : 'text-gray-600 hover:bg-red-50 hover:text-primary-red'}`}>
          <Users size={20} /> Miembros
        </NavLink>
        <NavLink to="/payments" className={({isActive}) => `flex items-center gap-3 p-3 rounded-lg transition-colors ${isActive ? 'bg-primary-red text-white' : 'text-gray-600 hover:bg-red-50 hover:text-primary-red'}`}>
          <CreditCard size={20} /> Pagos
        </NavLink>
        <NavLink to="/attendance" className={({isActive}) => `flex items-center gap-3 p-3 rounded-lg transition-colors ${isActive ? 'bg-primary-red text-white' : 'text-gray-600 hover:bg-red-50 hover:text-primary-red'}`}>
          <CalendarCheck size={20} /> Asistencia
        </NavLink>
      </nav>
      <div className="p-4 border-t">
        <button onClick={logout} className="flex items-center gap-3 p-3 w-full text-gray-600 hover:text-primary-red transition-colors">
          <LogOut size={20} /> Cerrar Sesión
        </button>
      </div>
    </div>
  );
};

export default Sidebar;
