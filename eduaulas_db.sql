/*
SQLyog Community Edition- MySQL GUI v8.05 
MySQL - 5.1.58-community : Database - eduaulas_db
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`eduaulas_db` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `eduaulas_db`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add migration history',7,'add_migrationhistory'),(20,'Can change migration history',7,'change_migrationhistory'),(21,'Can delete migration history',7,'delete_migrationhistory'),(22,'Can add Aula',8,'add_classroom'),(23,'Can change Aula',8,'change_classroom'),(24,'Can delete Aula',8,'delete_classroom'),(25,'Can add Grado',9,'add_grade'),(26,'Can change Grado',9,'change_grade'),(27,'Can delete Grado',9,'delete_grade'),(28,'Can add Docente',10,'add_teacher'),(29,'Can change Docente',10,'change_teacher'),(30,'Can delete Docente',10,'delete_teacher'),(31,'Can add Resultado',11,'add_result'),(32,'Can change Resultado',11,'change_result'),(33,'Can delete Resultado',11,'delete_result'),(34,'Can add Ejercicio',12,'add_exercise'),(35,'Can change Ejercicio',12,'change_exercise'),(36,'Can delete Ejercicio',12,'delete_exercise'),(37,'Can add Comentario del docente',13,'add_teachercomments'),(38,'Can change Comentario del docente',13,'change_teachercomments'),(39,'Can delete Comentario del docente',13,'delete_teachercomments'),(40,'Can add Unidad',14,'add_unit'),(41,'Can change Unidad',14,'change_unit'),(42,'Can delete Unidad',14,'delete_unit'),(43,'Can add Area',15,'add_area'),(44,'Can change Area',15,'change_area'),(45,'Can delete Area',15,'delete_area'),(46,'Can add Materia',16,'add_subject'),(47,'Can change Materia',16,'change_subject'),(48,'Can delete Materia',16,'delete_subject'),(49,'Can add Escuela',17,'add_school'),(50,'Can change Escuela',17,'change_school'),(51,'Can delete Escuela',17,'delete_school'),(52,'Can add Departamento',18,'add_department'),(53,'Can change Departamento',18,'change_department'),(54,'Can delete Departamento',18,'delete_department'),(55,'Can add Pais',19,'add_country'),(56,'Can change Pais',19,'change_country'),(57,'Can delete Pais',19,'delete_country'),(58,'Can add Estudiante',20,'add_student'),(59,'Can change Estudiante',20,'change_student'),(60,'Can delete Estudiante',20,'delete_student'),(61,'Can add person',21,'add_person'),(62,'Can change person',21,'change_person'),(63,'Can delete person',21,'delete_person');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$12000$lRwkirdm0WmY$O6VOF3C93nw2kBIH0G+QxiI0KJYbZtObqi6NvCVqOH4=','2014-06-04 02:46:15',1,'root','','','bradelev@hotmail.com',1,1,'2014-06-04 02:20:11');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `classroom_classroom` */

DROP TABLE IF EXISTS `classroom_classroom`;

