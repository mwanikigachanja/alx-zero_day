<template>
  <v-card class="payments-card">
    <v-card-title class="payments-title">
      Payments
    </v-card-title>
    <v-card-text>
      <v-list>
        <v-list-item
          v-for="(payment, index) in payments"
          :key="index"
          class="payment-item"
        >
          <v-list-item-title class="payment-date">
            Payment Date: {{ payment.date }}
          </v-list-item-title>
          <v-list-item-subtitle class="payment-amount">
            Amount: {{ payment.amount }}
          </v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<style scoped>
.payments-card {
  background-color: #f5f5f5;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.payments-title {
  font-size: 20px;
  color: #333;
  margin-bottom: 16px;
}

.payment-item {
  border-bottom: 1px solid #ddd;
  padding: 8px 0;
}

.payment-date {
  font-size: 16px;
  color: #333;
}

.payment-amount {
  font-size: 14px;
  color: #555;
}
</style>

