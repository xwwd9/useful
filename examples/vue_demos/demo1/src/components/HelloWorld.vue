<template>
  <div class="container">
    <ul class="list-group">
      <li class="list-group-item" v-for="(item, index) in lists" :key="index" >
        {{item}}
      </li>
    </ul>
  </div>

</template>

<script>
import {reactive, toRefs} from "vue"

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  setup() {
    const state = reactive({
      lists : [1,2,3]
    })
    return toRefs(state)
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
