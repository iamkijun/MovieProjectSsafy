<template>
  <div id="app">
    <br>
    
    <!-- <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link> -->
    <div id="nav"  class="d-flex justify-content-end">
      <!-- <div>
        <router-link :to="{ name: 'MvtiView' }"><img src="../assets/MVTI테스트.png" alt="MVTI"></router-link>
      </div> -->
      <div class="menu-nav">
        <div class="search-form d-flex justify-content-between">
          <b-input
            size="sm"
            class="mr-sm-2"
            type="text"
            placeholder="검색어를 입력해주세요"
            v-model="keyword"
            style="width:200px"
            @keyup.enter="searchresultshow(keyword)" 
          ></b-input>
          <b-button
            size="sm"
            class="my-2 my-sm-0 btn btn-primary"
            type="submit"
            style="width:56px; height: 50px;" 
            @click="searchresultshow(keyword)"
          >
          <span>검색</span>
          </b-button>    
        </div>
      </div>
    </div>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'


export default {
  name: 'MovieView',
  data() {
    return {
      keyword: ''
    }
  },
  components: {
    MovieList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      if (this.isLogin === true) { 
        this.$store.dispatch('getMovies')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView'})
      }
    },
    searchresultshow(keyword) {
      console.log('"',keyword,'"' + ' 검색')
      if (keyword !== ''){
        this.$router.push({
          name: "SearchPage",
          params: {
            keyword: this.keyword
          },
        }).catch(()=>{});
        this.isResultShow = true
      } else {
        alert('검색어를 입력해주세요!')
      }
    },
    keywordChanged() {
      this.isResultShow = false
    },
  },
}
</script>

<style>
h1{
  font-size: 60pt;
}
/* #search-form{
  height: 60px;
} */

</style>