<template>
    <div>
      <ArticleCommentListItem
        v-for="(comment, index) in articleCommentLists"
        :key="index"
        :comment="comment"
      />
    </div>
  </template>
  
  <script>
  import ArticleCommentListItem from "@/components/ArticleCommentListItem"
  
  export default {
    name: "ArticleCommentList",
    components: {
      ArticleCommentListItem,
    },
    computed: {
      articleCommentLists() {
        return this.$store.state.articleCommentLists
      },
    },
  }
  </script>
  
  <style>
  
  </style>  