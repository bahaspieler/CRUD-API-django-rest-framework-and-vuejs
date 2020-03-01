<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Products</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">Add product</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>
