<template>
  <div id="app">
    <head>
      <link href='https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons' rel="stylesheet">
    </head>
    <v-app id="inspire">
      <div>
        <v-toolbar>
          <div>
            <v-img
              src="https://frappe.io/assets/frappe_io/images/frappe-logo.png"
              width = "40"
              contain
              class="shrink mr-2"
            >
            </v-img>
          </div>

          <router-link :to="{ path: '/'}"><v-toolbar-title class="black--text">Frappe - Flask Hiring Test</v-toolbar-title></router-link>

          <v-spacer></v-spacer>

          <v-toolbar-items>
            <v-btn to='/product' text>Product</v-btn>
            <v-btn to='/location' text>Location</v-btn>
            <v-btn to='/productmovement' text>Product Movement</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <router-view/>
      </div>
    </v-app>
  </div>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
<style>
a {  text-decoration: none;}
</style>
