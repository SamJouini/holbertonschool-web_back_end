-- Creates a view need_meeting listing
-- all students that have a score < 80
-- and +0 last_meeting for 1 month
CREATE VIEW need_meeting AS
    SELECT name FROM students
    WHERE score < 80
    AND (last_meeting IS NULL
    OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH)
    );
