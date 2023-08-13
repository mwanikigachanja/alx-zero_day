// services/StocksService.js
import axios from 'axios';

const API_BASE_URL = 'https://your-api-url.com'; // Replace with your actual API base URL

export default {
  getStocks() {
    return axios.get(`${API_BASE_URL}/stocks`);
  }
  // Add more methods for handling CRUD operations on stocks
};

