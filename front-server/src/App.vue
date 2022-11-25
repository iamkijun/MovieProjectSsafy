<template>
  <div id="app">
    <nav>
      <div class="m-3 align-self-center">
        <router-link :to="{ name: 'MovieView' }">홈으로</router-link> | 
        <router-link :to="{ name: 'RecommendView' }">추천영화 </router-link> |
        <router-link :to="{ name: 'ArticleView' }">자유게시판</router-link> |
        <router-link :to="{ name: 'MvtiView' }">MVTI 테스트</router-link>
      </div>
      <div class="m-3 d-flex justify-content-end" style="margin-left: 100px;">
        <router-link :to="{ name: 'SignUpView' }">회원가입 </router-link>  | 
        <router-link :to="{ name: 'LogInView' }"> 로그인 </router-link>
      </div>
      <br>
      <router-link :to="{ name: 'MovieView' }"><img src="./assets/MVTI로고.png" alt="MVTI"></router-link>
      <br>
      <br>
    </nav>
    <router-view/>
    <footer id="footer" class="col-12">
      <hr>
      <div class="m-3">
        <div class="copy-text-block">주소: 대한민국 서울특별시 서울 강남구 테헤란로 212, 멀티캠퍼스 201호 (06220) | 9조 | made by 김호준 & 이기준</div>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from "axios"
export default {
  data() {
    return {
      bestMovieList: [],
    }
  },
  methods: {
    getBestMovieList() {
      const options = {
        url: `https://api.themoviedb.org/3/movie/top_rated`,
        method: "get",
        params: {
          api_key: "f7fb3966fa04584f38174fe8f31397a5",
          language: "ko-KR",
          page: 1,
        },
      }
      axios(options)
        .then((res) => {
          // console.log(res)
          this.bestMovieList = res.data.results
          this.$store.commit("GET_BEST_MOVIE_LIST", this.bestMovieList)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getBestMovieList()
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
@font-face {
    font-family: 'LINESeedKR-Bd';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/LINESeedKR-Bd.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}

* {
  background-color: lightslategray;
  color: white;
  font-family: 'LINESeedKR-Bd';
}

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  position: relative;
  min-height: 100%;
  padding-bottom: 114px;
}
/* nav {
  padding: 30px;
} */
#nav {
  text-align: right;
  height: 125px;
  padding: 25px;
  font-size: 30px;
  font-family: 'netflix-font';
}
/* nav a {
  font-weight: bold;
  color: #2c3e50;
} */
nav a {
  font-weight: bold;
  text-decoration: none;
  color: black;
}
/* nav a.router-link-exact-active {
  color: #42b983;
} */
nav a.router-link-exact-active {
  /* color: #E50914; */
  color: darkblue
}

#logo {
  width: 150px;
  height: 120px;
  margin-inline: 30px;
  margin-top: 10px;
}

#footer {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  text-align: left;
  font-size : 11.5px;
}
</style>
