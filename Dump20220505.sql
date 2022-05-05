-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: Napster
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DIRECTORY`
--

DROP TABLE IF EXISTS `DIRECTORY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DIRECTORY` (
  `SID` varchar(16) NOT NULL,
  `MD5` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIRECTORY`
--

LOCK TABLES `DIRECTORY` WRITE;
/*!40000 ALTER TABLE `DIRECTORY` DISABLE KEYS */;
/*!40000 ALTER TABLE `DIRECTORY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DOWNLOAD`
--

DROP TABLE IF EXISTS `DOWNLOAD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DOWNLOAD` (
  `SID` varchar(16) NOT NULL,
  `MD5` varchar(32) NOT NULL,
  `IP` varchar(15) NOT NULL,
  `PORTA` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DOWNLOAD`
--

LOCK TABLES `DOWNLOAD` WRITE;
/*!40000 ALTER TABLE `DOWNLOAD` DISABLE KEYS */;
/*!40000 ALTER TABLE `DOWNLOAD` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FILE`
--

DROP TABLE IF EXISTS `FILE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FILE` (
  `NOME` varchar(100) NOT NULL,
  `MD5` varchar(32) NOT NULL,
  PRIMARY KEY (`MD5`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FILE`
--

LOCK TABLES `FILE` WRITE;
/*!40000 ALTER TABLE `FILE` DISABLE KEYS */;
/*!40000 ALTER TABLE `FILE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UTENTE`
--

DROP TABLE IF EXISTS `UTENTE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UTENTE` (
  `IP` varchar(15) NOT NULL,
  `PORTA` varchar(5) NOT NULL,
  `SID` varchar(16) NOT NULL,
  PRIMARY KEY (`SID`),
  UNIQUE KEY `IP` (`IP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UTENTE`
--

LOCK TABLES `UTENTE` WRITE;
/*!40000 ALTER TABLE `UTENTE` DISABLE KEYS */;
INSERT INTO `UTENTE` VALUES ('025.014.181.181','49547','54UWTCWPQXS8QY28');
/*!40000 ALTER TABLE `UTENTE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utente2`
--

DROP TABLE IF EXISTS `utente2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utente2` (
  `id` tinyint(1) DEFAULT NULL,
  `nome` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utente2`
--

LOCK TABLES `utente2` WRITE;
/*!40000 ALTER TABLE `utente2` DISABLE KEYS */;
/*!40000 ALTER TABLE `utente2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-05 12:05:41
