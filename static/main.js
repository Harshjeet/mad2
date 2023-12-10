// const app = Vue.createApp({
//   template:`<router-view />`
// });
// app.mount('#app')

import router from "./router.js";
import navbar from "./components/Navbar.js";

new Vue({
  el: "#app",
  template: 
  `<div>
      <navbar />
      <router-view />
  </div>`,
  router,
  components: {
    navbar,
  }
});
