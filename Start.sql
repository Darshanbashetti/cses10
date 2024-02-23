CREATE DATABASE Temp;

use temp;

CREATE TABLE student ( id INT PRIMARY KEY, name VARCHAR(255) );

Insert into student value(1,'darshan');

select * from student;
insert into student values (2, 'vinayak');

select * from student where id=1;
select name,id  from student where id=1;
drop table student;
drop database temp;