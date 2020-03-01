<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
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
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.currency)
                axios
                    .post('https://productstoreapi.herokuapp.com/api/products/',
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