CREATE TABLE `classroom_classroom` (
  `code` varchar(5) NOT NULL,
  `class_letter` varchar(3) NOT NULL,
  `shift` varchar(20) NOT NULL,
  `grade_id` int(11) NOT NULL,
  PRIMARY KEY (`code`),
  KEY `classroom_classroom_d91b8533` (`grade_id`),
  CONSTRAINT `grade_id_refs_id_5794351f` FOREIGN KEY (`grade_id`) REFERENCES `classroom_grade` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `classroom_classroom` */

insert  into `classroom_classroom`(`code`,`class_letter`,`shift`,`grade_id`) values ('efr5g','A','OTHER',2),('fffrr','B','OTHER',2);

/*Table structure for table `classroom_classroom_teachers` */

DROP TABLE IF EXISTS `classroom_classroom_teachers`;

CREATE TABLE `classroom_classroom_teachers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classroom_id` varchar(5) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `classroom_id` (`classroom_id`,`teacher_id`),
  KEY `classroom_classroom_teachers_8b2e9f8d` (`classroom_id`),
  KEY `classroom_classroom_teachers_c12e9d48` (`teacher_id`),
  CONSTRAINT `teacher_id_refs_person_ptr_id_83d1ba20` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_teacher` (`person_ptr_id`),
  CONSTRAINT `classroom_id_refs_code_35cb1327` FOREIGN KEY (`classroom_id`) REFERENCES `classroom_classroom` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `classroom_classroom_teachers` */

/*Table structure for table `classroom_grade` */

DROP TABLE IF EXISTS `classroom_grade`;

CREATE TABLE `classroom_grade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `classroom_grade` */

insert  into `classroom_grade`(`id`,`name`) values (2,1),(3,2);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`user_id`,`content_type_id`,`object_id`,`object_repr`,`action_flag`,`change_message`) values (1,'2014-06-04 02:47:35',1,16,'1','Quimica',1,''),(2,'2014-06-04 02:47:38',1,16,'2','Fisica',1,''),(3,'2014-06-04 02:47:54',1,15,'1','Ciencias Naturales',1,''),(4,'2014-06-04 02:48:00',1,15,'2','Ciencias Sociales',1,''),(5,'2014-06-04 02:48:16',1,14,'1','A. El agua como solvente',1,''),(6,'2014-06-04 02:48:26',1,14,'2','B. El movimiento',1,''),(7,'2014-06-04 02:48:51',1,12,'1','Exercise object',1,''),(8,'2014-06-04 02:49:10',1,12,'2','Exercise object',1,''),(9,'2014-06-04 02:49:35',1,12,'3','Exercise object',1,''),(10,'2014-06-04 02:52:07',1,10,'2','Estela Gonzalez',1,'');

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`name`,`app_label`,`model`) values (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'migration history','south','migrationhistory'),(8,'Aula','classroom','classroom'),(9,'Grado','classroom','grade'),(10,'Docente','teacher','teacher'),(11,'Resultado','exercise','result'),(12,'Ejercicio','exercise','exercise'),(13,'Comentario del docente','exercise','teachercomments'),(14,'Unidad','exercise','unit'),(15,'Area','exercise','area'),(16,'Materia','exercise','subject'),(17,'Escuela','location','school'),(18,'Departamento','location','department'),(19,'Pais','location','country'),(20,'Estudiante','student','student'),(21,'person','person','person');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('55k4qpzmjgmfyuphhqlysv6dm62ihv3g','MDhlYWVlNDVkMDllMjI2NDg3MjdiZmU2NzQzNjZmZGVmOTBkYjgzODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-06-18 02:46:15'),('6qntjukula0sfckpqu14mdi06dslo1kq','MDhlYWVlNDVkMDllMjI2NDg3MjdiZmU2NzQzNjZmZGVmOTBkYjgzODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-06-18 02:22:34');

/*Table structure for table `exercise_area` */

DROP TABLE IF EXISTS `exercise_area`;

CREATE TABLE `exercise_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `exercise_area` */

insert  into `exercise_area`(`id`,`name`) values (1,'Ciencias Naturales'),(2,'Ciencias Sociales');

/*Table structure for table `exercise_exercise` */

DROP TABLE IF EXISTS `exercise_exercise`;

CREATE TABLE `exercise_exercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `grade_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `unit_id` int(11) NOT NULL,
  `exercise_type` varchar(50) NOT NULL,
  `teacher_guide` longtext NOT NULL,
  `img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exercise_exercise_d91b8533` (`grade_id`),
  KEY `exercise_exercise_56bb4187` (`subject_id`),
  KEY `exercise_exercise_b9dcc52b` (`unit_id`),
  CONSTRAINT `subject_id_refs_id_8ce323a6` FOREIGN KEY (`subject_id`) REFERENCES `exercise_subject` (`id`),
  CONSTRAINT `grade_id_refs_id_1bb226d2` FOREIGN KEY (`grade_id`) REFERENCES `classroom_grade` (`id`),
  CONSTRAINT `unit_id_refs_id_a09f2871` FOREIGN KEY (`unit_id`) REFERENCES `exercise_unit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `exercise_exercise` */

