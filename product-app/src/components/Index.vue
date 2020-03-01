<template>
    <div class="pt-5">
        <div v-if="products && products.length">
            <div class="card mb-3" style="background: rgba(25,25,25,.35);" v-for="product of products" v-bind:key="product.id">
                <div class="row no-gutters h-100">
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title" style="color:#fff;">{{ product.name }}</h5>
                            <p class="card-text" style="color:#fff;">{{ product.price }}</p>
                            <router-link :to="{name: 'edit', params: { id: product.id }}" class="btn btn-sm btn-primary">Edit</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteSubscription(product)">Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="products.length == 0">No products</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            products: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteSubscription: function(prdcts) {
            if (confirm('Delete ' + prdcts.name)) {
                axios.delete(`https://productstoreapi.herokuapp.com/api/products/${prdcts.id}`)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('https://productstoreapi.herokuapp.com/api/products/')
                .then( response => {
                    this.products = response.data
                });
        }
    },
}
</script>