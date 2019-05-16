




* like查询  
    select * from table where col like '%word%' limit 2;


* 查询建表(查询的时候注意，要指定别名)  
    create table table_name1 as 
    select * from(
    select b.* from(
    select temp_id from table_name2 where dayid=0000 
    union all
    select temp_id from table_name3 where dayid=0000
    ) as a 
    left join (
    select * from table_name4
    ) as b on a.temp_id=b.temp_id
    )as c;


* 查看表结构  
    desc tablename
    
    
* 删除分区  
    alert table tablename drop if exists partition (dayid='0000')



* where 语句判断null  
    is null  或者  is not null 