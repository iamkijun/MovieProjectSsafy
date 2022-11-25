<template>
    <div id="searchpage">
      <br>
      <div id="searchrequire">
        <div class="search-form-input">
          <b-form-input id="input-default" 
          type="text"
          v-model="keyword"
          v-on:input="keywordChanged()"
          v-on:keyup.enter="searchresultshow(keyword)"
          >
          {{keyword}}
          </b-form-input>
        </div>
        <div class="search-form-button">
          <button @click="searchresultshow(keyword)">
            검색
          </button>
        </div>
      </div>
      <SearchResult v-if="isResultShow" v-bind:keyword="keyword"></SearchResult>
      <div v-else>
        아직 검색어를 입력하지 않았습니다.
      </div>
    </div>
  </template>

<script>
import SearchResult from "@/components/SearchResult.vue";

export default {
  name: "SearchPage",
  components: {
    SearchResult
  },
  data() {
    return {
      isResultShow:true,
      keyword: this.$route.params.keyword
    }
  },
  methods: {
    searchresultshow(keyword) {
      console.log('"',keyword,'"' + ' 검색')
      if (keyword !== ''){
        this.$router.push({
          name: "SearchPage",
          params: {
            keyword: this.keyword
          },
        })
        .then((res) => {
          console.log(res)
          this.searchList = res.data
        })
        .catch(()=>{});
        this.isResultShow = true
      } else {
        alert('검색어를 입력해주세요!')
      }
    },
    keywordChanged() {
      this.isResultShow = false
    }
  }
};
</script>

<style>

#searchrequire{
  justify-content: center;
  text-align: center;
}

.search-form-input{
  width:500px;
  text-align: center;
}

</style>1`1`