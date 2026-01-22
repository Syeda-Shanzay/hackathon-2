// Custom JWT-based authentication client for the backend API
import { useState, useEffect } from 'react';

// Get API base URL from environment or default
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

// Store token in localStorage for persistence
const TOKEN_KEY = 'todo_app_token';

interface User {
  id: number;
  email: string;
  name?: string;
  created_at?: string;
  updated_at?: string;
}

interface LoginResponse {
  access_token: string;
  token_type: string;
  user: User;
}

interface RegisterResponse {
  access_token: string;
  token_type: string;
  user: User;
}

interface SessionData {
  user: User | null;
  isLoading: boolean;
}

// Authentication API functions
export const signIn = async (email: string, password: string): Promise<LoginResponse> => {
  const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({ detail: 'Login failed' }));
    throw new Error(errorData.detail || 'Login failed');
  }

  const data: LoginResponse = await response.json();

  // Store token in localStorage
  localStorage.setItem(TOKEN_KEY, data.access_token);

  return data;
};

export const signUp = async (email: string, password: string, name?: string): Promise<RegisterResponse> => {
  const response = await fetch(`${API_BASE_URL}/api/auth/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password, name }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({ detail: 'Registration failed' }));
    throw new Error(errorData.detail || 'Registration failed');
  }

  const data: RegisterResponse = await response.json();

  // Store token in localStorage
  localStorage.setItem(TOKEN_KEY, data.access_token);

  return data;
};

export const signOut = async (): Promise<void> => {
  // Remove token from localStorage
  localStorage.removeItem(TOKEN_KEY);
};

export const getCurrentUser = async (): Promise<User> => {
  const token = localStorage.getItem(TOKEN_KEY);

  if (!token) {
    throw new Error('No authentication token found');
  }

  const response = await fetch(`${API_BASE_URL}/api/auth/me`, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    // If unauthorized, remove the invalid token
    if (response.status === 401) {
      localStorage.removeItem(TOKEN_KEY);
    }
    throw new Error('Failed to get user info');
  }

  const user: User = await response.json();
  return user;
};

export const useSession = (): SessionData => {
  const [session, setSession] = useState<{ user: User | null } | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchSession = async () => {
      try {
        const token = localStorage.getItem(TOKEN_KEY);
        if (token) {
          const user = await getCurrentUser();
          setSession({ user });
        } else {
          setSession({ user: null });
        }
      } catch (error) {
        console.error('Error fetching session:', error);
        setSession({ user: null });
      } finally {
        setIsLoading(false);
      }
    };

    fetchSession();

    const handleStorageChange = () => {
      const token = localStorage.getItem(TOKEN_KEY);
      if (!token) {
        setSession({ user: null });
      }
    };

    window.addEventListener('storage', handleStorageChange);

    return () => {
      window.removeEventListener('storage', handleStorageChange);
    };
  }, []);

  // ✅ Yahan fix:
  return {
    user: session?.user ?? null,
    isLoading
  };
};


// Helper function to get auth headers
export const getAuthHeaders = (): { Authorization?: string } => {
  const token = localStorage.getItem(TOKEN_KEY);
  if (token) {
    return { 'Authorization': `Bearer ${token}` };
  }
  return {};
};