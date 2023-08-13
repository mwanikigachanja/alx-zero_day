// store/stocks.js
import StocksService from '@/services/StocksService';

const state = {
  stocks: []
};

const mutations = {
  setStocks(state, stocks) {
    state.stocks = stocks;
  }
};

const actions = {
  async fetchStocks({ commit }) {
    try {
      const response = await StocksService.getStocks();
      commit('setStocks', response.data);
    } catch (error) {
      console.error('Error fetching stocks:', error);
    }
  }
  // Add actions for adding, updating, and deleting stocks
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};

