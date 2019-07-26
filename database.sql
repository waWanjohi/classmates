BEGIN;

--
-- Database: `db`
--
CREATE DATABASE IF NOT EXISTS `db` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db`;

-- --------------------------------------------------------
--
-- Table structure for a student:
-- Create model Student
--
CREATE TABLE "student_student" (
	"sid" integer NOT NULL PRIMARY KEY, 
	"sname" varchar(100) NOT NULL, 
	"sgender" varchar(6) NOT NULL, 
	"srow" integer NOT NULL
	) ENGINE=InnoDB  DEFAULT CHARSET=latin1;
COMMIT;