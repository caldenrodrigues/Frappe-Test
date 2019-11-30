<template lang="html">
  <div class="">
    <v-data-table
      :headers="headers"
      :items="products"
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
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn color="#5E64FF" dark class="mb-2" v-on="on">New Item</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.name" label="Name"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.description" label="Description"></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.action="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          edit
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
        >
          delete
        </v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import axios from 'axios';
var {ip} = require('../IP.js')
export default {
  data(){
    return {
      ip:'',
      dialog: false,
      headers: [{text:"ID",value:"id"},{text:"Name",value:"name"},{text:"Description",value:"description"},{ text: 'Actions', value: 'action', sortable: false }],
      products: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        description: ''
      },
      defaultItem: {
        name: '',
        description: ''
      },
    }
  },
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },

  created () {
    this.ip = ip
    this.initialize()
  },
  methods: {
    initialize () {
      //this.products = [{id:"001",name:"Calden",description:"Lmao"},{id:"002",name:"Alden",description:"LmaoLMAO"}]
      axios.post(`${ip}/getProduct`)
      .then((res) => {
        console.log(res.data)
        this.products = res.data.products
      })
      .catch((err) => {
        console.log(err)
      })
    },

    editItem (item) {
      this.editedIndex = this.products.indexOf(item)
      this.editedItem = Object.assign({}, item)
      console.log(item.id)
      this.dialog = true
    },

    deleteItem (item) {
      const id = item.id
      axios.post(`${ip}/delProduct`,{id})
      .then((res) => {
        this.products = res.data.products
      })
      .catch((err) => {
        console.log(err)
      })
    },

    close () {
      this.dialog = false
      this.editedItem = Object.assign({}, this.defaultItem)
      this.editedIndex = -1
    },

    save () {
      if (this.editedIndex > -1) {

        //Object.assign(this.products[this.editedIndex], this.editedItem)
        const product = this.editedItem
        axios.post(`${ip}/editProduct`,product)
        .then((res) => {
          this.products = res.data.products
        })
        .catch((err) => {
          console.log(err)
        })

      } else {

        const product = this.editedItem
        axios.post(`${ip}/addProduct`, product)
        .then((res) => {
          console.log(res.data)
          this.products = res.data.products
        })
        .catch((err) => {
          console.log(err)
        })

      }
      //this.close()
      this.dialog = false
    },
  },
}
</script>

<style lang="css" scoped>
</style>
