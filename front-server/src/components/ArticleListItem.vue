<template>
  <router-link :to="{ name: 'DetailView', params: { id: article.id } }">
    <div class="article-list-item">
      <img src="../assets/2052642.png" alt="압정" style="height: 20px; float: center; background-color: palegoldenrod;"/>
      <p></p>
      <p id="ali">제목 : {{ article.title }}</p>
      <p id="ali">작성자 : {{ article.username }}</p>
    </div>
  </router-link>
</template>
  
  <script>
  export default {
    name: 'ArticleListItem',
    props: {
      article: Object,
    },
    methods: {
      // deleteArticle() {
      //   console.log('삭제 메서드 호출!!')
      //   this.$store.dispatch('deleteArticle', this.article)
      //   // this.$store.commit('DELETE_TODO', this.todo)
      // },
    },
  }
  </script>
  
  <style>
  .article-list-item {
    text-align: center;
    display:inline-block;
    align-items: center;
    background-color: palegoldenrod;
    border : thick double lightyellow;
    margin: 1px 10px 1px;
    padding: 0px 20px 20px ;
  }
  #ali{
    background-color:  palegoldenrod;
    border-radius: 15px;
    color: black;
  }
  /* .overview {
  height: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  height: 6em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
} */

.article-list-item:hover { 
   transform: scale(1.3);
   overflow: visible;
   cursor: pointer;
   z-index: 98;
}

button {
  background-color: darkblue;
  /* padding: 5px 10px; */
  /* border-radius: 4px; */
  cursor: pointer;
}

#modal {
  display: none;
  position:relative;
  width:100%;
  height:100%;
  z-index:1;
}

#modal h2 {
  margin:0;
}
#modal button {
  display:inline-block;
  width:100px;
  margin-left:calc(100% - 100px - 10px);
}

#modal .modal_content {
  width:300px;
  margin:100px auto;
  padding:20px 10px;
  background:#fff;
  border:2px solid #666;
}

#modal .modal_layer {
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background:rgba(0, 0, 0, 0.5);
  z-index:-1;
}   
  </style>
  