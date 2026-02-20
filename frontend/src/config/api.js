export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '';

// Helper to build full URL
const buildUrl = (path) => {
  // If API_BASE_URL is set, use it
  if (API_BASE_URL) {
    return `${API_BASE_URL}${path}`;
  }
  // Otherwise use relative path (for Vite proxy in dev)
  return path;
};

export const API_ENDPOINTS = {
    
}