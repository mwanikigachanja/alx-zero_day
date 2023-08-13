<template>
  <div>
    <h1>Stocks Module</h1>
    <StocksList :stocks="stocks" />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  computed: {
    ...mapState('stocks', ['stocks'])
  },
  created() {
    this.fetchStocks();
  },
  methods: {
    ...mapActions('stocks', ['fetchStocks'])
  }
};
</script>

