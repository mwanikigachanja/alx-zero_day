<template>
  <div>
    <account-management></account-management>
    <loan-status :hasLoan="hasLoan" :loanAmount="loanAmount"></loan-status>
    <payments></payments>
    <!-- Add more components as needed -->
  </div>
</template>

<script>
import AccountManagement from '@/components/acc_man.vue';
import LoanStatus from '@/components/loan_status.vue';
import Payments from '@/components/payments.vue';

export default {
  components: {
    AccountManagement,
    LoanStatus,
    Payments,
  },
data() {
    return {
      hasLoan: true, // Example loan status
      loanAmount: 5000, // Example loan amount
      paymentHistory: [
        { date: '2023-08-01', amount: 200 },
        { date: '2023-08-15', amount: 150 },
        // Add more payment history data
      ],
    };
  },
};
</script>

