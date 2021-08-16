SELECT * FROM School
INNER JOIN SchoolSubject
ON SchoolSubject.SchoolID = School.SchoolID
INNER JOIN Subject
ON SchoolSubject.SubjectID = Subject.SubjectID
AND SchoolSubject.Name = Subject.Name
WHERE School.Name = 'NANYANG JUNIOR COLLEGE';