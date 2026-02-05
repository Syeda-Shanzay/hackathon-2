/**
 * API client utility for the Todo App
 * Handles all API calls with proper authentication and error handling
 */

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  status: number;
}

export interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
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
  completed?: boolean;
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

class ApiClient {
  private baseUrl: string;

  constructor() {
    // Use the backend API URL from environment variables
    this.baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';
  }

  /**
   * Internal method to make API requests
   */
  private async request<T>(endpoint: string, options: RequestInit = {}): Promise<ApiResponse<T>> {
    // Prepend base URL if the endpoint is an absolute URL
    const url = endpoint.startsWith('http') ? endpoint : `${this.baseUrl}${endpoint}`;

    // Get the token from localStorage
    const token = typeof window !== 'undefined' ? localStorage.getItem('todo_app_token') : null;

    const headers = {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` }),
      ...options.headers,
    } as Record<string, string>;

    // const headers = {
    //   'Content-Type': 'application/json',
    //   ...options.headers,
    // } as Record<string, string>;


    try {
      // const response = await fetch(url, {
      //   ...options,
      //   headers,
      // });
      const response = await fetch(url, {
        ...options,
        headers,
        credentials: 'include', // ⭐⭐⭐ VERY IMPORTANT
      });


      // Handle 401 Unauthorized by redirecting to login
      if (response.status === 401) {
        // In a Next.js app, you'd typically redirect to login page
        if (typeof window !== 'undefined') {
          window.location.href = '/login';
        }
        console.warn('Unauthorized access - session may be expired');
      }

      // For 204 No Content responses, don't try to parse JSON
      if (response.status === 204) {
        return {
          status: response.status,
        } as ApiResponse<T>;
      }

      const data = await response.json();

      if (!response.ok) {
        return {
          error: data.detail || `HTTP error! status: ${response.status}`,
          status: response.status,
        };
      }

      return {
        data,
        status: response.status,
      };
    } catch (error: any) {
      return {
        error: error.message || 'Network error occurred',
        status: 0,
      };
    }
  }

  // Task methods - Updated to call backend API directly
  async getTasks(userId: number, status?: string, sort?: 'date' | 'title', order?: 'asc' | 'desc'): Promise<ApiResponse<Task[]>> {
    const params = new URLSearchParams();
    if (status && status !== 'all') params.append('status', status);
    if (sort) params.append('sort', sort);
    if (order) params.append('order', order);

    const queryString = params.toString();
    const endpoint = `/api/${userId}/tasks${queryString ? '?' + queryString : ''}`;

    return this.request<Task[]>(endpoint);
  }

  async getTaskById(userId: number, taskId: number): Promise<ApiResponse<Task>> {
    return this.request<Task>(`/api/${userId}/tasks/${taskId}`);
  }

  async createTask(userId: number, taskData: TaskCreateRequest): Promise<ApiResponse<Task>> {
    return this.request<Task>(`/api/${userId}/tasks`, {
      method: 'POST',
      body: JSON.stringify(taskData),
    });
  }

  async updateTask(userId: number, taskId: number, taskData: TaskUpdateRequest): Promise<ApiResponse<Task>> {
    return this.request<Task>(`/api/${userId}/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  }

  async deleteTask(userId: number, taskId: number): Promise<ApiResponse<void>> {
    return this.request<void>(`/api/${userId}/tasks/${taskId}`, {
      method: 'DELETE',
    });
  }

  async toggleTaskCompletion(userId: number, taskId: number): Promise<ApiResponse<Task>> {
    return this.request<Task>(`/api/${userId}/tasks/${taskId}/toggle`, {
      method: 'PATCH',
    });
  }
}

// Create singleton instance
export const apiClient = new ApiClient();

export default apiClient;