<template>
    <!-- <div id="searchresult">
      <div class="result-title">
        총 {{$store.getters.getFilteredMovie(keyword).length}}개의 영화가 검색되었습니다.
      </div>
      
      <div class="result-items">
        <div
        class="resultitem"
        :key="index"
        v-for="(movie, index) in $store.getters.getFilteredMovie(keyword)"
        @click="detailshow(index)"
        >
        <div class="movie-img">
          <img v-bind:src="movie.movieimg" />
        </div>
        <div class="movie-info">
          <li class="movie-info-title">{{ movie.title }}</li>
        </div>
        </div>
      </div>
    </div> -->
    
    <div>
      <br>
      <h4>검색결과</h4>
      <SearchResult
        v-for="(post, index) in searchList"
        :key="index"
        :post="post"
      />
      <hr />
    </div>

</template>

<script>
// import SearchResult from "@/components/SearchResult"
import axios from "axios"

const URL = 'http://127.0.0.1:8000'


export default {
  name: "SearchResult",
  props: [ 'keyword'], //상위 컴포넌트인 SearchPage.vue로부터 데이터 받음
  data() {
    return {
      searchList: [],
    }
  },
  methods:{
    getSearchList() {
      axios({
        method: "get",
        url: `${URL}/api/v1/movies/searchpage/${this.$route.params.keyword}/`,
      })
        .then((res) => {
          console.log(res)
          this.searchList = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getSearchList()
  },
}
</script>