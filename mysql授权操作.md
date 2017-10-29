
###  mysql授权操作

1. 创建用户
<pre>
create user 'test'@'%' identified by '123456';
create user 'only'@'192.168.1.2' identified by '123456'    # 创建only账号，只允许在192.168.1.2上用123456密码访问该数据库
</pre>
2. 删除用户
<pre>
drop user 'test'@'%'
</pre>
3. 修改密码
<pre>
set password for 'test'@'%' = password("123456"); 
</pre>
4. 授权
<pre>
grant insert on db.table1 to test@'%' identified by '123456';       # 授权test账号db数据库table1表的insert权限
grant select on db.table2 to test@'%' identified by '123456';       # 授权test账号db数据库table2表的select权限
grant delete on db.table3 to test@'%' identified by '123456';       # 授权test账号db数据库table3表的delete权限
grant all on *.* to test@'%' identified by '123456;              # 授权test账号所有数据库，所有表的所有权限
</pre>
5. 撤销权限
<pre>
revoke select on db.table1 from test@'%'
</pre>
