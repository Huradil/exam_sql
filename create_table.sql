create table payments(
id serial primary key,
course_id integer references user_course(id),
amount integer,
pay_date date
);
insert into payments(course_id,amount,pay_date)
values
(
(select id from user_course where student_id=(select id from user_student where name like '%Aman%')),
15000,
'2022-08-15'
),
(
(select id from user_course where student_id=(select id from user_student where name like '%Alena%')),
55000,
'2022-08-05'
),
(
(select id from user_course where student_id=(select id from user_student where name like '%Phil%')),
5000,
'2022-08-25'
);

select * from user_student;
select * from payments;