import { createApp } from 'vue'
import App from './App.vue'
import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

createApp(App).mount('#app')
Vue.use(Vuetify);

new Vue({
  vuetify: new Vuetify(),
  // ...
}).$mount('#app');
