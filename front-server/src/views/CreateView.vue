<template>
  <div>
    <br>
    <h1>게시글 작성</h1>
    <br>
    <form @submit.prevent="createArticle">
      <label for="title">제 목</label>
      <br>
      <input type="text" id="title" v-model.trim="title"><br>
      <br>
      <label for="content">내 용</label>
      <br>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <button type="submit" id="submit" class="btn btn-primary">작성하기</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        data: {
          title: title,
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'ArticleView' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
#postit{
  background-color: palegoldenrod ;
}
</style>
