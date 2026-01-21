/**
 * Type definitions for the Todo App
 * Contains all TypeScript interfaces and types used across the application
 */

export interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;  // Changed from status to completed (boolean)
  created_at: string;
  updated_at: string;
  user_id: number;  // Changed from owner_id to user_id to match backend
}

export interface TaskCreateRequest {
  title: string;
  description?: string;
}

export interface TaskUpdateRequest {
  title?: string;
  description?: string;
  completed?: boolean;  // Changed from status to completed (boolean)
}

export interface User {
  id: number;
  email: string;
  name?: string;
  created_at: string;
  updated_at: string;
}

export interface AuthResponse {
  id: string;
  email: string;
  access_token: string;
  refresh_token: string;
}

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  status: number;
}

export interface FilterOptions {
  status?: 'all' | 'pending' | 'completed';
  sort?: 'date' | 'title';
  order?: 'asc' | 'desc';
}

export interface TaskFormData {
  title: string;
  description?: string;
}