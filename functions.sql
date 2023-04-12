create or replace function get_course_id_by_email(email varchar(50))
returns integer as
$body$
	select id from user_course as cour where 
	(select email from user_student where id=cour.student_id)=email;
$body$
language sql;

select get_course_id_by_email('aman@mail.ru');

