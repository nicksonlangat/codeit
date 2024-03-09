import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './index.css'
import mitt from 'mitt';


// import 'highlight.js/styles/stackoverflow-light.css'
// import hljs from 'highlight.js/lib/core';
// import 'highlight.js/lib/common';
// import javascript from 'highlight.js/lib/languages/javascript';
// import hljsVuePlugin from "@highlightjs/vue-plugin";
// import 'highlight.js/styles/stackoverflow-light.css'
import 'highlight.js/styles/tokyo-night-dark.min.css';
import hljs from 'highlight.js/lib/core';
import 'highlight.js/lib/common';
import hljsVuePlugin from "@highlightjs/vue-plugin";


// hljs.registerLanguage('javascript', javascript);


const emitter = mitt();

const app = createApp(App).use(store).use(router).use(hljsVuePlugin)

app.config.globalProperties.emitter = emitter;

app.mount('#app')
