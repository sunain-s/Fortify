import axios from 'axios';
import { LoginCredentials, AuthResponse } from '../types/Auth';

const API_URL = 'http://localhost:8000/auth';

// For development testing only
const MOCK_MODE = true;

export const loginUser = async (credentials: LoginCredentials): Promise<AuthResponse> => {
    if (MOCK_MODE) {
        // Mock successful login with fake user data
        return {
            user: {
                id: "test-user-123",
                username: credentials.email.split('@')[0], // Use part of email as username
                email: credentials.email,
                token: "mock-token-xyz"
            },
            token: "mock-token-xyz"
        };
    }
    
    // Real implementation for when backend is ready
    const response = await axios.post<AuthResponse>(`${API_URL}/login`, credentials);
    return response.data;
};

export const signupUser = async (credentials: LoginCredentials): Promise<AuthResponse> => {
    if (MOCK_MODE) {
        // Mock successful signup with fake user data
        return {
            user: {
                id: "test-user-456",
                username: credentials.email.split('@')[0], // Use part of email as username
                email: credentials.email,
                token: "mock-token-abc"
            },
            token: "mock-token-abc"
        };
    }
    
    // Real implementation for when backend is ready
    const response = await axios.post<AuthResponse>(`${API_URL}/signup`, credentials);
    return response.data;
};