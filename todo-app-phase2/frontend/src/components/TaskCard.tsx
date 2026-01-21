/**
 * TaskCard component for the Todo App
 * Displays a single task in a modern card format with shadow, hover effects, and status badges
 */
import React, { useState } from 'react';
import { Task } from '../types';

interface TaskCardProps {
  task: Task;
  onToggleStatus: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
  onEdit: (task: Task) => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onToggleStatus, onDelete, onEdit }) => {
  const [showConfirmDelete, setShowConfirmDelete] = useState(false);

  const handleToggleStatus = () => {
    onToggleStatus(task.id, !task.completed);
  };

  const handleDeleteClick = () => {
    if (showConfirmDelete) {
      onDelete(task.id);
      setShowConfirmDelete(false);
    } else {
      setShowConfirmDelete(true);
      // Hide the confirmation after 5 seconds if not clicked
      setTimeout(() => setShowConfirmDelete(false), 5000);
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };

  return (
    <div className={`bg-white rounded-xl shadow-sm border border-gray-200 transition-all duration-200 hover:shadow-md hover:border-gray-300 ${
      task.completed ? 'bg-gray-50' : 'bg-white'
    }`}>
      <div className="p-5">
        <div className="flex items-start justify-between">
          <div className="flex-1 min-w-0">
            <div className="flex items-center mb-3">
              <input
                type="checkbox"
                checked={task.completed}
                onChange={handleToggleStatus}
                className="h-5 w-5 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded mr-3 cursor-pointer"
              />
              <h3 className={`text-lg font-semibold ${
                task.completed ? 'line-through text-gray-500' : 'text-gray-900'
              }`}>
                {task.title}
              </h3>
            </div>

            {task.description && (
              <p className={`text-sm mb-3 ${
                task.completed ? 'text-gray-500' : 'text-gray-600'
              }`}>
                {task.description}
              </p>
            )}

            <div className="flex items-center text-xs text-gray-500">
              <svg className="flex-shrink-0 mr-1.5 h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clipRule="evenodd" />
              </svg>
              <span>{formatDate(task.created_at)}</span>
            </div>
          </div>

          <div className="ml-4 flex-shrink-0 flex space-x-2">
            <button
              onClick={() => onEdit(task)}
              className="inline-flex items-center p-2 border border-gray-300 rounded-lg shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200"
              title="Edit task"
            >
              <svg className="h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
            </button>

            {showConfirmDelete ? (
              <button
                onClick={handleDeleteClick}
                className="inline-flex items-center p-2 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors duration-200"
                title="Confirm delete"
              >
                <svg className="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </button>
            ) : (
              <button
                onClick={handleDeleteClick}
                className="inline-flex items-center p-2 border border-gray-300 rounded-lg shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors duration-200"
                title="Delete task"
              >
                <svg className="h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

const MemoizedTaskCard = React.memo(TaskCard);
export default MemoizedTaskCard;