/**
 * Authentication hook for the Todo App
 * Exports the useAuth hook from the auth context
 */

import { User } from '../types';

// Export the hook from the auth context
export { useAuth } from '../app/contexts/auth-context';

// Export the interface
export interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<any>;
  register: (email: string, password: string) => Promise<any>;
  logout: () => void;
  isAuthenticated: boolean;
}