insert  into `exercise_exercise`(`id`,`exercise_id`,`grade_id`,`subject_id`,`unit_id`,`exercise_type`,`teacher_guide`,`img`) values (1,1,2,1,1,'TRUE_FALSE','',''),(2,2,2,1,1,'DRAG_AND_DROP','',''),(3,3,2,2,2,'DRAG_AND_DROP','','');

/*Table structure for table `exercise_exercise_bad_related_exercises` */

DROP TABLE IF EXISTS `exercise_exercise_bad_related_exercises`;

CREATE TABLE `exercise_exercise_bad_related_exercises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_exercise_id` int(11) NOT NULL,
  `to_exercise_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_exercise_id` (`from_exercise_id`,`to_exercise_id`),
  KEY `exercise_exercise_bad_related_exercises_cb28bbe1` (`from_exercise_id`),
  KEY `exercise_exercise_bad_related_exercises_c0e587b5` (`to_exercise_id`),
  CONSTRAINT `to_exercise_id_refs_id_c76c2973` FOREIGN KEY (`to_exercise_id`) REFERENCES `exercise_exercise` (`id`),
  CONSTRAINT `from_exercise_id_refs_id_c76c2973` FOREIGN KEY (`from_exercise_id`) REFERENCES `exercise_exercise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `exercise_exercise_bad_related_exercises` */

/*Table structure for table `exercise_exercise_good_related_exercises` */

DROP TABLE IF EXISTS `exercise_exercise_good_related_exercises`;

CREATE TABLE `exercise_exercise_good_related_exercises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_exercise_id` int(11) NOT NULL,
  `to_exercise_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_exercise_id` (`from_exercise_id`,`to_exercise_id`),
  KEY `exercise_exercise_good_related_exercises_cb28bbe1` (`from_exercise_id`),
  KEY `exercise_exercise_good_related_exercises_c0e587b5` (`to_exercise_id`),
  CONSTRAINT `to_exercise_id_refs_id_5747f221` FOREIGN KEY (`to_exercise_id`) REFERENCES `exercise_exercise` (`id`),
  CONSTRAINT `from_exercise_id_refs_id_5747f221` FOREIGN KEY (`from_exercise_id`) REFERENCES `exercise_exercise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `exercise_exercise_good_related_exercises` */

/*Table structure for table `exercise_result` */

DROP TABLE IF EXISTS `exercise_result`;

