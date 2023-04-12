select * from payments;

select sum(amount) as sum_amount,(select name from user_language where id=(select language_id from user_course where id=course_id))
as language
from payments
group by language;