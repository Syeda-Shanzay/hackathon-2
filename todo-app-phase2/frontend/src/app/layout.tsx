import '../styles/globals.css';
import { Providers } from './providers';
import { AuthProvider } from './contexts/auth-context';
import Navbar from './components/Navbar';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
        <Providers>
          <AuthProvider>
            <div className="min-h-screen flex flex-col">
              <Navbar />
              <main className="flex-grow container mx-auto px-4 py-8 max-w-7xl">
                {children}
              </main>
              <footer className="bg-white border-t border-gray-200 py-8 mt-12">
                <div className="container mx-auto px-4">
                  <div className="flex flex-col md:flex-row justify-between items-center">
                    <div className="mb-4 md:mb-0">
                      <h3 className="text-lg font-semibold text-gray-900">TodoApp</h3>
                      <p className="text-gray-600 mt-1">Stay organized, stay productive</p>
                    </div>
                    <div className="text-center md:text-right">
                      <p className="text-gray-600">© {new Date().getFullYear()} Todo App. All rights reserved.</p>
                      <div className="mt-2 flex justify-center md:justify-end space-x-6">
                        <a href="#" className="text-gray-500 hover:text-gray-700 text-sm">Privacy Policy</a>
                        <a href="#" className="text-gray-500 hover:text-gray-700 text-sm">Terms of Service</a>
                        <a href="#" className="text-gray-500 hover:text-gray-700 text-sm">Contact</a>
                      </div>
                    </div>
                  </div>
                </div>
              </footer>
            </div>
          </AuthProvider>
        </Providers>
      </body>
    </html>
  );
}