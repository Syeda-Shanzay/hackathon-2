'use client';

import { createContext, useContext, useState, ReactNode, useEffect } from 'react';
import { useSession, signIn, signUp, signOut, getCurrentUser } from '../../lib/better-auth-client';
import { User } from '../../types';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<any>;
  register: (email: string, password: string) => Promise<any>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const { user: sessionUser, isLoading: isPending } = useSession();
  const [loading, setLoading] = useState<boolean>(false);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    if (sessionUser) {
      const userData: User = {
        id: sessionUser.id,
        email: sessionUser.email,
        name: sessionUser.name || sessionUser.email?.split('@')[0],
        created_at: sessionUser.created_at || new Date().toISOString(),
        updated_at: sessionUser.updated_at || new Date().toISOString()
      };
      setUser(userData);
      setIsAuthenticated(true);
    } else {
      setUser(null);
      setIsAuthenticated(false);
    }
  }, [sessionUser]);


  const login = async (email: string, password: string) => {
    setLoading(true);
    try {
      const result = await signIn(email, password);

      // Update user state after successful login
      if (result.user) {
        const userData: User = {
          id: result.user.id,
          email: result.user.email,
          name: result.user.name || result.user.email?.split('@')[0],
          created_at: result.user.created_at || new Date().toISOString(),
          updated_at: result.user.updated_at || new Date().toISOString()
        };
        setUser(userData);
        setIsAuthenticated(true);
      }

      return result;
    } catch (error: any) {
      console.error('Login error:', error);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  const register = async (email: string, password: string) => {
    setLoading(true);
    try {
      const result = await signUp(email, password);

      // Update user state after successful registration
      if (result.user) {
        const userData: User = {
          id: result.user.id,
          email: result.user.email,
          name: result.user.name || result.user.email?.split('@')[0],
          created_at: result.user.created_at || new Date().toISOString(),
          updated_at: result.user.updated_at || new Date().toISOString()
        };
        setUser(userData);
        setIsAuthenticated(true);
      }

      return result;
    } catch (error: any) {
      console.error('Registration error:', error);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    try {
      await signOut();
      setUser(null);
      setIsAuthenticated(false);
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  const value = {
    user,
    loading: loading || isPending,
    login,
    register,
    logout,
    isAuthenticated,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};