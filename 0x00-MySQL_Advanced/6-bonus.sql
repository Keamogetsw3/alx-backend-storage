-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- Requirements:
-- Procedure AddBonus is taking 3 inputs (in this order):
-- 1. user_id, a users.id value (you can assume user_id is linked to an existing users).
-- 2. project_name, a new or already exists projects - if no projects.name found in the table, you should create it.
-- 3. score, the score value for the correction.

DELIMITER $$ ;
CREATE PROCEDURE AddBonus(
	IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER
)
BEGIN
	IF NOT EXISTS(SELECT name FROM projects WHERE name=project_name) THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, (SELECT id from projects WHERE name=project_name), score);
END;$$
DELIMITER ;
