-- phpMyAdmin SQL Dump
-- version 3.5.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 24, 2014 at 11:19 PM
-- Server version: 5.5.33-31.1
-- PHP Version: 5.3.17

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `myeong_urban`
--

-- --------------------------------------------------------

--
-- Table structure for table `address`
--

CREATE TABLE IF NOT EXISTS `address` (
  `tfl_id` int(10) unsigned NOT NULL,
  `name` varchar(100) NOT NULL,
  `lat` decimal(12,10) NOT NULL,
  `lon` decimal(12,10) NOT NULL,
  PRIMARY KEY (`tfl_id`),
  UNIQUE KEY `tfl_id_UNIQUE` (`tfl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `address`
--

INSERT INTO `address` (`tfl_id`, `name`, `lat`, `lon`) VALUES
(0, 'Intersection, Baltimore Ave and Berwyn House Rd.', 38.9922640000, -76.9332980000),
(1, 'Intersection, Baltimore Ave and Knox Rd.', 38.9805190000, -76.9379710000),
(2, 'Near Baltimore Ave and Gallatin St.', 38.9976260000, -76.9315950000),
(3, 'Intersection, Adelphi Rd and Campus Dr.', 38.9850500000, -76.9555890000),
(4, 'Around 4500 Paint Branch Parkway', 38.9831500000, -76.9297640000),
(5, 'Intersection, University Blvd E and Metzerott Rd.', 39.0000740000, -76.9426980000),
(6, 'Intersection, Cherry Hill Rd and Baltimore Ave.', 39.0144250000, -76.9278490000),
(7, 'Intersection, Ikea Center Blvd and Baltimore Ave.', 39.0216700000, -76.9251990000),
(8, 'Intersection, Campus Dr and Baltimore Ave.', 38.9887200000, -76.9351430000),
(9, 'Intersection, Paint Branch Pkwy and River Rd.', 38.9784860000, -76.9266710000),
(10, 'Intersection, Route 201 and Westchester Park Dr.', 38.9903270000, -76.9058300000),
(11, 'Around Edgewood Rd and Rhode Island Ave.', 39.0152040000, -76.9210000000),
(12, 'Intersection, Cherrywood Ln and Greenbelt Rd.', 38.9979900000, -76.9117730000),
(13, 'Intersection, Quebec St and 62nd Ave.', 38.9928240000, -76.9094770000),
(14, 'Intersection, University Blvd and Stadium Dr.', 38.9926230000, -76.9518470000),
(15, 'Intersection, Metzerott Rd and Greenmead Dr.', 39.0008740000, -76.9446110000),
(16, 'Intersection, Baltimore Ave and Hollywood Rd.', 39.0114410000, -76.9284840000),
(17, 'Intersection, University Blvd E and Rhode Island Ave.', 38.9991660000, -76.9255400000),
(18, 'Intersection, Baltimore Ave and Melbourne Pl.', 38.9908500000, -76.9338920000),
(19, 'Around Yale Avenue', 38.9830090000, -76.9357850000),
(20, 'Intersection, Yale Ave and Knox Rd.', 38.9806090000, -76.9367070000);

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE IF NOT EXISTS `answers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `points_id` bigint(20) unsigned NOT NULL,
  `users_id` bigint(20) unsigned NOT NULL,
  `address_answer` int(10) unsigned DEFAULT NULL,
  `landmark_answer` varchar(4) DEFAULT NULL,
  `correctness` tinyint(4) NOT NULL,
  `familiarity_answer` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_answers_users1` (`users_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=167 ;

-- --------------------------------------------------------

--
-- Table structure for table `landmarks`
--

CREATE TABLE IF NOT EXISTS `landmarks` (
  `ons_label` varchar(4) NOT NULL,
  `name` varchar(100) NOT NULL,
  `lat` decimal(12,10) NOT NULL,
  `lon` decimal(12,10) NOT NULL,
  PRIMARY KEY (`ons_label`),
  UNIQUE KEY `tfl_id_UNIQUE` (`ons_label`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `landmarks`
--

INSERT INTO `landmarks` (`ons_label`, `name`, `lat`, `lon`) VALUES
('a', 'In front of University View APT', 38.9922640000, -76.9332980000),
('b', 'In front of College Park Shopping Center', 38.9805190000, -76.9379710000),
('c', 'Near Graduate Hills APT', 38.9850500000, -76.9555890000),
('d', 'Near UMD Fire and Rescue Institute', 38.9831500000, -76.9297640000),
('e', 'North of University of Maryland', 39.0000740000, -76.9426980000),
('f', 'Near Shoppers and BestBuy', 39.0144250000, -76.9278490000),
('g', 'In front of IKEA', 39.0216700000, -76.9251990000),
('h', 'Main Gate, University of Maryland College Park', 38.9887200000, -76.9351430000),
('i', 'In front of College Park Metro', 38.9784860000, -76.9266710000),
('j', 'In front of Westchester Park Apartments', 38.9903270000, -76.9058300000),
('k', 'Near Hollywood Plaza (shopping center)', 39.0152040000, -76.9210000000),
('l', 'Near Giant (grocery store) ', 38.9979900000, -76.9117730000),
('m', 'Near Berwyn Heights Elementary School', 38.9928240000, -76.9094770000),
('n', 'Entrance to UMD Golf Course', 38.9926230000, -76.9518470000),
('o', 'Near Wallace Presbyterian Church', 39.0008740000, -76.9446110000),
('p', 'Near United States Post Office (USPS Office)', 39.0114410000, -76.9284840000),
('q', 'Near Branchville Volunteer Fire station', 38.9991660000, -76.9255400000),
('r', 'Near College Park Volunteer Fire Department', 38.9908500000, -76.9338920000),
('s', 'Near Fraternity Row', 38.9830090000, -76.9357850000),
('t', 'Near Soronity Row', 38.9806090000, -76.9367070000);

-- --------------------------------------------------------

--
-- Table structure for table `points`
--

CREATE TABLE IF NOT EXISTS `points` (
  `id` bigint(20) unsigned NOT NULL,
  `lat` decimal(12,10) NOT NULL,
  `lon` decimal(12,10) NOT NULL,
  `fake` tinyint(4) DEFAULT NULL,
  `reported` int(10) unsigned DEFAULT '0',
  `landmark_id` varchar(4) NOT NULL,
  `address_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `points`
--

INSERT INTO `points` (`id`, `lat`, `lon`, `fake`, `reported`, `landmark_id`, `address_id`) VALUES
(0, 38.9922640000, -76.9332980000, NULL, 0, 'a', 0),
(1, 38.9805190000, -76.9379710000, NULL, 0, 'b', 1),
(2, 38.9850500000, -76.9555890000, NULL, 0, 'c', 3),
(3, 38.9832080000, -76.9299250000, NULL, 0, 'd', 4),
(4, 39.0000740000, -76.9426980000, NULL, 0, 'e', 5),
(5, 39.0144250000, -76.9278490000, NULL, 0, 'f', 6),
(6, 39.0216700000, -76.9251990000, NULL, 0, 'g', 7),
(7, 38.9887200000, -76.9351430000, NULL, 0, 'h', 8),
(8, 38.9784860000, -76.9266710000, NULL, 0, 'i', 9),
(9, 38.9903270000, -76.9058300000, NULL, 0, 'j', 10),
(10, 39.0152040000, -76.9210000000, NULL, 0, 'k', 11),
(11, 38.9979900000, -76.9117730000, NULL, 0, 'l', 12),
(12, 38.9928240000, -76.9094770000, NULL, 0, 'm', 13),
(13, 38.9926230000, -76.9518470000, NULL, 0, 'n', 14),
(14, 39.0008740000, -76.9446110000, NULL, 0, 'o', 15),
(15, 39.0114410000, -76.9284840000, NULL, 0, 'p', 16),
(16, 38.9991660000, -76.9255400000, NULL, 0, 'q', 17),
(17, 38.9908500000, -76.9338920000, NULL, 0, 'r', 18),
(18, 38.9830090000, -76.9357850000, NULL, 0, 's', 19),
(19, 38.9806090000, -76.9367070000, NULL, 0, 't', 20);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) DEFAULT NULL,
  `ip_city` varchar(100) DEFAULT NULL,
  `ip_country` varchar(100) DEFAULT NULL,
  `ip_lat` decimal(12,10) DEFAULT NULL,
  `ip_lon` decimal(12,10) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `twitter` varchar(45) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `postcode` varchar(45) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  `ethnic` varchar(45) DEFAULT NULL,
  `occupation` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=269 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `fk_answers_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
