import { createContext, useContext, useState, ReactNode } from 'react';
import { User } from '../types/User';
import { loginUser, signupUser } from '../api/authApi';
import { LoginCredentials } from '../types/Auth';

interface AuthContextType {
    user: User | null;
    login: (credentials: LoginCredentials) => Promise<void>;
    signup: (credentials: LoginCredentials) => Promise<void>;
    logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
    const [user, setUser] = useState<User | null>(null);

    const login = async (credentials: LoginCredentials) => {
        try {
            const { user } = await loginUser(credentials);
            setUser(user);
            localStorage.setItem('token', user.token || '');
        } catch (error) {
            console.error('Login failed', error);
        }
    };

    const signup = async (credentials: LoginCredentials) => {
        try {
            const { user } = await signupUser(credentials);
            setUser(user);
            localStorage.setItem('token', user.token || '');
        } catch (error) {
            console.error('Signup failed', error);
        }
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem('token');
    };

    return (
        <AuthContext.Provider value={{ user, login, signup, logout }}>
        {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
};
