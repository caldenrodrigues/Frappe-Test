import Vue from 'vue'
import Router from 'vue-router'
import Home from './pages/home.vue'
import Product from './pages/product.vue'
import Location from './pages/location.vue'
import ProductMovement from './pages/productmovement.vue'

Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/product',
      name: 'product',
      component: Product
    },
    {
      path: '/location',
      name: 'location',
      component: Location
    },
    {
      path: '/productmovement',
      name: 'productmovement',
      component: ProductMovement
    }
    // {
    //   path: '/register',
    //   name: 'register',
    //   component: Register
    // },
    // {
    //   path: '/mart',
    //   name: 'mart',
    //   component: Mart
    // },
    // {
    //   path: '/checkout',
    //   name: 'checkout',
    //   component: Checkout
    // },
    // {
    //   path: '/profile',
    //   name: 'profile',
    //   component: Profile
    // },
    // {
    //   path: '/admin',
    //   name: 'adminLogin',
    //   component: AdminLogin
    // },
    // {
    //   path: '/adminhome',
    //   name: 'admin',
    //   component: Admin
    // }
  ]
})

// router.beforeEach((to, from, next) => {
//   if(to.name == 'home' || to.name == 'mart' || to.name == 'adminLogin' || to.name == 'register'){
//     next();
//   }
//   else if(to.name == 'admin'){
//     if(localStorage.getItem('admintoken') != null){
//       next();
//     }
//     else{
//       next('/');
//     }
//   }
//   else if(localStorage.getItem('token') != null){
//     next();
//   }
//   else{
//     next('/')
//   }
// })

export default router
