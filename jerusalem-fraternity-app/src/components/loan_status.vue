<template>
  <v-card class="loan-status-card">
    <v-card-title class="loan-status-title">
      Loan Status
    </v-card-title>
    <v-card-text>
      <div v-if="hasLoan" class="active-loan">
        <p class="loan-status-text">You have an active loan.</p>
        <p class="loan-amount">Loan Amount: {{ loanAmount }}</p>
      </div>
      <div v-else class="no-loan">
        <p class="loan-status-text">You don't have an active loan.</p>
      </div>
    </v-card-text>
  </v-card>
</template>

<style scoped>
.loan-status-card {
  background-color: #f5f5f5;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.loan-status-title {
  font-size: 20px;
  color: #333;
  margin-bottom: 16px;
}

.active-loan {
  background-color: #c7e1c1;
  padding: 8px;
  border-radius: 4px;
}

.loan-status-text {
  font-size: 16px;
  color: #333;
}

.loan-amount {
  font-size: 14px;
  color: #555;
}
</style>

