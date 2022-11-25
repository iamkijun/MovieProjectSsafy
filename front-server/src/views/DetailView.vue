<template>
    <div>
      <br>
      <h5 style="color:black">제목</h5>
      <p>{{ article?.title }}</p>
      <h5 style="color:black">내용</h5>
      <p>{{ article?.content }}</p>
      <button class="btn btn-danger" @click="deleteArticle">글 삭제</button>
      <br />
      <ArticleCommentForm />
      <ArticleCommentList />
      <router-link :to="{ name: 'ArticleView' }">뒤로가기</router-link>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import ArticleCommentList from '@/components/ArticleCommentList'
  import ArticleCommentForm from '@/components/ArticleCommentForm'
  
  const API_URL = "http://127.0.0.1:8000";
  
  export default {
    name: "DetailView",
    components: {
      ArticleCommentList,
      ArticleCommentForm,
    },
    data() {
      return {
        article: null,
        article_comment: null,
      };
    },
    created() {
      this.getArticleDetail();
    },

    methods: {
      getArticleDetail() {
        axios({
          method: "get",
          url: `${API_URL}/articles/${this.$route.params.id}`,
        })
          .then((res) => {
            console.log(res);
            this.article = res.data;
          })
          .catch((err) => {
            console.log(err);
          });
      },
      deleteArticle() {
        console.log('삭제 메서드 호출!!')
        this.$store.dispatch('deleteArticle', this.article)
        // this.$store.commit('DELETE_TODO', this.todo)
      },
    },
  };
  </script>
  
<style>

</style>