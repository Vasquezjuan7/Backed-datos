import React from 'react';
import { Users, CreditCard, Activity } from 'lucide-react';

const DashboardCard = ({ title, value, icon: Icon }) => (
  <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex items-center justify-between">
    <div>
      <p className="text-gray-500 mb-1">{title}</p>
      <h3 className="text-2xl font-bold text-gray-900">{value}</h3>
    </div>
    <div className="bg-red-50 p-4 rounded-full text-primary-red">
      <Icon size={24} />
    </div>
  </div>
);

const Dashboard = () => {
  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <DashboardCard title="Miembros Activos" value="150" icon={Users} />
        <DashboardCard title="Ingresos del Mes" value="$3,500" icon={CreditCard} />
        <DashboardCard title="Asistencias Hoy" value="45" icon={Activity} />
      </div>
    </div>
  );
};

export default Dashboard;
