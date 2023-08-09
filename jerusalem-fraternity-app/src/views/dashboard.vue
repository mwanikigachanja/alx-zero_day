<template>
  <div>
    <account-management></account-management>
    <loan-status></loan-status>
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
};
</script>

