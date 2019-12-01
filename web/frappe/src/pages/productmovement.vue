<template lang="html">
  <div id="app">
    <v-app id="inspire">
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <v-combobox
              v-model="location"
              :items="locations"
              @change="changedLocation"
              item-text="name"
              label="Select a Location"
              color="#5E64FF"
              return-object
              autofocus
            ></v-combobox>
          </v-col>
          <v-col cols="12">
            <v-data-table
              :headers="headers"
              :items="productsLocation"
              :items-per-page="10"
              class="elevation-1 "
            >
              <template v-slot:top>
                <v-toolbar flat color="white">
                  <v-toolbar-title>Products</v-toolbar-title>
                  <v-divider
                    class="mx-4"
                    inset
                    vertical
                  ></v-divider>
                  <v-spacer></v-spacer>
                  <v-dialog v-model="importDialog" max-width="500px">
                    <template v-slot:activator="{ on }">
                      <v-btn color="#5E64FF" dark class="ma-2" v-on="on">Import Product</v-btn>
                    </template>
                    <v-card>
                      <v-card-title>
                        <span class="headline">Import Product</span>
                      </v-card-title>

                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12">
                              <v-combobox
                                v-model="productSelected"
                                :items="products"
                                item-text="name"
                                label="Select a Product"
                                color="#5E64FF"
                                return-object
                                autofocus
                              ></v-combobox>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field v-model="quantity" label="Quantity"></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="closeImport">Cancel</v-btn>
                        <v-btn color="blue darken-1" text @click="saveImport">Save</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-dialog v-model="exportDialog" max-width="500px">
                    <template v-slot:activator="{ on }">
                      <v-btn color="#e53935" dark class="ma-2" v-on="on">Export Product</v-btn>
                    </template>
                    <v-card>
                      <v-card-title>
                        <span class="headline">Export Product</span>
                      </v-card-title>

                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12">
                              <v-combobox
                                v-model="productSelected"
                                :items="products"
                                item-text="name"
                                label="Select a Product"
                                color="#5E64FF"
                                return-object
                                autofocus
                              ></v-combobox>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field v-model="quantity" label="Quantity"></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="closeExport">Cancel</v-btn>
                        <v-btn color="blue darken-1" text @click="saveExport">Save</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-toolbar>
              </template>
            </v-data-table>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios';
var {ip} = require('../IP.js')
export default {
  data(){
    return{
      importDialog: false,
      exportDialog: false,
      productSelected: "",
      headers: [{text:"ID",value:"id"},{text:"Name",value:"name"},{text:"Description",value:"description"}, {text:"Quantity", value:"quantity"}],
      locations: [],
      products: [],
      productsLocation: [],
      location: "",
      quantity: 0,
    }
  },
  created () {
    this.ip = ip
    this.initialize()
  },
  methods: {
    initialize () {
      axios.post(`${ip}/getLocation`)
      .then((res) => {
        console.log(res.data)
        this.locations = res.data.locations

        axios.post(`${ip}/getProduct`)
        .then((res) => {
          console.log(res.data)
          this.products = res.data.products
        })
        .catch((err) => {
          console.log(err)
        })

      })
      .catch((err) => {
        console.log(err)
      })



    },
    changedLocation() {
      //console.log(this.location.id)
      const location = this.location.id
      axios.post(`${ip}/move/getProduct`,{location})
      .then((res) => {
        console.log(res.data.products)
        this.productsLocation = res.data.products
      })
      .catch((err) => {
        console.log(err)
      })
    },
    closeImport() {
      this.importDialog = false
    },
    saveImport() {
      const location = this.location.id
      const product = this.productSelected.id
      const quantity = this.quantity
      axios.post(`${ip}/move/importProduct`,{
        location,
        product,
        quantity
      })
      .then((res) => {
        this.productsLocation = res.data.products
      })
      .catch((err) => {
        console.log(err)
      })
      this.importDialog = false
    },
    closeExport() {
      this.exportDialog = false
    },
    saveExport() {
      const location = this.location.id
      const product = this.productSelected.id
      const quantity = this.quantity
      axios.post(`${ip}/move/exportProduct`,{
        location,
        product,
        quantity
      })
      .then((res) => {
        this.productsLocation = res.data.products
      })
      .catch((err) => {
        console.log(err)
      })
      this.exportDialog = false
    },
  }
}
</script>

<style lang="css" scoped>
</style>
