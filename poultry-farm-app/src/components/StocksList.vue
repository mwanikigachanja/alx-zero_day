<template>
  <div>
    <h2>Stocks</h2>
    <ul>
      <li v-for="stock in stocks" :key="stock.id">{{ stock.type }} - {{ stock.quantity }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['stocks']
}
</script>

<style scoped>
/* Add your component-specific styles here */
</style>

