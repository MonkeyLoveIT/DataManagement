-- 创建表格
create table mysql_test(
    id int primary key auto_increment,
    name varchar(30),
    age int(5),
    tag ENUM('Y', 'N') not null, -- 只能为Y或N
    created_by varchar(30),
    created_date TIMESTAMP not null default current_timestamp,
    updated_by varchar(30),
    updated_date TIMESTAMP not null default current_timestamp on update current_timestamp
);

-- 创建索引
create index index_test_created_by on mysql_test(created_by);

insert into mysql_test(name, age, tag) values ('a', 1, 'Y');

select * from mysql_test;

update mysql_test set age=2;

drop table mysql_test;

show tables;