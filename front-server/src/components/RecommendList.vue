<template>
    <div class="py-5">
      <div class="container">
        <div class="row row-cols-1 row-cols-md-6 g-4">
          <RecommendListItem
            v-for="recommend_movie in randomMovie"
            :key="recommend_movie.id"
            :recommend_movie="recommend_movie"
          />
        </div>
      </div>
      <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT"
        crossorigin="anonymous"
      />
    </div>
  </template>
  
  <script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
    crossorigin="anonymous"
  ></script>
  
  <script>
  import RecommendListItem from '@/components/RecommendListItem'
  import _ from "lodash"
  
  export default {
    name: 'RecommendList',
    components: {
      RecommendListItem
    },
    computed: {
      recommend_movies() {
        return this.$store.state.movies
      },
      randomMovie(){
        let a = _.sampleSize(_.range(50), 6)
        let li = a.map((val)=>{return this.recommend_movies[val]})
        return li
      },
    },
  }
  
  </script>
  
  <style>
  .recommend_movie-list {
    text-align: start;
  }
  </style>
  