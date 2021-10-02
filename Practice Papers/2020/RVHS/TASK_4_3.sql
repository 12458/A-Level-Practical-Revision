SELECT s.Class, s.IndexNo FROM Student s
INNER JOIN Vote v ON v.MatricNo = s.MatricNo
INNER JOIN Candidate c ON c.CandidateNo = v.CandidateNo
WHERE c.Name = 'Ee Pei Chi Neoma' AND s.Class IN ('1A','1B','1C','1D','1E','1F','1G','1H','1I','1J','1K','1M');