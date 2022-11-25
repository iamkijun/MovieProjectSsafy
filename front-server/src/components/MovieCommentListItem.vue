<template>
    <div class="d-flex justify-content-center">
      <h5 @click="updateWatchStatus" :class="{ 'is-watched': watch.isWatched }">{{ watch.title }}</h5>
      <span></span>
      <img src="../assets/458594.png" alt="삭제" style="height: 20px; float: right" @click="deleteComment" />
      <!-- <button class="btn btn-danger" @click="deleteComment" style="height: 23px; width: 75px; font-size: 10px;">댓글 지우기</button> -->
    </div>
  </template>
  
  <script>
  export default {
    name: "MovieCommentListItem",
    props: {
      watch: Object,
    },
    methods: {
      deleteComment() {
        // console.log('삭제 메서드 호출!!')
        this.$store.dispatch('deleteComment', this.watch)
        // this.$store.commit('DELETE_TODO', this.todo)
      },
      updateWatchStatus() {
        this.$store.dispatch("updateWatchStatus", this.watch)
      },
    },
  }
  </script>
  
  <style>
  
  </style>
  