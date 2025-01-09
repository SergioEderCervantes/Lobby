-- MySQL dump 10.13  Distrib 8.4.0, for Win64 (x86_64)
--
-- Host: localhost    Database: lobby
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_emailaddress`
--

DROP TABLE IF EXISTS `account_emailaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_emailaddress_user_id_email_987c8728_uniq` (`user_id`,`email`),
  KEY `account_emailaddress_email_03be32b2` (`email`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailaddress`
--

LOCK TABLES `account_emailaddress` WRITE;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_emailconfirmation`
--

DROP TABLE IF EXISTS `account_emailconfirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailconfirmation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailconfirmation`
--

LOCK TABLES `account_emailconfirmation` WRITE;
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add site',6,'add_site'),(22,'Can change site',6,'change_site'),(23,'Can delete site',6,'delete_site'),(24,'Can view site',6,'view_site'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add email address',8,'add_emailaddress'),(30,'Can change email address',8,'change_emailaddress'),(31,'Can delete email address',8,'delete_emailaddress'),(32,'Can view email address',8,'view_emailaddress'),(33,'Can add email confirmation',9,'add_emailconfirmation'),(34,'Can change email confirmation',9,'change_emailconfirmation'),(35,'Can delete email confirmation',9,'delete_emailconfirmation'),(36,'Can view email confirmation',9,'view_emailconfirmation'),(37,'Can add social account',10,'add_socialaccount'),(38,'Can change social account',10,'change_socialaccount'),(39,'Can delete social account',10,'delete_socialaccount'),(40,'Can view social account',10,'view_socialaccount'),(41,'Can add social application',11,'add_socialapp'),(42,'Can change social application',11,'change_socialapp'),(43,'Can delete social application',11,'delete_socialapp'),(44,'Can view social application',11,'view_socialapp'),(45,'Can add social application token',12,'add_socialtoken'),(46,'Can change social application token',12,'change_socialtoken'),(47,'Can delete social application token',12,'delete_socialtoken'),(48,'Can view social application token',12,'view_socialtoken'),(49,'Can add promocion',13,'add_promocion'),(50,'Can change promocion',13,'change_promocion'),(51,'Can delete promocion',13,'delete_promocion'),(52,'Can view promocion',13,'view_promocion'),(53,'Can add sucursal',14,'add_sucursal'),(54,'Can change sucursal',14,'change_sucursal'),(55,'Can delete sucursal',14,'delete_sucursal'),(56,'Can view sucursal',14,'view_sucursal'),(57,'Can add sucursal_ producto',15,'add_sucursal_producto'),(58,'Can change sucursal_ producto',15,'change_sucursal_producto'),(59,'Can delete sucursal_ producto',15,'delete_sucursal_producto'),(60,'Can view sucursal_ producto',15,'view_sucursal_producto'),(61,'Can add sucursal_ promocion',16,'add_sucursal_promocion'),(62,'Can change sucursal_ promocion',16,'change_sucursal_promocion'),(63,'Can delete sucursal_ promocion',16,'delete_sucursal_promocion'),(64,'Can view sucursal_ promocion',16,'view_sucursal_promocion'),(65,'Can add comment',17,'add_comment'),(66,'Can change comment',17,'change_comment'),(67,'Can delete comment',17,'delete_comment'),(68,'Can view comment',17,'view_comment'),(69,'Can add reservation',18,'add_reservation'),(70,'Can change reservation',18,'change_reservation'),(71,'Can delete reservation',18,'delete_reservation'),(72,'Can view reservation',18,'view_reservation'),(73,'Can add consola',19,'add_consola'),(74,'Can change consola',19,'change_consola'),(75,'Can delete consola',19,'delete_consola'),(76,'Can view consola',19,'view_consola'),(77,'Can add consola_disponibilidad',20,'add_consola_disponibilidad'),(78,'Can change consola_disponibilidad',20,'change_consola_disponibilidad'),(79,'Can delete consola_disponibilidad',20,'delete_consola_disponibilidad'),(80,'Can view consola_disponibilidad',20,'view_consola_disponibilidad'),(81,'Can add torneo',21,'add_torneo'),(82,'Can change torneo',21,'change_torneo'),(83,'Can delete torneo',21,'delete_torneo'),(84,'Can view torneo',21,'view_torneo'),(85,'Can add producto',22,'add_producto'),(86,'Can change producto',22,'change_producto'),(87,'Can delete producto',22,'delete_producto'),(88,'Can view producto',22,'view_producto'),(89,'Can add seccion_productos',23,'add_seccion_productos'),(90,'Can change seccion_productos',23,'change_seccion_productos'),(91,'Can delete seccion_productos',23,'delete_seccion_productos'),(92,'Can view seccion_productos',23,'view_seccion_productos');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (179,'2025-01-09 04:09:03.022671','2','Seccion de Cerveza',2,'[{\"changed\": {\"fields\": [\"Imagen de apoyo 1\"]}}]',23,35),(180,'2025-01-09 04:09:42.028643','5','Seccion de Bebidas Con Alcohol',2,'[{\"changed\": {\"fields\": [\"Imagen de apoyo 1\"]}}]',23,35);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'account','emailaddress'),(9,'account','emailconfirmation'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(17,'lobby','comment'),(13,'lobby','promocion'),(14,'lobby','sucursal'),(15,'lobby','sucursal_producto'),(16,'lobby','sucursal_promocion'),(19,'reservations','consola'),(20,'reservations','consola_disponibilidad'),(18,'reservations','reservation'),(22,'restaurante','producto'),(23,'restaurante','seccion_productos'),(5,'sessions','session'),(6,'sites','site'),(10,'socialaccount','socialaccount'),(11,'socialaccount','socialapp'),(12,'socialaccount','socialtoken'),(21,'tournaments','torneo'),(7,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-12-19 22:35:12.637447'),(2,'contenttypes','0002_remove_content_type_name','2024-12-19 22:35:12.701025'),(3,'auth','0001_initial','2024-12-19 22:35:12.893999'),(4,'auth','0002_alter_permission_name_max_length','2024-12-19 22:35:12.960991'),(5,'auth','0003_alter_user_email_max_length','2024-12-19 22:35:12.960991'),(6,'auth','0004_alter_user_username_opts','2024-12-19 22:35:12.978531'),(7,'auth','0005_alter_user_last_login_null','2024-12-19 22:35:12.982193'),(8,'auth','0006_require_contenttypes_0002','2024-12-19 22:35:12.982193'),(9,'auth','0007_alter_validators_add_error_messages','2024-12-19 22:35:12.989046'),(10,'auth','0008_alter_user_username_max_length','2024-12-19 22:35:12.997159'),(11,'auth','0009_alter_user_last_name_max_length','2024-12-19 22:35:12.997159'),(12,'auth','0010_alter_group_name_max_length','2024-12-19 22:35:13.013469'),(13,'auth','0011_update_proxy_permissions','2024-12-19 22:35:13.016769'),(14,'auth','0012_alter_user_first_name_max_length','2024-12-19 22:35:13.024311'),(15,'users','0001_initial','2024-12-19 22:35:13.154373'),(16,'account','0001_initial','2024-12-19 22:35:13.298203'),(17,'account','0002_email_max_length','2024-12-19 22:35:13.320324'),(18,'account','0003_alter_emailaddress_create_unique_verified_email','2024-12-19 22:35:13.342503'),(19,'account','0004_alter_emailaddress_drop_unique_email','2024-12-19 22:35:13.379187'),(20,'account','0005_emailaddress_idx_upper_email','2024-12-19 22:35:13.401622'),(21,'account','0006_emailaddress_lower','2024-12-19 22:35:13.415206'),(22,'account','0007_emailaddress_idx_email','2024-12-19 22:35:13.450024'),(23,'account','0008_emailaddress_unique_primary_email_fixup','2024-12-19 22:35:13.461880'),(24,'account','0009_emailaddress_unique_primary_email','2024-12-19 22:35:13.467930'),(25,'admin','0001_initial','2024-12-19 22:35:13.581806'),(26,'admin','0002_logentry_remove_auto_add','2024-12-19 22:35:13.581806'),(27,'admin','0003_logentry_add_action_flag_choices','2024-12-19 22:35:13.598607'),(28,'restaurante','0001_initial','2024-12-19 22:35:13.611315'),(29,'lobby','0001_initial','2024-12-19 22:35:13.842095'),(30,'lobby','0002_comments','2024-12-19 22:35:13.959210'),(31,'lobby','0003_rename_comments_comment','2024-12-19 22:35:13.982275'),(32,'reservations','0001_initial','2024-12-19 22:35:14.058969'),(33,'reservations','0002_initial','2024-12-19 22:35:14.119792'),(34,'reservations','0003_consola_reservation_consola_seleccionada_and_more','2024-12-19 22:35:14.326624'),(35,'reservations','0004_remove_reservation_telefono','2024-12-19 22:35:14.345767'),(36,'sessions','0001_initial','2024-12-19 22:35:14.362396'),(37,'sites','0001_initial','2024-12-19 22:35:14.380909'),(38,'sites','0002_alter_domain_unique','2024-12-19 22:35:14.402039'),(39,'socialaccount','0001_initial','2024-12-19 22:35:14.720907'),(40,'socialaccount','0002_token_max_lengths','2024-12-19 22:35:14.783402'),(41,'socialaccount','0003_extra_data_default_dict','2024-12-19 22:35:14.792240'),(42,'socialaccount','0004_app_provider_id_settings','2024-12-19 22:35:14.913666'),(43,'socialaccount','0005_socialtoken_nullable_app','2024-12-19 22:35:15.031288'),(44,'socialaccount','0006_alter_socialaccount_extra_data','2024-12-19 22:35:15.132228'),(45,'tournaments','0001_initial','2024-12-19 22:35:15.160756'),(46,'tournaments','0002_initial','2024-12-19 22:35:15.281643'),(47,'users','0002_user_telefono','2024-12-19 22:35:15.325554'),(48,'users','0003_alter_user_email_alter_user_telefono','2024-12-19 22:35:15.510992'),(49,'users','0004_user_juegos_inscritos','2024-12-19 22:35:15.599362'),(50,'users','0005_alter_user_telefono','2024-12-22 20:37:06.174308'),(51,'lobby','0004_promocion_imagen_promocion_nombre_and_more','2024-12-22 22:01:11.117382'),(52,'lobby','0005_alter_promocion_nombre','2024-12-26 02:23:23.173054'),(53,'restaurante','0002_seccion_productos_producto_seccion_producto','2024-12-26 02:23:23.270000'),(54,'restaurante','0003_alter_seccion_productos_options_and_more','2024-12-26 02:56:45.052201'),(55,'restaurante','0004_alter_seccion_productos_nombre_seccion','2024-12-26 02:58:55.309136'),(56,'users','0006_alter_user_telefono','2024-12-30 18:57:14.001207'),(57,'users','0007_user_avatar_alter_user_telefono','2024-12-30 18:57:14.219452'),(58,'tournaments','0003_torneo_requisitos','2024-12-30 21:23:48.615860'),(59,'tournaments','0004_alter_torneo_descripcion_alter_torneo_reglas_and_more','2024-12-30 21:35:09.281038'),(60,'tournaments','0005_remove_torneo_requisitos_alter_torneo_descripcion_and_more','2025-01-02 22:04:52.360568'),(61,'tournaments','0006_torneo_requisitos_alter_torneo_descripcion_and_more','2025-01-02 22:04:52.399041'),(62,'users','0008_alter_user_telefono','2025-01-02 22:04:52.461740'),(63,'lobby','0006_alter_comment_options_alter_promocion_options_and_more','2025-01-08 17:19:04.347312'),(64,'reservations','0005_alter_consola_disponibilidad_options_and_more','2025-01-08 17:19:04.366631'),(65,'restaurante','0005_alter_seccion_productos_options','2025-01-08 17:19:04.369802'),(66,'tournaments','0007_alter_torneo_modo_torneo','2025-01-08 17:19:04.382219');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4reqhqxqh5nlave1r5imeahxbmnbf25r','.eJxVkMFqwzAQRP9lz8ZItWXLvrX3QiDHUsxKu47V1FKQZNoS8u-12lxyW2bezMJcAa0Nm88Tbnlhn53F7IKfVs5LoATj2xX-bxjhgil9hUhQAWYYZd-oQale63oQTatkW8GWOHpceaeP5xBP_Eyr84cY4PZewd-XqTCTK4UNPGgG7Zl9MegD_SnUNvgcnakLUt_dVL8G4s-XO_tQsGBa9rQmiVqT6WTbdU84U7tne2y0mRsUKAV33CtjdKtYd7hPIOdBsBWkSNAsSmnilMoQ_H1x8QdGcfsFW3hk3Q:1tTtOu:Biitp0dPpxiXIszwoa9yy2IpgJpcthBlcZ41Nwat7wU','2025-01-18 01:56:28.947040'),('7k0wmh0ab7q8eczqg0oqsibo4q4vb47u','.eJxVkMFuhDAMRP_FZ4QSSCBwa-899VhVyInNkm5JViSorVb77yXtXvZmed6MNb4COhf3kCfc88Ihe4fZxzCtnJdICca3K_zPMMIFU_qKG0EFmGGUfauNHuTQ1EOjtWpUBXviLeDKB_16jtuJn2j1AW7vFfydmAow-ZLWwsPOojtzKAJ9YDjF2sWQN2_rgtR3NdUvkfjz-c4-BCyYlsNtSKIxZDupuq7BmdTh7bE1dm5RoBTcca-tNUqz6fDoL-dBsBOkSdAsSmjilMoX-Pvitx8Yxe0XByFjqQ:1tTUGu:vLn_PMTyvtzb5qkTqYtlyiVfHRA3d4auk3VVoYTASYc','2025-01-16 23:06:32.954755'),('avw68r1cfgu4nvowpf72mdtgltsf4bm1','.eJxVjDEOAiEQRe9CbQgywIClvWcgA4OyaiBZdivj3XWTLbT9773_EpHWpcZ1lDlOLE4CrDj8jonyo7SN8J3arcvc2zJPSW6K3OmQl87led7dv4NKo37r4BVp7bR16AqAQWeREKyhjBaPOSnmgCWkkL1hto5BFyDPVw0ZlBHvD9qLN1k:1tVjjh:ecfP3IB7BX7yxe69Mx88I1-ozlDdsKHfhDnWd00LbbA','2025-01-23 04:01:33.357551'),('cy7uyqn8h8qzs6dx6xzod35y55bhefft','.eJxVkLFuwzAMRP-Fs2FIsSWr3tq9U8eiMCiRjtXEUiDJaIsg_16rzZKN4L074ngFdC5uoUy4lYVD8Q6Lj2FauSyRMozvV_ifYYQL5vwVE0EDWGCUQ6c7paU6tKoflFC6gS1zCrjyTr-dYjryM60-wO2jgb8TUwUmX9M6eNhZdCcOVaBPDMfYuhhK8ratSHtXc_saic8vd_YhYMG87G5DEo0hq2Wv9QFn6nfvgJ2xc4cCpWDNg7LW9IqNxr2_nJ8EO0GKBM2ihmbOuX6Bvy8-_cAobr_-AWOf:1tVZYO:KQKDahERT7_7wcNMArk1aPyhuLx89E48eqO-Ck7DcAQ','2025-01-22 17:09:12.581424'),('fbeqowypenwx2t01gvwcw9lvo38xft3a','.eJxVjDsOgzAQRO-ydYTwLwa6cBFr8a6FFcdIYKeJcvdAREM5b2beB9D7pebi3rzGEJkcvzAmGHJN6QYOa5ld3Xh1kWAACRc2oX9yPgpM6cDNqWv-m7PemseeOJfoscQlj-froppxm3dPICOMNlIF7S0KgUgt2cBBtti1qrszalTWTJ0JQvakdt4LGWyvtJWe4PsDgfFHbg:1tOPGP:77DQ6bK84Pdkk8WIb8sF8F2rOx8_Te0K2v3Nu83A9EQ','2025-01-02 22:45:01.583163');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_site` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lobby_comment`
--

DROP TABLE IF EXISTS `lobby_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lobby_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comentario` varchar(100) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lobby_comments_usuario_id_2b5be089_fk_users_user_id` (`usuario_id`),
  CONSTRAINT `lobby_comments_usuario_id_2b5be089_fk_users_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lobby_comment`
