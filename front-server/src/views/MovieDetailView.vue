<template>
  
  <div class="row g-0">
    <div class="container">
      <div class="row">
        <div class="col-12">
        </div>
      </div>
      <hr>
    </div>
    
    <section class="mx-4">
      <div class="container">
        <div class="row justify-content-center align-items-center">
          <div class="col-5">
            <img class="detail_img" :src="poster_path" alt="POSTER" style="height:600px">
          </div>
          <div class="col-1"></div>
          <div class="col-6 text-bg p-4">
            <br>
            <br>
            <h2>{{ movieInfo?.title }}</h2>
            <h6 class="d-flex justify-content-end">개봉일: {{ movieInfo?.release_date }}</h6>
            <br>
            <p style="font-size: 13pt">{{ movieInfo?.overview }}</p>
            <hr>
            <h3>댓글 목록</h3>
            <br>
            <div>
              <MovieCommentList />
              <MovieCommentListForm />
            </div>
            <div class="d-flex justify-content-between">
              <span></span>
              <router-link :to="{ name: 'MovieView',}">
              [뒤로가기]
              </router-link>
            </div>
            
          </div>
        </div>
      </div>
      
      <hr>
    </section>
    
  </div>

</template>

<script>
import axios from 'axios'
import MovieCommentList from '@/components/MovieCommentList'
import MovieCommentListForm from '@/components/MovieCommentListForm'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    MovieCommentList,
    MovieCommentListForm,
  },
  data() {
    return {
      movieInfo: null,
      review: null,
      poster_path: null,
    }
  },
  created() {
    this.getMovieDetail()
    this.getReviews()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
      })
        .then((res) => {
          console.log(res)
          this.movieInfo = res.data
          this.poster_path = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${this.movieInfo.poster_path}`
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getReviews() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${this.$route.params.id}/reviews/`
      })
        .then((res) => {
          console.log(res)
          this.review = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
}
</script>