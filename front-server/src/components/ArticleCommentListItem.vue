<template>
    <div class="d-flex justify-content-center">
      <p @click="updateArticleCommentStatus">{{ comment.content }}</p>
      <img src="../assets/458594.png" alt="삭제" style="height: 20px;" @click="deleteArticleComment" />
    </div>
  </template>
  
  <script>
  export default {
    name: "ArticleCommentListItem",
    props: {
      comment: Object,
    },
    methods: {
      updateArticleCommentStatus() {
        this.$store.dispatch("updateArticleCommentStatus", this.comment)
      },
      deleteArticleComment() {
        // console.log('삭제 메서드 호출!!')
        this.$store.dispatch('deleteArticleComment', this.comment)
        // this.$store.commit('DELETE_TODO', this.todo)
      },
    },
  }
  </script>
  
  <style>
  
  </style>  