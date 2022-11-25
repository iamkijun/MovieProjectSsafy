<template>
    <div>
      <hr>
      <br>
      <h3 style="color:black"> 오늘의 추천 영화</h3>
      <RecommendList/>
      <h3 style="color:black"> 이런 영화는 어때요?</h3>
      <RecommendListMvti/>
    </div>
  </template>
  
  <script>
  import RecommendList from '@/components/RecommendList'
  import RecommendListMvti from '@/components/RecommendListMvti'
  
  export default {
    name: 'RecommendView',
    components: {
      RecommendList,
      RecommendListMvti,
    },
    computed:{
      isLogin() {
        return this.$store.getters.isLogin
      }
    },
    created() {
      this.getRecommend()
    },
    methods: {
      getRecommend() {
        if (this.isLogin === true) { 
          this.$store.dispatch('getRecommend')
        } else {
          alert('로그인이 필요한 서비스 입니다.')
          this.$router.push({ name: 'LogInView'})
        }
      }
    }
  }
  </script>
  
  <style>
  
  </style>
  