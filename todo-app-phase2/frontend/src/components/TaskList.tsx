/**
 * TaskList component for the Todo App
 * Displays a list of tasks in a modern grid layout
 */
import React from 'react';
import TaskCard from './TaskCard';
import { Task, FilterOptions } from '../types';

interface TaskListProps {
  tasks: Task[];
  onToggleStatus: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
  onEdit: (task: Task) => void;
  filterOptions: FilterOptions;
  onFilterChange: (options: FilterOptions) => void;
  loading?: boolean;
}

const TaskList: React.FC<TaskListProps> = ({
  tasks,
  onToggleStatus,
  onDelete,
  onEdit,
  filterOptions,
  onFilterChange,
  loading = false
}) => {
  // Filter tasks based on completion status
  const filteredTasks = tasks.filter(task => {
    if (filterOptions.status === 'pending') return !task.completed;
    if (filterOptions.status === 'completed') return task.completed;
    return true; // 'all' or undefined
  });

  // Sort tasks based on selected criteria
  const sortedTasks = [...filteredTasks].sort((a, b) => {
    if (filterOptions.sort === 'date') {
      const dateA = new Date(a.created_at);
      const dateB = new Date(b.created_at);
      return filterOptions.order === 'desc' ? dateB.getTime() - dateA.getTime() : dateA.getTime() - dateB.getTime();
    } else if (filterOptions.sort === 'title') {
      return filterOptions.order === 'desc'
        ? b.title.localeCompare(a.title)
        : a.title.localeCompare(b.title);
    }
    return 0;
  });

  if (loading) {
    return (
      <div className="p-6">
        <div className="flex justify-center items-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-indigo-600"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="p-6">
      {sortedTasks.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {sortedTasks.map((task) => (
            <TaskCard
              key={task.id}
              task={task}
              onToggleStatus={onToggleStatus}
              onDelete={onDelete}
              onEdit={onEdit}
            />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <div className="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-indigo-100 text-indigo-600">
            <svg className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <h3 className="mt-4 text-lg font-medium text-gray-900">No tasks yet</h3>
          <p className="mt-1 text-gray-500">Get started by creating a new task.</p>
        </div>
      )}
    </div>
  );
};

const MemoizedTaskList = React.memo(TaskList);
export default MemoizedTaskList;