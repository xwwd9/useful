# mongo常用命令：
* 启动mongo服务：
    * 启动docker：docker run -itd --name mongo -p 27017:27017 mongo --auth
    * 进入shell，选择admin用户：docker exec -it mongo mongo admin
    * 创建用户：db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'}]});
    * 授权链接： db.auth('admin', '123456')
    * 创建一般用户：db.createUser({user: "pgy",pwd: "******",roles: [{role: "readWrite",db: "hope"}]})
    * 更新权限：db.grantRolesToUser("pgy", [{role:"root", db:"admin"}])
* 创建索引：db.company_contact.createIndex({"companyName": 1, "source": 1}, {"background": true, "unique":true})
* 查看当前索引：db.sentiment.getIndexes()
* 其他：
    * show dbs
    * show users
* 常用查询
    * 模糊查询
        ```
            1.查询包含XXX:{name:/xxx/}
            2.查询以XXX开头:{name:/^xxx/}
            3.查询以XXX结尾:{name:/xxx^/}
            4.查询忽略大小写:{name:/xxx/i}
        
            db.contacts.find({
                contact_type:3,
                contact_info:{ $regex:/.../}
            }).count()
        ```
    * 列表类型的一些操作
        ```
        sources是个列表类型，其中存的是字典,查询字段是否存在
        {
            ***:***
            "sources" : [
                {
                    "c" : "year",
                    "s" : "***",
                    "s_url" : "***"
                },
                {
                    "c" : "date",
                    "s" : "***",
                    "s_date" : ***,
                    "s_url" : "***"
                }
            ],
        }
        db.contacts.find({"sources.s_date":{$exists: true}})
           
        对sources.source_date为空的字段进行删除，应该可以直接单独使用unset进行操作
        db.contacts.update(
           { },
           { $unset: { "sources.$[elem].source_date" : "" } },
           { multi: true,
             arrayFilters: [ { "elem.source_date": "" } ]
           }
        )
        ```
  
  * remove操作
    ```
        db.contacts.remove({
            type:3,
            info:{ $regex:/.../}
        })
    ```
    
   * 数据中对象查询
        ```
            //插入测试数据
            db.test_pgy.insert(
                [
                    {
                    "sources":[{"category":"o2o"}]
                    },
                
                    {
                    "sources":[{"category":"b2b"}]
                    },
                
                    {
                    "sources":[{"category":"o2o"}, {"category":"b2b"}]
                    },
                    
                    {
                    "sources":[{"category":"o2o"}, {"category":"b2b"}]
                    },
                ]
            )
     
            //数组中如果有一个元素匹配的上，该集合就有效
            db.test_pgy.find({"sources":{ $elemMatch:{   category:{$ne:"b2b"}}       }          }   )
            
            
            //等于条件只要数组中有一个等于，该集合就匹配。
            //不等于条件需要数组中全部数据都不等于才匹配。
            db.test_pgy.find({"sources.category":{$ne:"b2b"}}   )
            db.test_pgy.find({"sources.category":{$eq:"b2b"}}   )

            //统计数组中符合条件的个数
            db.test_pgy.aggregate(
                [
                    {"$match":{"sources":{ $elemMatch:{   category:{$ne:"b2b"}}}}},
                    {"$project": {"sources":1}},
                    {"$unwind": "$sources"},
                    {"$match":{"sources.category":{$ne:"b2b"}}},
                ]
            
            )
     
     
        ```
     
    * 聚合查询
        ```
            $project: 过滤字段
            $match：匹配条件
            $unwind：拆分字段
        ```
      
      



* 导入导出
    https://www.runoob.com/mongodb/mongodb-linux-install.html
    export PATH=/usr/local/mongodb/bin:$PATH
    ```
        mongoexport --authenticationDatabase nbd_cloud_st -h dds-2ze1ef8846dcb504118410.mongodb.rds.aliyuncs.com:3717 -u nbd_cloud_st -p fanshan@2019  -d nbd_cloud_st -c clue_social_qixinbao -o  ./clue_social_qixinbao.json
        
        mongoimport --authenticationDatabase data_rawdb -h dds-2ze1ef8846dcb504118410.mongodb.rds.aliyuncs.com:3717 -u data_rawdb -p Raw_Fs2020  -d data_rawdb -c statistics --file ./a.json
    
    ```
