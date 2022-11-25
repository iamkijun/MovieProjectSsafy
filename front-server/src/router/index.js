import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import ArticleView from '@/views/ArticleView'
import DetailView from '@/views/DetailView'
import RandomView from '@/views/RandomView'
import CreateView from '@/views/CreateView'
import MovieDetailView from '@/views/MovieDetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import SearchPage from '@/views/SearchPage'
import MvtiView from '@/views/MvtiView'
import RecommendView from '@/views/RecommendView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
  {
    path: '/articles',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  {
    path: '/random',
    name: 'random',
    component: RandomView
  },
  {
    path: '/searchpage/:keyword',
    name: 'SearchPage',
    component: SearchPage
  },
  {
    path: '/mvti',
    name: 'MvtiView',
    component: MvtiView
  },
  {
    path: '/movies/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/article/:id',
    name: 'DetailView',
    component: DetailView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
