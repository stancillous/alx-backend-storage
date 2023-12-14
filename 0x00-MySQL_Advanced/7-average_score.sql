-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the
-- average score for a student
DELIMETER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id)
BEGIN
SELECT AVG(score) FROM users WHERE user_id = user_id;

END //
DELIMETER ;
