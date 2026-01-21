/**
 * Custom hook for managing tasks with API integration
 * Connects the frontend components to the backend API
 */
import { useState, useEffect } from 'react';
import { apiClient } from '../lib/api';
import { Task, FilterOptions } from '../types';
import { useAuth } from './useAuth';

interface UseTasksReturn {
  tasks: Task[];
  loading: boolean;
  error: string | null;
  fetchTasks: (filters?: FilterOptions) => Promise<void>;
  createTask: (taskData: { title: string; description?: string }) => Promise<Task | null>;
  updateTask: (taskId: number, taskData: Partial<Task>) => Promise<Task | null>;
  deleteTask: (taskId: number) => Promise<boolean>;
  toggleTaskCompletion: (taskId: number) => Promise<Task | null>;
  refreshTasks: () => Promise<void>;
}

export const useTasks = (): UseTasksReturn => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const { user } = useAuth(); // Get the current user from auth context

  const fetchTasks = async (filters?: FilterOptions) => {
    if (!user) {
      setError('User not authenticated');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const status = filters?.status === 'all' ? undefined : filters?.status;
      const sort = filters?.sort;
      const order = filters?.order;

      const response = await apiClient.getTasks(user.id, status, sort, order);

      if (response.error) {
        setError(response.error);
      } else {
        setTasks(response.data || []);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch tasks');
    } finally {
      setLoading(false);
    }
  };

  const createTask = async (taskData: { title: string; description?: string }) => {
    if (!user) {
      setError('User not authenticated');
      return null;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await apiClient.createTask(user.id, taskData);

      if (response.error) {
        setError(response.error);
        return null;
      }

      // Add the new task to the local state
      if (response.data) {
        setTasks(prev => [...prev, response.data as Task]);
        return response.data as Task;
      }

      return null;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create task');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const updateTask = async (taskId: number, taskData: Partial<Task>) => {
    if (!user) {
      setError('User not authenticated');
      return null;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await apiClient.updateTask(user.id, taskId, taskData);

      if (response.error) {
        setError(response.error);
        return null;
      }

      // Update the task in the local state
      if (response.data) {
        setTasks(prev => prev.map(task =>
          task.id === taskId ? response.data as Task : task
        ));
        return response.data as Task;
      }

      return null;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update task');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async (taskId: number) => {
    if (!user) {
      setError('User not authenticated');
      return false;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await apiClient.deleteTask(user.id, taskId);

      if (response.error) {
        setError(response.error);
        return false;
      }

      // Remove the task from the local state
      setTasks(prev => prev.filter(task => task.id !== taskId));
      return true;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete task');
      return false;
    } finally {
      setLoading(false);
    }
  };

  const toggleTaskCompletion = async (taskId: number) => {
    if (!user) {
      setError('User not authenticated');
      return null;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await apiClient.toggleTaskCompletion(user.id, taskId);

      if (response.error) {
        setError(response.error);
        return null;
      }

      // Update the task in the local state
      if (response.data) {
        setTasks(prev => prev.map(task =>
          task.id === taskId ? response.data as Task : task
        ));
        return response.data as Task;
      }

      return null;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to toggle task completion');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const refreshTasks = async () => {
    await fetchTasks();
  };

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    createTask,
    updateTask,
    deleteTask,
    toggleTaskCompletion,
    refreshTasks,
  };
};