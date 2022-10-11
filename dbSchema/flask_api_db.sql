-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Jun 29, 2022 at 09:55 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_api_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `user_id` int(11) NOT NULL,
  `admin_id` varchar(50) DEFAULT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`user_id`, `admin_id`, `enable`, `created_at`, `updated_at`) VALUES
(1, 'testCode1', 'Y', '2022-04-19 17:56:28', '2022-04-19 17:56:28'),
(5, 'testId', 'Y', '2022-05-27 15:31:22', '2022-05-27 15:31:22');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `course_id` int(11) NOT NULL,
  `course_name` varchar(100) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`course_id`, `course_name`, `enable`, `created_at`, `updated_at`) VALUES
(1, '2560', 'Y', '2022-06-29 03:28:17', '2022-06-29 03:28:17');

-- --------------------------------------------------------

--
-- Table structure for table `majors`
--

CREATE TABLE `majors` (
  `major_id` int(11) NOT NULL,
  `major_name` varchar(100) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `majors`
--

INSERT INTO `majors` (`major_id`, `major_name`, `enable`, `created_at`, `updated_at`) VALUES
(1, 'test', 'Y', '2022-05-27 15:45:59', '2022-05-27 15:45:59');

-- --------------------------------------------------------

--
-- Table structure for table `prename_list`
--

CREATE TABLE `prename_list` (
  `prename_id` int(11) NOT NULL,
  `prename_text` varchar(20) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prename_list`
--

INSERT INTO `prename_list` (`prename_id`, `prename_text`, `enable`, `created_at`, `updated_at`) VALUES
(1, 'นาย', 'Y', '2022-04-19 17:54:26', '2022-04-19 17:54:26'),
(2, 'นาง', 'Y', '2022-04-19 17:54:26', '2022-04-19 17:54:26'),
(3, 'นางสาว', 'Y', '2022-04-19 17:54:55', '2022-04-19 17:54:55'),
(4, 'อ.ดร', 'Y', '2022-04-19 17:54:55', '2022-04-19 17:54:55'),
(5, 'ผศ.ดร', 'Y', '2022-04-19 17:55:29', '2022-04-19 17:55:29'),
(6, 'ศ.ดร', 'Y', '2022-04-19 17:55:29', '2022-04-19 17:55:29');

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

CREATE TABLE `quiz` (
  `quiz_id` int(11) NOT NULL,
  `quiz_question` longtext NOT NULL,
  `quiz_answer` longtext NOT NULL,
  `quiz_point` decimal(20,2) NOT NULL,
  `quiz_standard` varchar(15) DEFAULT NULL COMMENT 'RESULT,RESULT_COMMAND',
  `quiz_group_id` int(11) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`quiz_id`, `quiz_question`, `quiz_answer`, `quiz_point`, `quiz_standard`, `quiz_group_id`, `enable`, `created_at`, `updated_at`) VALUES
(1, 'TEST QUESTION', 'SELECT QUESTION', '10.00', 'RESULT_COMMAND', 1, 'Y', '2022-06-29 03:30:28', '2022-06-29 03:30:28'),
(2, 'โจทย์', 'COMMAND', '10.00', 'RESULT', 5, 'Y', '2022-06-29 04:41:33', '2022-06-29 04:41:33'),
(3, 'โจทย์', 'COMMAND', '10.00', 'RESULT', 6, 'Y', '2022-06-29 04:41:53', '2022-06-29 04:41:53'),
(5, 'โจทย์', 'COMMAND', '10.00', 'RESULT', 8, 'Y', '2022-06-29 04:54:48', '2022-06-29 04:54:48');

-- --------------------------------------------------------

--
-- Table structure for table `quiz_groups`
--

CREATE TABLE `quiz_groups` (
  `quiz_group_id` int(11) NOT NULL,
  `database_id` int(11) NOT NULL,
  `quiz_objective` varchar(150) DEFAULT NULL,
  `quiz_num` int(11) NOT NULL DEFAULT 1,
  `quiz_type` varchar(10) NOT NULL COMMENT 'SELF,AUTO',
  `quiz_start_date` date DEFAULT NULL,
  `quiz_end_date` date DEFAULT NULL,
  `quiz_start_time` time NOT NULL,
  `quiz_end_time` time NOT NULL,
  `subject_group_id` int(11) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quiz_groups`
--

INSERT INTO `quiz_groups` (`quiz_group_id`, `database_id`, `quiz_objective`, `quiz_num`, `quiz_type`, `quiz_start_date`, `quiz_end_date`, `quiz_start_time`, `quiz_end_time`, `subject_group_id`, `enable`, `created_at`, `updated_at`) VALUES
(1, 1, 'test', 3, 'S', '2022-05-01', '2022-05-02', '10:00:00', '09:59:59', 1, 'Y', '2022-06-29 03:29:08', '2022-06-29 03:29:08'),
(3, 1, '', 1, 'SELF', '2022-05-02', '2022-05-02', '12:20:00', '15:19:59', 1, 'Y', '2022-06-29 04:37:57', '2022-06-29 04:37:57'),
(4, 1, '', 1, 'SELF', '2022-05-02', '2022-05-02', '12:20:00', '15:19:59', 1, 'Y', '2022-06-29 04:40:11', '2022-06-29 04:40:11'),
(5, 1, '', 1, 'SELF', '2022-05-02', '2022-05-02', '12:20:00', '15:19:59', 1, 'Y', '2022-06-29 04:41:33', '2022-06-29 04:41:33'),
(6, 1, '', 1, 'SELF', '2022-05-02', '2022-05-02', '12:20:00', '15:19:59', 1, 'Y', '2022-06-29 04:41:53', '2022-06-29 04:41:53'),
(8, 1, '', 1, 'SELF', '2022-05-02', '2022-05-02', '12:20:00', '15:19:59', 1, 'Y', '2022-06-29 04:54:48', '2022-06-29 04:54:48');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `user_id` int(11) NOT NULL,
  `student_id` varchar(50) DEFAULT NULL,
  `major_id` int(11) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `student_reg_subject_group`
--

CREATE TABLE `student_reg_subject_group` (
  `student_reg_subject_group_id` int(11) NOT NULL,
  `user_student_id` int(11) NOT NULL,
  `subject_group_id` int(11) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `student_test_result`
--

CREATE TABLE `student_test_result` (
  `student_test_result_id` int(11) NOT NULL,
  `student_reg_id` int(11) NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `do_point` decimal(20,2) NOT NULL,
  `quiz_answer` longtext NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `enable` varchar(5) NOT NULL DEFAULT 'Y'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL,
  `subject_code` varchar(50) NOT NULL,
  `subject_name` varchar(150) NOT NULL,
  `subject_decription` longtext DEFAULT NULL,
  `course_id` int(11) NOT NULL,
  `subject_year` varchar(10) DEFAULT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subject_id`, `subject_code`, `subject_name`, `subject_decription`, `course_id`, `subject_year`, `enable`, `created_at`, `updated_at`) VALUES
(1, '0010001', 'DB', 'DB', 1, '2565', 'Y', '2022-06-29 03:28:36', '2022-06-29 03:28:36');

-- --------------------------------------------------------

--
-- Table structure for table `subject_groups`
--

CREATE TABLE `subject_groups` (
  `subject_group_id` int(11) NOT NULL,
  `subject_group_name` varchar(20) NOT NULL,
  `user_id_teacher` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject_groups`
--

INSERT INTO `subject_groups` (`subject_group_id`, `subject_group_name`, `user_id_teacher`, `subject_id`, `enable`, `created_at`, `updated_at`) VALUES
(1, '700', 2, 1, 'Y', '2022-06-29 03:28:55', '2022-06-29 03:28:55');

-- --------------------------------------------------------

--
-- Table structure for table `system_databases`
--

CREATE TABLE `system_databases` (
  `database_id` int(11) NOT NULL,
  `database_name` varchar(50) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `system_databases`
--

INSERT INTO `system_databases` (`database_id`, `database_name`, `enable`, `created_at`, `updated_at`) VALUES
(1, 'test', 'Y', '2022-06-28 07:33:18', '2022-06-28 07:33:18'),
(2, 'test2', 'Y', '2022-06-28 11:02:14', '2022-06-28 11:02:14'),
(3, 'test2', 'Y', '2022-06-28 11:03:16', '2022-06-28 11:03:16'),
(4, 'test2', 'Y', '2022-06-28 11:04:48', '2022-06-28 11:04:48'),
(5, 'test2', 'Y', '2022-06-28 11:05:56', '2022-06-28 11:05:56');

-- --------------------------------------------------------

--
-- Table structure for table `system_tables`
--

CREATE TABLE `system_tables` (
  `system_table_id` int(11) NOT NULL,
  `system_database_id` int(11) NOT NULL,
  `system_table_name` varchar(150) NOT NULL,
  `comment` longtext NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `user_id` int(11) NOT NULL,
  `teacher_id` varchar(50) NOT NULL,
  `teacher_phone` varchar(10) NOT NULL,
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`user_id`, `teacher_id`, `teacher_phone`, `enable`, `created_at`, `updated_at`) VALUES
(2, '1', '0000000000', 'Y', '2022-05-08 21:04:56', '2022-05-08 21:04:56');

-- --------------------------------------------------------

--
-- Table structure for table `templates`
--

CREATE TABLE `templates` (
  `template_id` int(11) NOT NULL,
  `database_id` int(11) NOT NULL,
  `template_question` longtext NOT NULL,
  `template_command` longtext NOT NULL,
  `template_command_type` varchar(15) DEFAULT NULL COMMENT 'SELECT,INSERT,UPDATE,DELETE',
  `template_level` varchar(15) DEFAULT NULL COMMENT 'REMEMBER,UNDERSTAND,IMPLEMENT,ANALYSIS',
  `enable` varchar(5) NOT NULL DEFAULT 'Y'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `user_username` varchar(50) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_prename` int(11) NOT NULL,
  `user_firstname` varchar(50) DEFAULT NULL,
  `user_lastname` varchar(50) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL COMMENT 'STUDENT,TEACHER,ADMIN',
  `enable` varchar(5) NOT NULL DEFAULT 'Y',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_username`, `user_password`, `user_prename`, `user_firstname`, `user_lastname`, `user_email`, `user_type`, `enable`, `created_at`, `updated_at`) VALUES
(1, 'test', 'test', 1, 't', 't', NULL, 'ADMIN', 'Y', '2022-04-19 17:55:55', '2022-04-19 17:55:55'),
(2, 'test_teacher', 'test_teacher', 1, 'test_teacher', 'test_teacher', NULL, 'TEACHER', 'Y', '2022-05-08 21:04:14', '2022-05-08 21:04:14'),
(5, 'test_admin', 'test_password', 1, 'ADMIN', 'ADMIN', NULL, 'ADMIN', 'Y', '2022-05-27 15:31:22', '2022-05-27 15:31:22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `admin_id` (`admin_id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `majors`
--
ALTER TABLE `majors`
  ADD PRIMARY KEY (`major_id`);

--
-- Indexes for table `prename_list`
--
ALTER TABLE `prename_list`
  ADD PRIMARY KEY (`prename_id`),
  ADD KEY `prename_text` (`prename_text`);

--
-- Indexes for table `quiz`
--
ALTER TABLE `quiz`
  ADD PRIMARY KEY (`quiz_id`),
  ADD KEY `quiz_question` (`quiz_question`(768)),
  ADD KEY `quiz_answer` (`quiz_answer`(768)),
  ADD KEY `quiz_group_id` (`quiz_group_id`);

--
-- Indexes for table `quiz_groups`
--
ALTER TABLE `quiz_groups`
  ADD PRIMARY KEY (`quiz_group_id`),
  ADD KEY `database_id` (`database_id`),
  ADD KEY `quiz_start_date` (`quiz_start_date`),
  ADD KEY `quiz_end_date` (`quiz_end_date`),
  ADD KEY `subject_group_id` (`subject_group_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `major_id` (`major_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `student_reg_subject_group`
--
ALTER TABLE `student_reg_subject_group`
  ADD PRIMARY KEY (`student_reg_subject_group_id`),
  ADD KEY `user_student_id` (`user_student_id`),
  ADD KEY `subject_group_id` (`subject_group_id`);

--
-- Indexes for table `student_test_result`
--
ALTER TABLE `student_test_result`
  ADD PRIMARY KEY (`student_test_result_id`),
  ADD KEY `student_reg_id` (`student_reg_id`),
  ADD KEY `quiz_id` (`quiz_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subject_id`),
  ADD KEY `subject_code` (`subject_code`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `subject_groups`
--
ALTER TABLE `subject_groups`
  ADD PRIMARY KEY (`subject_group_id`),
  ADD KEY `user_id_teacher` (`user_id_teacher`),
  ADD KEY `subject_id` (`subject_id`);

--
-- Indexes for table `system_databases`
--
ALTER TABLE `system_databases`
  ADD PRIMARY KEY (`database_id`);

--
-- Indexes for table `system_tables`
--
ALTER TABLE `system_tables`
  ADD PRIMARY KEY (`system_table_id`),
  ADD KEY `system_database_id` (`system_database_id`),
  ADD KEY `system_table_name` (`system_table_name`),
  ADD KEY `comment` (`comment`(768));

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `teacher_phone` (`teacher_phone`);

--
-- Indexes for table `templates`
--
ALTER TABLE `templates`
  ADD PRIMARY KEY (`template_id`),
  ADD KEY `template_command_type` (`template_command_type`),
  ADD KEY `template_level` (`template_level`),
  ADD KEY `database_id` (`database_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_prename` (`user_prename`),
  ADD KEY `user_email` (`user_email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `majors`
--
ALTER TABLE `majors`
  MODIFY `major_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `prename_list`
--
ALTER TABLE `prename_list`
  MODIFY `prename_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `quiz`
--
ALTER TABLE `quiz`
  MODIFY `quiz_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `quiz_groups`
--
ALTER TABLE `quiz_groups`
  MODIFY `quiz_group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `student_reg_subject_group`
--
ALTER TABLE `student_reg_subject_group`
  MODIFY `student_reg_subject_group_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `student_test_result`
--
ALTER TABLE `student_test_result`
  MODIFY `student_test_result_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `subject_groups`
--
ALTER TABLE `subject_groups`
  MODIFY `subject_group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `system_databases`
--
ALTER TABLE `system_databases`
  MODIFY `database_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `system_tables`
--
ALTER TABLE `system_tables`
  MODIFY `system_table_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `templates`
--
ALTER TABLE `templates`
  MODIFY `template_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `quiz`
--
ALTER TABLE `quiz`
  ADD CONSTRAINT `quiz_ibfk_1` FOREIGN KEY (`quiz_group_id`) REFERENCES `quiz_groups` (`quiz_group_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `quiz_groups`
--
ALTER TABLE `quiz_groups`
  ADD CONSTRAINT `quiz_groups_ibfk_1` FOREIGN KEY (`database_id`) REFERENCES `system_databases` (`database_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `quiz_groups_ibfk_2` FOREIGN KEY (`subject_group_id`) REFERENCES `subject_groups` (`subject_group_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `students_ibfk_2` FOREIGN KEY (`major_id`) REFERENCES `majors` (`major_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student_reg_subject_group`
--
ALTER TABLE `student_reg_subject_group`
  ADD CONSTRAINT `student_reg_subject_group_ibfk_1` FOREIGN KEY (`user_student_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `student_reg_subject_group_ibfk_2` FOREIGN KEY (`subject_group_id`) REFERENCES `subject_groups` (`subject_group_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student_test_result`
--
ALTER TABLE `student_test_result`
  ADD CONSTRAINT `student_test_result_ibfk_1` FOREIGN KEY (`student_reg_id`) REFERENCES `student_reg_subject_group` (`student_reg_subject_group_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `student_test_result_ibfk_2` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subjects`
--
ALTER TABLE `subjects`
  ADD CONSTRAINT `subjects_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subject_groups`
--
ALTER TABLE `subject_groups`
  ADD CONSTRAINT `subject_groups_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `subject_groups_ibfk_2` FOREIGN KEY (`user_id_teacher`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `system_tables`
--
ALTER TABLE `system_tables`
  ADD CONSTRAINT `system_tables_ibfk_1` FOREIGN KEY (`system_database_id`) REFERENCES `system_databases` (`database_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `teachers`
--
ALTER TABLE `teachers`
  ADD CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `templates`
--
ALTER TABLE `templates`
  ADD CONSTRAINT `templates_ibfk_1` FOREIGN KEY (`database_id`) REFERENCES `system_databases` (`database_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`user_prename`) REFERENCES `prename_list` (`prename_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
