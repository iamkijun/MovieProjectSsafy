<template>
    <div>
      <div class="col">
        <div class="card h-200" style="border: 0px;">
          <!-- <img :src="this.movieURL" /> -->
          <router-link :to="{ name: 'MovieDetailView', params: { id: recommend_movie.id } }">
            <img :src="this.movieURL" style="height: 249px;"/>
          </router-link>
          <div class="card-body">
            <h5 class="text-center" style="font-weight: bold; font-size: 11pt; color: white;" >
              {{ recommend_movie.title }}
            </h5>
            <h5 class="overview">
              <p>{{ recommend_movie.overview }}</p>
            </h5>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RecommendListItem',
    props: {
      recommend_movie: Object,
    },
    computed: {
      movieURL() {
        return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${this.recommend_movie.poster_path}`
      },
    },
  }
  </script>
  
  <style>
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
  .overview {
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
  /* font-weight: bold;
  font-size: 9pt;
  color: black; */
}

.card:hover { 
   transition: transform .8s;
   transform: rotateY( 360deg );
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