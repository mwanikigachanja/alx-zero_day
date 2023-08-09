<template>
  <v-card>
    <v-card-title>
      Payments
    </v-card-title>
    <v-card-text>
      <v-list>
        <v-list-item v-for="(payment, index) in payments" :key="index">
          <v-list-item-title>Payment Date: {{ payment.date }}</v-list-item-title>
          <v-list-item-subtitle>Amount: {{ payment.amount }}</v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    payments: Array,
    // Add more props as needed
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>

