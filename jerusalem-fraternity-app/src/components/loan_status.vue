<template>
  <v-card>
    <v-card-title>
      Loan Status
    </v-card-title>
    <v-card-text>
      <div v-if="hasLoan">
        <p>You have an active loan.</p>
        <p>Loan Amount: {{ loanAmount }}</p>
      </div>
      <div v-else>
        <p>You don't have an active loan.</p>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    hasLoan: Boolean,
    loanAmount: Number,
    // Add more props as needed
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>