CREATE TABLE `exercise_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `points` double DEFAULT NULL,
  `answer` longtext,
  `exercise_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `time_elapsed` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `exercise_result_c18e0af4` (`exercise_id`),
  KEY `exercise_result_94741166` (`student_id`),
  CONSTRAINT `exercise_id_refs_id_2157aa32` FOREIGN KEY (`exercise_id`) REFERENCES `exercise_exercise` (`id`),
  CONSTRAINT `student_id_refs_person_ptr_id_a23f675b` FOREIGN KEY (`student_id`) REFERENCES `student_student` (`person_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `exercise_result` */

insert  into `exercise_result`(`id`,`points`,`answer`,`exercise_id`,`student_id`,`time_elapsed`) values (2,0.6,NULL,2,6,NULL),(5,0.3,NULL,1,6,NULL),(6,1,NULL,2,7,NULL),(7,0.5,NULL,1,7,NULL),(8,0.4,NULL,1,10,NULL),(9,1,NULL,2,8,NULL),(10,1,NULL,1,8,NULL),(12,0.2,NULL,2,10,NULL);

/*Table structure for table `exercise_subject` */

DROP TABLE IF EXISTS `exercise_subject`;

CREATE TABLE `exercise_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `exercise_subject` */

insert  into `exercise_subject`(`id`,`name`) values (1,'Quimica'),(2,'Fisica');

/*Table structure for table `exercise_teachercomments` */

DROP TABLE IF EXISTS `exercise_teachercomments`;

CREATE TABLE `exercise_teachercomments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) NOT NULL,
  `comments` longtext NOT NULL,
  `exercise_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exercise_teachercomments_c12e9d48` (`teacher_id`),
  KEY `exercise_teachercomments_c18e0af4` (`exercise_id`),
  CONSTRAINT `exercise_id_refs_id_f8410c4f` FOREIGN KEY (`exercise_id`) REFERENCES `exercise_exercise` (`id`),
  CONSTRAINT `teacher_id_refs_person_ptr_id_b8c1e566` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_teacher` (`person_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `exercise_teachercomments` */

/*Table structure for table `exercise_unit` */

DROP TABLE IF EXISTS `exercise_unit`;

CREATE TABLE `exercise_unit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `letter` varchar(1) NOT NULL,
  `name` varchar(150) NOT NULL,
  `description` longtext NOT NULL,
  `subject_id` int(11) NOT NULL,
  `available` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exercise_unit_56bb4187` (`subject_id`),
  CONSTRAINT `subject_id_refs_id_ec004977` FOREIGN KEY (`subject_id`) REFERENCES `exercise_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `exercise_unit` */

insert  into `exercise_unit`(`id`,`letter`,`name`,`description`,`subject_id`,`available`) values (1,'A','El agua como solvente','',1,1),(2,'B','El movimiento','f',2,1);

/*Table structure for table `location_country` */

DROP TABLE IF EXISTS `location_country`;

CREATE TABLE `location_country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location_country` */

/*Table structure for table `location_department` */

DROP TABLE IF EXISTS `location_department`;

CREATE TABLE `location_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `location_department_d860be3c` (`country_id`),
  CONSTRAINT `country_id_refs_id_7e566d4a` FOREIGN KEY (`country_id`) REFERENCES `location_country` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location_department` */

/*Table structure for table `location_school` */

DROP TABLE IF EXISTS `location_school`;

CREATE TABLE `location_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `location_school_69d14838` (`department_id`),
  CONSTRAINT `department_id_refs_id_795b1fae` FOREIGN KEY (`department_id`) REFERENCES `location_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location_school` */

/*Table structure for table `person_person` */

DROP TABLE IF EXISTS `person_person`;

CREATE TABLE `person_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `serial` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `person_person` */

insert  into `person_person`(`id`,`name`,`last_name`,`date_of_birth`,`gender`,`serial`) values (2,'Estela','Gonzalez','2014-06-03','FEMALE','sss'),(6,'Maria','Lacalle',NULL,'',''),(7,'Federico','Gonzalez',NULL,'',''),(8,'Jorge','Orecchia',NULL,'',''),(10,'Agustina','Lopez',NULL,'','');

/*Table structure for table `south_migrationhistory` */

DROP TABLE IF EXISTS `south_migrationhistory`;

CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `south_migrationhistory` */

/*Table structure for table `student_student` */

DROP TABLE IF EXISTS `student_student`;

CREATE TABLE `student_student` (
  `person_ptr_id` int(11) NOT NULL,
  `class_room_id` varchar(5) NOT NULL,
  PRIMARY KEY (`person_ptr_id`),
  KEY `student_student_45e2f3cc` (`class_room_id`),
  CONSTRAINT `person_ptr_id_refs_id_065e9448` FOREIGN KEY (`person_ptr_id`) REFERENCES `person_person` (`id`),
  CONSTRAINT `class_room_id_refs_code_f832d64b` FOREIGN KEY (`class_room_id`) REFERENCES `classroom_classroom` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_student` */

insert  into `student_student`(`person_ptr_id`,`class_room_id`) values (6,'efr5g'),(7,'efr5g'),(8,'efr5g'),(10,'efr5g');

/*Table structure for table `teacher_teacher` */

DROP TABLE IF EXISTS `teacher_teacher`;

CREATE TABLE `teacher_teacher` (
  `person_ptr_id` int(11) NOT NULL,
  `email` varchar(75) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`person_ptr_id`),
  CONSTRAINT `person_ptr_id_refs_id_f8e02444` FOREIGN KEY (`person_ptr_id`) REFERENCES `person_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `teacher_teacher` */

insert  into `teacher_teacher`(`person_ptr_id`,`email`,`nickname`,`password`) values (2,'gatomanya09@hotmail.com','estela','estela');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
