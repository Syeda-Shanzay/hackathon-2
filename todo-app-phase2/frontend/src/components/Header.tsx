/**
 * Header component for the Todo App
 * Contains navigation links and user authentication controls
 */
import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useAuth } from '../hooks/useAuth';

const Header = () => {
  const pathname = usePathname();
  const { isAuthenticated, logout } = useAuth();

  // Navigation links
  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Tasks', path: '/tasks' },
  ];

  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex-shrink-0 flex items-center">
              <span className="text-xl font-bold text-indigo-600">Todo App</span>
            </Link>
            <nav className="ml-6 flex space-x-4">
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  href={link.path}
                  className={`px-3 py-2 rounded-md text-sm font-medium ${
                    pathname === link.path
                      ? 'bg-indigo-100 text-indigo-700'
                      : 'text-gray-700 hover:bg-gray-100'
                  }`}
                >
                  {link.name}
                </Link>
              ))}
            </nav>
          </div>

          <div className="flex items-center">
            {/* User profile dropdown or login/logout buttons */}
            {isAuthenticated ? (
              <div className="ml-4 flex items-center space-x-4">
                <button className="text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-medium">
                  Profile
                </button>
                <button
                  onClick={logout}
                  className="text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-medium"
                >
                  Logout
                </button>
              </div>
            ) : (
              <div className="ml-4 flex items-center space-x-4">
                <Link href="/login" className="text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-medium">
                  Login
                </Link>
                <Link href="/signup" className="text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-medium">
                  Sign Up
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;