--

LOCK TABLES `lobby_comment` WRITE;
/*!40000 ALTER TABLE `lobby_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `lobby_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lobby_promocion`
--

DROP TABLE IF EXISTS `lobby_promocion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lobby_promocion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `tiene_vigencia` tinyint(1) NOT NULL,
  `vigencia` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lobby_promocion`
--

LOCK TABLES `lobby_promocion` WRITE;
/*!40000 ALTER TABLE `lobby_promocion` DISABLE KEYS */;
/*!40000 ALTER TABLE `lobby_promocion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lobby_sucursal`
--

DROP TABLE IF EXISTS `lobby_sucursal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lobby_sucursal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_sucursal` varchar(30) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lobby_sucursal`
--

LOCK TABLES `lobby_sucursal` WRITE;
/*!40000 ALTER TABLE `lobby_sucursal` DISABLE KEYS */;
INSERT INTO `lobby_sucursal` VALUES (1,'Sucursal 1','Lopez Mateos','-','lobby@example.com');
/*!40000 ALTER TABLE `lobby_sucursal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lobby_sucursal_producto`
--

DROP TABLE IF EXISTS `lobby_sucursal_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lobby_sucursal_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `producto_id` bigint NOT NULL,
  `sucursal_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lobby_sucursal_produ_producto_id_c0907989_fk_restauran` (`producto_id`),
  KEY `lobby_sucursal_produ_sucursal_id_5e838aec_fk_lobby_suc` (`sucursal_id`),
  CONSTRAINT `lobby_sucursal_produ_producto_id_c0907989_fk_restauran` FOREIGN KEY (`producto_id`) REFERENCES `restaurante_producto` (`id`),
  CONSTRAINT `lobby_sucursal_produ_sucursal_id_5e838aec_fk_lobby_suc` FOREIGN KEY (`sucursal_id`) REFERENCES `lobby_sucursal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lobby_sucursal_producto`
--

LOCK TABLES `lobby_sucursal_producto` WRITE;
/*!40000 ALTER TABLE `lobby_sucursal_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `lobby_sucursal_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lobby_sucursal_promocion`
--

DROP TABLE IF EXISTS `lobby_sucursal_promocion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lobby_sucursal_promocion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `promocion_id` bigint NOT NULL,
  `sucursal_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lobby_sucursal_promo_promocion_id_c7d55ab5_fk_lobby_pro` (`promocion_id`),
  KEY `lobby_sucursal_promo_sucursal_id_e1d954b7_fk_lobby_suc` (`sucursal_id`),
  CONSTRAINT `lobby_sucursal_promo_promocion_id_c7d55ab5_fk_lobby_pro` FOREIGN KEY (`promocion_id`) REFERENCES `lobby_promocion` (`id`),
  CONSTRAINT `lobby_sucursal_promo_sucursal_id_e1d954b7_fk_lobby_suc` FOREIGN KEY (`sucursal_id`) REFERENCES `lobby_sucursal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lobby_sucursal_promocion`
--

LOCK TABLES `lobby_sucursal_promocion` WRITE;
/*!40000 ALTER TABLE `lobby_sucursal_promocion` DISABLE KEYS */;
/*!40000 ALTER TABLE `lobby_sucursal_promocion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations_consola`
--

DROP TABLE IF EXISTS `reservations_consola`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_consola` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `disponibilidad_diaria` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `reservations_consola_chk_1` CHECK ((`disponibilidad_diaria` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_consola`
--

LOCK TABLES `reservations_consola` WRITE;
/*!40000 ALTER TABLE `reservations_consola` DISABLE KEYS */;
INSERT INTO `reservations_consola` VALUES (1,'Xbox',3),(2,'PlayStation',2),(3,'NintendoSwitch',3),(4,'Billar',1);
/*!40000 ALTER TABLE `reservations_consola` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations_consola_disponibilidad`
--

DROP TABLE IF EXISTS `reservations_consola_disponibilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_consola_disponibilidad` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `disponibles` bigint unsigned NOT NULL,
  `consola_id` bigint NOT NULL,
  `sucursal_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservations_consola_dis_consola_id_sucursal_id_f_478c27a9_uniq` (`consola_id`,`sucursal_id`,`fecha`),
  KEY `reservations_consola_sucursal_id_8657766d_fk_lobby_suc` (`sucursal_id`),
  CONSTRAINT `reservations_consola_consola_id_6a80a165_fk_reservati` FOREIGN KEY (`consola_id`) REFERENCES `reservations_consola` (`id`),
  CONSTRAINT `reservations_consola_sucursal_id_8657766d_fk_lobby_suc` FOREIGN KEY (`sucursal_id`) REFERENCES `lobby_sucursal` (`id`),
  CONSTRAINT `reservations_consola_disponibilidad_chk_1` CHECK ((`disponibles` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=601 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_consola_disponibilidad`
--

LOCK TABLES `reservations_consola_disponibilidad` WRITE;
/*!40000 ALTER TABLE `reservations_consola_disponibilidad` DISABLE KEYS */;
INSERT INTO `reservations_consola_disponibilidad` VALUES (361,'2025-01-08',3,1,1),(362,'2025-01-08',2,2,1),(363,'2025-01-08',3,3,1),(364,'2025-01-08',1,4,1),(365,'2025-01-09',3,1,1),(366,'2025-01-09',2,2,1),(367,'2025-01-09',3,3,1),(368,'2025-01-09',1,4,1),(369,'2025-01-10',3,1,1),(370,'2025-01-10',2,2,1),(371,'2025-01-10',3,3,1),(372,'2025-01-10',1,4,1),(373,'2025-01-11',3,1,1),(374,'2025-01-11',2,2,1),(375,'2025-01-11',3,3,1),(376,'2025-01-11',1,4,1),(377,'2025-01-12',3,1,1),(378,'2025-01-12',2,2,1),(379,'2025-01-12',3,3,1),(380,'2025-01-12',1,4,1),(381,'2025-01-13',3,1,1),(382,'2025-01-13',2,2,1),(383,'2025-01-13',3,3,1),(384,'2025-01-13',1,4,1),(385,'2025-01-14',3,1,1),(386,'2025-01-14',2,2,1),(387,'2025-01-14',3,3,1),(388,'2025-01-14',1,4,1),(389,'2025-01-15',3,1,1),(390,'2025-01-15',2,2,1),(391,'2025-01-15',3,3,1),(392,'2025-01-15',1,4,1),(393,'2025-01-16',3,1,1),(394,'2025-01-16',2,2,1),(395,'2025-01-16',3,3,1),(396,'2025-01-16',1,4,1),(397,'2025-01-17',3,1,1),(398,'2025-01-17',2,2,1),(399,'2025-01-17',3,3,1),(400,'2025-01-17',1,4,1),(401,'2025-01-18',3,1,1),(402,'2025-01-18',2,2,1),(403,'2025-01-18',3,3,1),(404,'2025-01-18',1,4,1),(405,'2025-01-19',3,1,1),(406,'2025-01-19',2,2,1),(407,'2025-01-19',3,3,1),(408,'2025-01-19',1,4,1),(409,'2025-01-20',3,1,1),(410,'2025-01-20',2,2,1),(411,'2025-01-20',3,3,1),(412,'2025-01-20',1,4,1),(413,'2025-01-21',3,1,1),(414,'2025-01-21',2,2,1),(415,'2025-01-21',3,3,1),(416,'2025-01-21',1,4,1),(417,'2025-01-22',3,1,1),(418,'2025-01-22',2,2,1),(419,'2025-01-22',3,3,1),(420,'2025-01-22',1,4,1),(421,'2025-01-23',3,1,1),(422,'2025-01-23',2,2,1),(423,'2025-01-23',3,3,1),(424,'2025-01-23',1,4,1),(425,'2025-01-24',3,1,1),(426,'2025-01-24',2,2,1),(427,'2025-01-24',3,3,1),(428,'2025-01-24',1,4,1),(429,'2025-01-25',3,1,1),(430,'2025-01-25',2,2,1),(431,'2025-01-25',3,3,1),(432,'2025-01-25',1,4,1),(433,'2025-01-26',3,1,1),(434,'2025-01-26',2,2,1),(435,'2025-01-26',3,3,1),(436,'2025-01-26',1,4,1),(437,'2025-01-27',3,1,1),(438,'2025-01-27',2,2,1),(439,'2025-01-27',3,3,1),(440,'2025-01-27',1,4,1),(441,'2025-01-28',3,1,1),(442,'2025-01-28',2,2,1),(443,'2025-01-28',3,3,1),(444,'2025-01-28',1,4,1),(445,'2025-01-29',3,1,1),(446,'2025-01-29',2,2,1),(447,'2025-01-29',3,3,1),(448,'2025-01-29',1,4,1),(449,'2025-01-30',3,1,1),(450,'2025-01-30',2,2,1),(451,'2025-01-30',3,3,1),(452,'2025-01-30',1,4,1),(453,'2025-01-31',3,1,1),(454,'2025-01-31',2,2,1),(455,'2025-01-31',3,3,1),(456,'2025-01-31',1,4,1),(457,'2025-02-01',3,1,1),(458,'2025-02-01',2,2,1),(459,'2025-02-01',3,3,1),(460,'2025-02-01',1,4,1),(461,'2025-02-02',3,1,1),(462,'2025-02-02',2,2,1),(463,'2025-02-02',3,3,1),(464,'2025-02-02',1,4,1),(465,'2025-02-03',3,1,1),(466,'2025-02-03',2,2,1),(467,'2025-02-03',3,3,1),(468,'2025-02-03',1,4,1),(469,'2025-02-04',3,1,1),(470,'2025-02-04',2,2,1),(471,'2025-02-04',3,3,1),(472,'2025-02-04',1,4,1),(473,'2025-02-05',3,1,1),(474,'2025-02-05',2,2,1),(475,'2025-02-05',3,3,1),(476,'2025-02-05',1,4,1),(477,'2025-02-06',3,1,1),(478,'2025-02-06',2,2,1),(479,'2025-02-06',3,3,1),(480,'2025-02-06',1,4,1),(481,'2025-02-07',3,1,1),(482,'2025-02-07',2,2,1),(483,'2025-02-07',3,3,1),(484,'2025-02-07',1,4,1),(485,'2025-02-08',3,1,1),(486,'2025-02-08',2,2,1),(487,'2025-02-08',3,3,1),(488,'2025-02-08',1,4,1),(489,'2025-02-09',3,1,1),(490,'2025-02-09',2,2,1),(491,'2025-02-09',3,3,1),(492,'2025-02-09',1,4,1),(493,'2025-02-10',3,1,1),(494,'2025-02-10',2,2,1),(495,'2025-02-10',3,3,1),(496,'2025-02-10',1,4,1),(497,'2025-02-11',3,1,1),(498,'2025-02-11',2,2,1),(499,'2025-02-11',3,3,1),(500,'2025-02-11',1,4,1),(501,'2025-02-12',3,1,1),(502,'2025-02-12',2,2,1),(503,'2025-02-12',3,3,1),(504,'2025-02-12',1,4,1),(505,'2025-02-13',3,1,1),(506,'2025-02-13',2,2,1),(507,'2025-02-13',3,3,1),(508,'2025-02-13',1,4,1),(509,'2025-02-14',3,1,1),(510,'2025-02-14',2,2,1),(511,'2025-02-14',3,3,1),(512,'2025-02-14',1,4,1),(513,'2025-02-15',3,1,1),(514,'2025-02-15',2,2,1),(515,'2025-02-15',3,3,1),(516,'2025-02-15',1,4,1),(517,'2025-02-16',3,1,1),(518,'2025-02-16',2,2,1),(519,'2025-02-16',3,3,1),(520,'2025-02-16',1,4,1),(521,'2025-02-17',3,1,1),(522,'2025-02-17',2,2,1),(523,'2025-02-17',3,3,1),(524,'2025-02-17',1,4,1),(525,'2025-02-18',3,1,1),(526,'2025-02-18',2,2,1),(527,'2025-02-18',3,3,1),(528,'2025-02-18',1,4,1),(529,'2025-02-19',3,1,1),(530,'2025-02-19',2,2,1),(531,'2025-02-19',3,3,1),(532,'2025-02-19',1,4,1),(533,'2025-02-20',3,1,1),(534,'2025-02-20',2,2,1),(535,'2025-02-20',3,3,1),(536,'2025-02-20',1,4,1),(537,'2025-02-21',3,1,1),(538,'2025-02-21',2,2,1),(539,'2025-02-21',3,3,1),(540,'2025-02-21',1,4,1),(541,'2025-02-22',3,1,1),(542,'2025-02-22',2,2,1),(543,'2025-02-22',3,3,1),(544,'2025-02-22',1,4,1),(545,'2025-02-23',3,1,1),(546,'2025-02-23',2,2,1),(547,'2025-02-23',3,3,1),(548,'2025-02-23',1,4,1),(549,'2025-02-24',3,1,1),(550,'2025-02-24',2,2,1),(551,'2025-02-24',3,3,1),(552,'2025-02-24',1,4,1),(553,'2025-02-25',3,1,1),(554,'2025-02-25',2,2,1),(555,'2025-02-25',3,3,1),(556,'2025-02-25',1,4,1),(557,'2025-02-26',3,1,1),(558,'2025-02-26',2,2,1),(559,'2025-02-26',3,3,1),(560,'2025-02-26',1,4,1),(561,'2025-02-27',3,1,1),(562,'2025-02-27',2,2,1),(563,'2025-02-27',3,3,1),(564,'2025-02-27',1,4,1),(565,'2025-02-28',3,1,1),(566,'2025-02-28',2,2,1),(567,'2025-02-28',3,3,1),(568,'2025-02-28',1,4,1),(569,'2025-03-01',3,1,1),(570,'2025-03-01',2,2,1),(571,'2025-03-01',3,3,1),(572,'2025-03-01',1,4,1),(573,'2025-03-02',3,1,1),(574,'2025-03-02',2,2,1),(575,'2025-03-02',3,3,1),(576,'2025-03-02',1,4,1),(577,'2025-03-03',3,1,1),(578,'2025-03-03',2,2,1),(579,'2025-03-03',3,3,1),(580,'2025-03-03',1,4,1),(581,'2025-03-04',3,1,1),(582,'2025-03-04',2,2,1),(583,'2025-03-04',3,3,1),(584,'2025-03-04',1,4,1),(585,'2025-03-05',3,1,1),(586,'2025-03-05',2,2,1),(587,'2025-03-05',3,3,1),(588,'2025-03-05',1,4,1),(589,'2025-03-06',3,1,1),(590,'2025-03-06',2,2,1),(591,'2025-03-06',3,3,1),(592,'2025-03-06',1,4,1),(593,'2025-03-07',3,1,1),(594,'2025-03-07',2,2,1),(595,'2025-03-07',3,3,1),(596,'2025-03-07',1,4,1),(597,'2025-03-08',3,1,1),(598,'2025-03-08',2,2,1),(599,'2025-03-08',3,3,1),(600,'2025-03-08',1,4,1);
/*!40000 ALTER TABLE `reservations_consola_disponibilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations_reservation`
--

DROP TABLE IF EXISTS `reservations_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_reservation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `fecha` date NOT NULL,
  `fecha_reservacion` date NOT NULL,
  `hora` time(6) NOT NULL,
  `num_personas` int unsigned NOT NULL,
  `comentarios` longtext,
  `sucursal_id` bigint NOT NULL,
  `username_id` bigint NOT NULL,
  `consola_seleccionada_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reservations_reserva_sucursal_id_b527a48d_fk_lobby_suc` (`sucursal_id`),
  KEY `reservations_reservation_username_id_fe4daede_fk_users_user_id` (`username_id`),
  KEY `reservations_reserva_consola_seleccionada_a47d91e8_fk_reservati` (`consola_seleccionada_id`),
  CONSTRAINT `reservations_reserva_consola_seleccionada_a47d91e8_fk_reservati` FOREIGN KEY (`consola_seleccionada_id`) REFERENCES `reservations_consola` (`id`),
  CONSTRAINT `reservations_reserva_sucursal_id_b527a48d_fk_lobby_suc` FOREIGN KEY (`sucursal_id`) REFERENCES `lobby_sucursal` (`id`),
  CONSTRAINT `reservations_reservation_username_id_fe4daede_fk_users_user_id` FOREIGN KEY (`username_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `reservations_reservation_chk_1` CHECK ((`num_personas` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_reservation`
--

LOCK TABLES `reservations_reservation` WRITE;
/*!40000 ALTER TABLE `reservations_reservation` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations_reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurante_producto`
--

DROP TABLE IF EXISTS `restaurante_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurante_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_producto` varchar(30) NOT NULL,
  `precio` int NOT NULL,
  `descripcion` longtext,
  `seccion_producto_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `restaurante_producto_seccion_producto_id_74a4158d_fk_restauran` (`seccion_producto_id`),
  CONSTRAINT `restaurante_producto_seccion_producto_id_74a4158d_fk_restauran` FOREIGN KEY (`seccion_producto_id`) REFERENCES `restaurante_seccion_productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurante_producto`
--

LOCK TABLES `restaurante_producto` WRITE;
/*!40000 ALTER TABLE `restaurante_producto` DISABLE KEYS */;
INSERT INTO `restaurante_producto` VALUES (4,'Cubeta 6 cervezas',165,'Carta blanca, Tecate, Tecate Light, Indio',2),(5,'Cubeta 6 cervezas',225,'XX Laguer,  XX Ambar, Heineken',2),(6,'Cubeta 6 cervezas',255,'Miller, Corona, Victoria',2),(7,'Cubeta 12 Cervezas',300,'Carta Blanca, Tecate, Tecate Light, Indio',2),(8,'Cubeta 12 Cervezas',430,'XX Laguer, XX Ambar, Heineken',2),(9,'Cubeta 12 Cervezas',490,'Miller, Conora, Victoria',2),(10,'Heineken 0.0',25,'500 ml.',2),(11,'Sol clamato',30,'500 ml.',2),(12,'Carta Blanca',35,'500 ml.',2),(13,'Tecate',35,'500 ml.',2),(14,'Tecate',35,'500 ml.',2),(15,'Tecate Light',35,'500 ml.',2),(16,'Indio',35,'500 ml.',2),(17,'XX Laguer',40,'500 ml.',2),(18,'XX Ambar',40,'500 ml.',2),(19,'Heineken',40,'500 ml.',2),(20,'Miller',45,'500 ml.',2),(21,'Bohemia',45,'Oscura o cristal 500 ml.',2),(22,'Corona',45,'500 ml.',2),(23,'Victoria',45,'500 ml.',2),(24,'Carta Blanca',65,'Caguama',2),(25,'Tecate',65,'Caguama',2),(26,'Tecate Light',65,'Caguama',2),(27,'Indio',65,'Caguama',2),(28,'XX Laguer',75,'Caguama',2),(29,'XX Ambar',75,'Caguama',2),(30,'Heineken',75,'Caguama',2),(31,'Miller',80,'Caguama',2),(32,'Miller Escarchada',90,'Caguama',2),(33,'Corona',75,'Caguama',2),(34,'Victoria',75,'Caguama',2),(35,'Orden de Alitas/Boneless',165,'Salsas: Bufalo, BBQ, Mango Habanero, Lemon Peper, Mostaza y Miel, Queso Parmesano\r\nAderezos: Queso amarillo, Catsup, Mayonesa, Ranch\r\nExtra: $15',1),(36,'Media orden de Alitas/Boneless',100,'Salsas: Bufalo, BBQ, Mango Habanero, Lemon Peper, Mostaza y Miel, Queso Parmesano\r\nAderezos: Queso amarillo, Catsup, Mayonesa, Ranch\r\nExtra: $15',1),(37,'Hamburguesa sencilla',130,'Carne de res, queso amarillo, jamon, lechuga, aguacate, jitomate, cebolla',1),(38,'Hamburguesa doble',165,'Doble carne de res, queso amarillo, queso asadero, tocino, jamon, lechuga, aguacate, jitomate y cebolla',1),(39,'Hamburguesa suprema',175,'Doble carne de res, queso amarillo, queso asadero, salchicha, piña, tocino, jamon, lechuga, aguacate, jitomate y cebolla',1),(40,'Hamburguesa de Boneless',185,'Boneless, Queso amarillo, aguacate, lechuga, jitomate y cebolla',1),(41,'Papas Gajo',100,'',1),(42,'Papas a la francesa',60,'',1),(43,'Aros de Cebolla',90,'',1),(44,'Dedos de queso',120,'',1),(45,'Salchipulpos',80,'',1),(46,'Nachos Sencillos',80,'Queso amarillo y chiles',1),(47,'Nachos Especiales',120,'Queso Amarillo, chillibean y guacamole',1),(48,'Coca-cola',35,'',3),(49,'Coca-cola sin azucar',35,'',3),(50,'Refresco de Sabor',35,'',3),(51,'Dr, Peper',35,'',3),(52,'Jugo del Valle',25,'',3),(53,'Fuze Tea',30,'',3),(54,'Rusa',30,'500 ml',3),(55,'Rusa',50,'1 L.',3),(56,'Limonada',30,'500 ml.',3),(57,'Limonada',50,'1 L.',3),(58,'Naranjada',30,'500 ml.',3),(59,'Naranjada',50,'1 L.',3),(60,'Piñada',50,'500 ml.',3),(61,'Piñada',65,'1 L.',3),(62,'Agua embotellada',25,'500 ml.',3),(63,'Centenario Reposado',800,'',4),(64,'Centenario Plata',850,'',4),(65,'Jose Cuervo Reposado',700,'',4),(66,'Jose Cuervo Plata',750,'',4),(67,'Torres 5',600,'',4),(68,'Torres 10',800,'',4),(69,'Etiqueta Roja',900,'',4),(70,'Capitan Morgan',600,'',4),(71,'Absolut',700,'',4),(72,'Smirnoff',650,'',4),(73,'Bacardy',650,'',4),(74,'Azul',800,'',4),(75,'Kriptonita',110,'Bebida en un vaso de litro escarchado, un preparado que contiene caribe cooler de kiwi y sprite',5),(76,'Piña Colada',100,'1 L de refrescante piña colada',5),(77,'Durazno Drink',110,'Bebida con Vaso de litro escarchado, un preparado que contiene caribe cooler de durazno y Sprite',5),(78,'Pantera Rosa/Frappe Pantera R',100,'Refrescante bebida de 500 ml. a base de crema de coco y ron',5),(79,'Ultra Violeta',100,'Bebida en vaso de litro escarchado. Un preparado que contiene Vodka',5),(80,'Pitufo/Frappe Pitufo',100,'Refrescante bebida a base de crema de coco y ron',5),(81,'Chorreados',110,'1L. Bebida a base de mezcal o ron blanco, con el sabor a elección:\r\nMango, Manzana, Sandia, Guayaba, Fresa, Pepino, Durazno',5),(82,'Chorreados',70,'500ml. Bebida a base de mezcal o ron blanco, con el sabor a eleccion:\r\nMango, Manzana, Sandia, Guayaba, Fresa, Pepino, Durazno',5),(83,'Cubanito',100,'1L de clasico cubanito',5),(84,'Cubanito',60,'500 ml. del clasico cubanito',5),(85,'Azulito',100,'1 L. Refrescante bebida con Vodka acompañado con bebida energética',5),(86,'Azulito',60,'500 ml. de refrescante bebida con vodka acompañado con bebida energética',5),(87,'Mojito',90,'El tradicional mojito con sabor a elección:\r\nMango, Manzana, Sandia, Guayaba, Fresa, Pepino, Durazno',5),(88,'Carajillo',80,'Clasico carajillo hecho a base de licor y café',5),(89,'Cantarito mezcal',80,'Bebida a base de mezcal con refresco de toronja',5),(90,'Bacacho de Horchata',90,'Refrescante bebida de horchata con ron Blanco',5),(91,'Mezcalita/Frappe Mezcalita',70,'Refrescante bebida de mango a base de mezcal',5),(92,'Caballitos de colores',40,'Pantera rosa, Pitufo. Loki, Frozen',5),(93,'Perla Negra',150,'Shot de Jagermeister con bebida energetica',5);
/*!40000 ALTER TABLE `restaurante_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurante_seccion_productos`
--

DROP TABLE IF EXISTS `restaurante_seccion_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurante_seccion_productos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_seccion` varchar(20) NOT NULL,
  `imagen_respaldo_1` varchar(100) NOT NULL,
  `imagen_respaldo_2` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurante_seccion_productos`
--

LOCK TABLES `restaurante_seccion_productos` WRITE;
/*!40000 ALTER TABLE `restaurante_seccion_productos` DISABLE KEYS */;
INSERT INTO `restaurante_seccion_productos` VALUES (1,'Comida','imagen_seccion/nachos.webp','imagen_seccion/restaurant.jpg'),(2,'Cerveza','imagen_seccion/CervezasLobby.jpg','imagen_seccion/Lobby_Beer.png'),(3,'Bebidas Sin Alcohol','imagen_seccion/Bebida_sin_alcohol_1.png','imagen_seccion/Bebida_sin_alcohol_2.png'),(4,'Botellas','imagen_seccion/Botellas_1.jpeg','imagen_seccion/Botellas_2.jpeg'),(5,'Bebidas Con Alcohol','imagen_seccion/Fondo_Lobby.jpg','imagen_seccion/Cubanito_.png');
/*!40000 ALTER TABLE `restaurante_seccion_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialaccount`
--

DROP TABLE IF EXISTS `socialaccount_socialaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialaccount` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(200) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` json NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  KEY `socialaccount_socialaccount_user_id_8146e70c_fk_users_user_id` (`user_id`),
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialaccount`
--

LOCK TABLES `socialaccount_socialaccount` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialapp`
--

DROP TABLE IF EXISTS `socialaccount_socialapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialapp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  `provider_id` varchar(200) NOT NULL,
  `settings` json NOT NULL DEFAULT (_utf8mb3'{}'),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp`
--

LOCK TABLES `socialaccount_socialapp` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialapp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialapp_sites`
--

DROP TABLE IF EXISTS `socialaccount_socialapp_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialapp_sites` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `socialapp_id` int NOT NULL,
  `site_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`),
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp_sites`
--

LOCK TABLES `socialaccount_socialapp_sites` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialtoken`
--

DROP TABLE IF EXISTS `socialaccount_socialtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialtoken` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int NOT NULL,
  `app_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialtoken`
--

LOCK TABLES `socialaccount_socialtoken` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tournaments_torneo`
--

DROP TABLE IF EXISTS `tournaments_torneo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tournaments_torneo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_torneo` varchar(30) NOT NULL,
  `nombre_juego` varchar(30) NOT NULL,
  `modo_torneo` varchar(8) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `imagen_banner` varchar(100) DEFAULT NULL,
  `fecha` datetime(6) NOT NULL,
  `is_defined` tinyint(1) NOT NULL,
  `descripcion` longtext,
  `reglas` longtext,
  `requisitos` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_torneo` (`nombre_torneo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tournaments_torneo`
--

LOCK TABLES `tournaments_torneo` WRITE;
/*!40000 ALTER TABLE `tournaments_torneo` DISABLE KEYS */;
INSERT INTO `tournaments_torneo` VALUES (2,'FC25','FC25','Direct','imagen_torneo/Principal_FC_2.webp','imagen_torneo/Banners_lobby_FC_24.webp','2025-01-14 00:00:00.000000',0,'Lobby Restaurant Bar te invita a participar, hacer amigos y divertirte en el torneo de FC25!!\r\n\r\nEl torneo se llevara acabó el Día Lunes 14 de octubre en punto de las 7:00 pm en Av. Adolfo Lopez Mateos Ote. #428 interior 10 (frente al surtidor del tapicero)\r\nInscripción: $50\r\n TODO LO RECAUDADO EN INSCRIPCIÓN SERA EL PREMIO PARA EL 1er LUGAR (70%) Y 2do LUGAR (30%) \r\n*Lobby no se quedara con ningun porcentaje del premió*\r\n\r\n*Pueden llevar su propio control a las instalaciones si así lo desean*\r\n\r\nCualquier duda sobre el torneo con gusto se las podemos despejar al whatsapp 4492153687\r\n\r\nSuerte a todos y gracias por participar!!','Dependiendo el # de participantes se definirá la eliminatoria: Si son solo 16 participantes, el mejor de 3 partidos pasa a la siguiente ronda, si son 32 participantes será eliminación directa\r\nEquipo libre, NO se permite cambiar configuraciones del partido como, lesiones, manos, fuera de lugar, cámara de partido,tiempo de partido , de infringir con la regla se sancionará a la persona con 1 gol en contra en el resultado final. (Se puede configurar alineaciones solamente)','Como requisito general se le pide a los asistentes consumir dentro del establecimiento, esto con la finalidad de poder costear gastos internos como luz, agua, y todo lo que conlleva sustentar el establecimiento, se agradece su comprensión\r\nPlataformas: XBOX SERIES\r\nPuedes apartar tu lugar pagando directamente en Lobby antes del torneo o pagar el día del evento con registro previo al whatsapp 449 565 0644\r\n El check-in y pago de inscripciones se realizara a las 6:30 PM, Se les pide por favor PUNTUALIDAD para poder comenzar a tiempo el torneo a las 7:00 PM'),(3,'MK1','MK1','Round','imagen_torneo/Tetris_Principal.webp','imagen_torneo/Tetris_Banner.jpg','2025-01-21 00:00:00.000000',0,'Lobby Restaurant Bar te invita a participar, hacer amigos y divertirte en el torneo de\r\nMortal Kombat 1!!\r\nCUPO LIMITADO A 25 PARTICIPANTES\r\nInscripción: $50\r\nTODO LO RECAUDADO EN INSCRIPCIÓN SERA EL PREMIO PARA EL 1er LUGAR (70%) Y 2do LUGAR (30%)\r\n*Lobby no se quedara con ningún porcentaje del premio*\r\nCualquier duda sobre el torneo con gusto se las podemos despejar en el what´sapp 4492153687','Se disputara FT3 (primero en ganar 3) todas las partidas y FT5 la final (Primero en ganar 5)\r\nSolo el perdedor del round puede cambiar de personaje y kameo (quien gane el round permanece con los mismos)\r\nodas las partidas seran de eliminación directa, por lo que el ganador avanzara a la siguiente ronda y el perdedor termina su participación','Como requisito general se le pide a los asistentes consumir dentro del establecimiento, esto con la finalidad de poder costear gastos internos como luz, agua, y todo lo que conlleva sustentar el establecimiento, se agradece su comprensión \r\nPlataformas: XBOX SERIES Y PS5\r\nPuedes apartar tu lugar pagando directamente en Lobby antes del torneo o pagar el día del evento con registro previo a través de la inscripcion online \r\nEl check-in y pago de inscripciones se realizara a las 6:30 PM, Se les pide por favor PUNTUALIDAD para poder comenzar a tiempo el torneo a las 7:00 PM'),(4,'Smash','Smash Bros','Direct','imagen_torneo/mejoracalidad.jpeg','imagen_torneo/Banner_alt.webp','2025-01-28 00:00:00.000000',0,'Lobby Restaurant Bar te invita a participar, hacer amigos y divertirte en el torneo de Super Smash Bros Ultimate!!! \r\nCUPO LIMITADO A 25 PARTICIPANTES\r\nInscripción: $50\r\nTODO LO RECAUDADO EN INSCRIPCIÓN SERA EL PREMIO PARA EL 1er LUGAR (70%) Y 2do LUGAR (30%)\r\n*Lobby no se quedara con ningún porcentaje del premio*','','Como requisito general se le pide a los asistentes consumir dentro del establecimiento, esto con la finalidad de poder costear gastos internos como luz, agua, y todo lo que conlleva sustentar el establecimiento, se agradece su comprensión \r\nPuedes apartar tu lugar pagando directamente en Lobby antes del torneo o pagar el día del evento con registro previo a través de la inscripción online\r\nSe requiere/recomienda que los participantes lleven sus propios controles para evitar malos entendidos por funcionamientos o configuraciones'),(5,'FC 25 Duos','FC25','Direct','imagen_torneo/Principal_FC.webp','imagen_torneo/Banner_alt.webp','2025-02-11 00:00:00.000000',0,'Lobby Restaurant Bar te invita a participar, hacer amigos y divertirte en el torneo de FC25!! El torneo se llevara acabó el Día Lunes 14 de octubre en punto de las 7:00 pm en Av. Adolfo Lopez Mateos Ote. #428 interior 10 (frente al surtidor del tapicero)\r\nInscripción: $50 TODO LO RECAUDADO EN INSCRIPCIÓN SERA EL PREMIO PARA EL 1er LUGAR (70%) Y 2do LUGAR (30%)\r\n *Lobby no se quedara con ningun porcentaje del premió* *Pueden llevar su propio control a las instalaciones si así lo desean* Cualquier duda sobre el torneo con gusto se las podemos despejar al whatsapp 4492153687\r\nSuerte a todos y gracias por participar!!','Dependiendo el # de participantes se definirá la eliminatoria: Si son solo 16 participantes, el mejor de 3 partidos pasa a la siguiente ronda, si son 32 participantes será eliminación directa\r\nEquipo libre, NO se permite cambiar configuraciones del partido como, lesiones, manos, fuera de lugar, cámara de partido,tiempo de partido , de infringir con la regla se sancionará a la persona con 1 gol en contra en el resultado final. (Se puede configurar alineaciones solamente)','Como requisito general se le pide a los asistentes consumir dentro del establecimiento, esto con la finalidad de poder costear gastos internos como luz, agua, y todo lo que conlleva sustentar el establecimiento, se agradece su comprensión\r\nPlataformas: XBOX SERIES\r\nPuedes apartar tu lugar pagando directamente en Lobby antes del torneo o pagar el día del evento con registro previo al whatsapp 449 565 0644\r\nEl check-in y pago de inscripciones se realizara a las 6:30 PM, Se les pide por favor PUNTUALIDAD para poder comenzar a tiempo el torneo a las 7:00 PM'),(6,'TETRIS','TETRIS','Direct','imagen_torneo/Tetris_Principal.webp','imagen_torneo/Tetris_Banner.jpg','2025-02-18 00:00:00.000000',0,'¡Prepárate para una experiencia de juego única! Únete a nuestro emocionante torneo de Tetris, donde podrás demostrar tu velocidad, estrategia y habilidad para mantener el tablero limpio. Ya seas un jugador experto o alguien que disfruta de los clásicos, este evento es para ti.','Ados','Hola');
/*!40000 ALTER TABLE `tournaments_torneo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tournaments_torneo_jugadores_inscritos`
--

DROP TABLE IF EXISTS `tournaments_torneo_jugadores_inscritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tournaments_torneo_jugadores_inscritos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `torneo_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tournaments_torneo_jugad_torneo_id_user_id_b9adf0e5_uniq` (`torneo_id`,`user_id`),
  KEY `tournaments_torneo_j_user_id_e871ba91_fk_users_use` (`user_id`),
  CONSTRAINT `tournaments_torneo_j_torneo_id_8f0521a4_fk_tournamen` FOREIGN KEY (`torneo_id`) REFERENCES `tournaments_torneo` (`id`),
  CONSTRAINT `tournaments_torneo_j_user_id_e871ba91_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tournaments_torneo_jugadores_inscritos`
--

LOCK TABLES `tournaments_torneo_jugadores_inscritos` WRITE;
/*!40000 ALTER TABLE `tournaments_torneo_jugadores_inscritos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tournaments_torneo_jugadores_inscritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `tipo_usuario` varchar(2) NOT NULL,
  `email` varchar(254) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `juegos_inscritos` json NOT NULL DEFAULT (_utf8mb3'[]'),
  `avatar` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `users_user_email_243f6e77_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (35,'pbkdf2_sha256$870000$SQYaTyNqzF7bAxlhVmoX1a$8kei3BA96BKsSO572o5wKHMYE4Im+y0uys/HoL4c0j0=','2025-01-09 04:01:33.350386',1,'LobbyAdmin','','',1,1,'2025-01-09 04:00:33.520943','AD','lobby@example.com','6612175991','[]',''),(36,'pbkdf2_sha256$870000$bcQYDz1Cyy5VAqrqfiyjd8$qCZpFkE9L2Phfri1O0hOixeoPTbV126BpRXVp5eJjD8=',NULL,1,'AdminAux','','',1,1,'2025-01-09 04:03:38.000127','AD','Aux@example.com','8152982059','[]','');
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-09  0:22:18
