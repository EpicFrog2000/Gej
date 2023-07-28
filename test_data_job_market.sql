-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2023 at 04:33 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test_data_job_market`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `management_level` varchar(255) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `tryb_pracy` varchar(255) DEFAULT NULL,
  `etat` varchar(255) DEFAULT NULL,
  `kontrakt` varchar(255) DEFAULT NULL,
  `specjalizacja` varchar(255) DEFAULT NULL,
  `doswiadczenie` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `etat`
--

CREATE TABLE `etat` (
  `id` int(11) NOT NULL,
  `etat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kontrakt`
--

CREATE TABLE `kontrakt` (
  `id` int(11) NOT NULL,
  `kontrakt` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `management_level`
--

CREATE TABLE `management_level` (
  `id` int(11) NOT NULL,
  `management_level` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `specjalizacje`
--

CREATE TABLE `specjalizacje` (
  `id` int(11) NOT NULL,
  `specjalizacja` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `technologie_mile_widziane`
--

CREATE TABLE `technologie_mile_widziane` (
  `id` int(11) NOT NULL,
  `technologia` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `technologie_wymagane`
--

CREATE TABLE `technologie_wymagane` (
  `id` int(11) NOT NULL,
  `technologia` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `work_type`
--

CREATE TABLE `work_type` (
  `id` int(11) NOT NULL,
  `work_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
