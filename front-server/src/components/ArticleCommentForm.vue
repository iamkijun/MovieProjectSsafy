<template>
    <div class="container">
      <hr>
      <br />
      <h2>댓글 목록</h2>
      <input id="iput" type="text" v-model.trim="articleCommentContent" />
      <button @click="createArticleComment" class="btn btn-primary">등록</button>
      <br />
      <br>
    </div>
  </template>
  
  <script>
  export default {
    name: "ArticleCommentForm",
    data: function () {
      return {
        articleCommentContent: null,
      }
    },
    methods: {
      createArticleComment() {
        if (this.articleCommentContent) {
          this.$store.dispatch("createArticleComment", this.articleCommentContent)
        }
        this.articleCommentContent = null
      },
    },
  }
  </script>
  
  <style>
  #iput {
    margin-right: 10px;
    border-radius: 8px;
  }
  </style>
  