<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="name">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="product.name"
                    v-validate="'required'"
                    name="name"
                    placeholder="Enter name"
                    :class="{'is-invalid': errors.has('product.name') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="price">price</label>
                <input
                    type="number"
                    name="price"
                    v-validate="'required'"
                    class="form-control"
                    id="price"
                    v-model="product.price"
                    placeholder="Enter price"
                    :class="{'is-invalid': errors.has('product.price') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid price.
                </div>
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            product: {
                name: '',
                price: '',
            },
            submitted: false
        }
    },
    mounted() {
        axios.get('https://productstoreapi.herokuapp.com/api/products/' + this.$route.params.id)
            .then( response => {
                console.log(response.data)
                this.product = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .put(`https://productstoreapi.herokuapp.com/api/products/${this.product.id}/`,
                        this.product
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>

