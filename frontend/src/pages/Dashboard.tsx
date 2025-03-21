import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

const Dashboard = () => {
    const { user, logout } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (!user) {
            navigate('/login');
        }
    }, [user, navigate]);

    return (
        <div>
            <h1>Dashboard</h1>
            <p>Welcome, {user?.username}!</p>
            <button onClick={logout}>Logout</button>
        </div>
    );
};

export default Dashboard;
