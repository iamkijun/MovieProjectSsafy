<template>
  <div class="py-5">
    <div class="container">
      <div class="row row-cols-1 row-cols-md-6 g-4">
        <MovieListItem
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
    <!-- <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT"
      crossorigin="anonymous"
    /> -->
  </div>
</template>

<!-- <script
  src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
  crossorigin="anonymous"
></script> -->

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  components: {
    MovieListItem
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
}
</script>

<style>
.movie-list {
  text-align: start;
  transform: scale(1.3);
  overflow: visible;
  cursor: pointer;
  z-index: 98;
}

</style>
