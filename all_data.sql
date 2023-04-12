select st.name,cr.date_started,cr.name,men.name,l.name from user_student as st
left join user_course as cr on cr.student_id=st.id
left join user_mentor as men on men.id=cr.mentor_id
left join user_language as l on l.id=cr.language_id;