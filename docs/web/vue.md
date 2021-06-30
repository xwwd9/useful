




# elementui 使用

* 给表单添加校验
```vue
<el-form ref="dataForm" :model="form" :rules="rules" label-width="250px">
    <el-form-item  label="aa" prop="pickup_page"> 
        <el-input v-model.trim="form.pickup_page" @input="myinput"/>
    </el-form-item>
</el-form>

<script>
export default {
    data() {
        return {
            // 添加规则， rules，key是form中的prop， validator是自定义的验证器，trigger是触发验证的时机，默认blur可以自动触发，如果需要在其它时候触发，需要在其它触发函数中主动调用验证，比如当输入值改变的时候调用自定义的myinput函数然后主动触发
            rules: {
                pickup_page: [ {required: true,message: '请输入小写英文',trigger: 'blur', validator: this.pickupValiator}]
            }
        }      
    },
   
    methods: {
        myinput(a, b) { 
          console.log(this.refs, this.$refs)
          this.$refs.dataForm.validateField('pickup_page') // 主动触发函数
        },
    
        // 自定义的校验函数
        pickupValiator(rule, value, callback){
          const isMatched = value.match(/^[a-z]+$/)
          console.log(isMatched, 'asdf')
          if (!isMatched) {
            callback(new Error('格式不正确'))
          }
        }
    }
}
</script>

```