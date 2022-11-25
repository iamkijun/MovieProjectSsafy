<template>
    <div class="article-list row row-cols-1 row-cols-md-4 g-4">
      <ArticleListItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
      />
    </div>
  </template>
  
  <script>
  import ArticleListItem from '@/components/ArticleListItem'
  
  export default {
    name: 'ArticleList',
    components: {
      ArticleListItem
    },
    computed: {
      articles() {
        return this.$store.state.articles
      }
    }
  }
  </script>
  
  <style>
  .article-list {
    text-align: center;
    display:inline-block;
    /* transform: scale(1.3); */
    overflow: visible;
    cursor: pointer;
    z-index: 98;
  }
  </style>
  