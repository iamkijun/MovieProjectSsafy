<template>
    <div class="search-form d-flex justify-content-center">
      <!-- <input id="iput" type="text" placeholder="댓글을 입력해주세요" v-model.trim="watchTitle" />
      <button @click="createWatch" class="btn btn-primary">댓글 작성</button> -->
      <b-input
        size="sm"
        class="mr-sm-2"
        type="text"
        placeholder="댓글을 입력해주세요."
        v-model.trim="watchTitle"
        style="width:200px"
        @keyup.enter="createWatch" 
      ></b-input>
      <b-button
        size="sm"
        class="my-2 my-sm-0 btn btn-primary"
        type="submit"
        style="width:56px; height: 40px;" 
        @click="createWatch"
      >
      <span>검색</span> 
      </b-button>    
      <br />
    </div>
  </template>
  
  <script>
  export default {
    name: "MovieCommentListForm",
    data: function () {
      return {
        watchTitle: null,
      }
    },
    methods: {
      createWatch() {
        if (this.watchTitle) {
          this.$store.dispatch("createWatch", this.watchTitle)
        }
        this.watchTitle = null
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
  