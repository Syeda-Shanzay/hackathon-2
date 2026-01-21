/**
 * Tasks page for the Todo App
 * Integrates all components and API calls for task management
 */
'use client';

import React, { useState, useEffect } from 'react';
import TaskList from '../../components/TaskList';
import TaskForm from '../../components/TaskForm';
import { Task, FilterOptions, TaskFormData } from '../../types';
import { useAuth } from '../../hooks/useAuth';
import { useTasks } from '../../hooks/useTasks';

const TasksPage = () => {
  const { user, isAuthenticated } = useAuth();
  const { tasks, loading, error, fetchTasks, createTask, updateTask, deleteTask, toggleTaskCompletion } = useTasks();
  const [showForm, setShowForm] = useState<boolean>(false);
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [filterOptions, setFilterOptions] = useState<FilterOptions>({});

  // Load tasks on component mount and when user changes
  useEffect(() => {
    if (isAuthenticated) {
      fetchTasks(filterOptions);
    }
  }, [isAuthenticated, filterOptions]);

  const handleToggleStatus = async (id: number, completed: boolean) => {
    try {
      await toggleTaskCompletion(id);
    } catch (err) {
      console.error('Error toggling task status:', err);
    }
  };

  const handleDelete = async (id: number) => {
    try {
      await deleteTask(id);
    } catch (err) {
      console.error('Error deleting task:', err);
    }
  };

  const handleEdit = (task: Task) => {
    setEditingTask(task);
    setShowForm(true);
  };

  const handleFormSubmit = async (taskData: TaskFormData) => {
    try {
      if (editingTask) {
        // Update existing task
        await updateTask(editingTask.id, {
          title: taskData.title,
          description: taskData.description,
        });
      } else {
        // Create new task
        await createTask({
          title: taskData.title,
          description: taskData.description,
        });
      }

      setShowForm(false);
      setEditingTask(null);
    } catch (err) {
      console.error('Error submitting task:', err);
    }
  };

  const handleFormCancel = () => {
    setShowForm(false);
    setEditingTask(null);
  };

  const handleFilterChange = (options: FilterOptions) => {
    setFilterOptions(options);
  };

  if (loading && tasks.length === 0) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-indigo-600"></div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">My Tasks</h1>
        <p className="text-gray-600">Manage your daily tasks and boost your productivity</p>
      </div>

      {error && (
        <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
          <div className="text-red-800">{error}</div>
        </div>
      )}

      <div className="flex flex-col lg:flex-row gap-6">
        <div className="lg:w-3/4">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
            <div className="p-6 border-b border-gray-200">
              <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <h2 className="text-xl font-semibold text-gray-900">Task List</h2>
                <button
                  onClick={() => setShowForm(true)}
                  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200"
                >
                  <svg className="-ml-1 mr-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clipRule="evenodd" />
                  </svg>
                  Add Task
                </button>
              </div>
            </div>

            <TaskList
              tasks={tasks}
              onToggleStatus={handleToggleStatus}
              onDelete={handleDelete}
              onEdit={handleEdit}
              filterOptions={filterOptions}
              onFilterChange={handleFilterChange}
              loading={loading}
            />
          </div>
        </div>

        <div className="lg:w-1/4">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 sticky top-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Filters</h3>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Status</label>
                <select
                  value={filterOptions.status || 'all'}
                  onChange={(e) => handleFilterChange({ ...filterOptions, status: e.target.value as 'all' | 'pending' | 'completed' })}
                  className="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                >
                  <option value="all">All Tasks</option>
                  <option value="pending">Pending</option>
                  <option value="completed">Completed</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Sort By</label>
                <select
                  value={filterOptions.sort || ''}
                  onChange={(e) => handleFilterChange({ ...filterOptions, sort: e.target.value as 'date' | 'title' })}
                  className="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                >
                  <option value="">Default</option>
                  <option value="date">Date</option>
                  <option value="title">Title</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Order</label>
                <select
                  value={filterOptions.order || 'asc'}
                  onChange={(e) => handleFilterChange({ ...filterOptions, order: e.target.value as 'asc' | 'desc' })}
                  className="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                >
                  <option value="asc">Ascending</option>
                  <option value="desc">Descending</option>
                </select>
              </div>
            </div>

            <div className="mt-6 pt-6 border-t border-gray-200">
              <div className="grid grid-cols-2 gap-4">
                <div className="text-center p-3 bg-gray-50 rounded-lg">
                  <div className="text-2xl font-bold text-gray-900">{tasks.length}</div>
                  <div className="text-sm text-gray-600">Total</div>
                </div>
                <div className="text-center p-3 bg-blue-50 rounded-lg">
                  <div className="text-2xl font-bold text-blue-600">
                    {tasks.filter(t => !t.completed).length}
                  </div>
                  <div className="text-sm text-gray-600">Pending</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {showForm && (
        <TaskForm
          task={editingTask ? {
            title: editingTask.title,
            description: editingTask.description || '',
          } : undefined}
          onSubmit={handleFormSubmit}
          onCancel={handleFormCancel}
          isEditing={!!editingTask}
        />
      )}
    </div>
  );
};

export default TasksPage;