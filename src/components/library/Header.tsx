import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="py-4 border-b border-gray-200 bg-white">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        {/* Logo - Updated to image and external link */}
        <div className="flex items-center">
          <a href="https://www.hannahstone.org/reading" target="_blank" rel="noopener noreferrer">
            <img src="/images/hannahstone-logo.png" alt="Hannah Stone Logo" className="h-8" />
          </a>
        </div>
        {/* Only one navigation link to reading website */}
        <nav className="flex space-x-8">
          <a 
            href="https://www.hannahstone.org/reading" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="text-sm font-medium text-gray-600 hover:text-gray-900"
          >
            Reading Website
          </a>
        </nav>
      </div>
    </header>
  );
};

export default Header; 