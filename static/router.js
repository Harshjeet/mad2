import home from './components/Home.js'
import Login from './components/login.js'

const routes = [
  { path: '/', component: home },
  { path: '/login', component: Login },

];

export default new VueRouter({
  routes,
})