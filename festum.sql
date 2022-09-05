-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 05, 2022 at 02:49 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `festum`
--

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('1ca8de1380b0af3af832007aa2660158cd838db0', '2022-09-05 08:38:07.189912', 23),
('897c01478c5df99809e95574526293410a86da9c', '2022-09-05 08:35:00.486193', 20),
('cd6c8a79a11124cf9316045c611777a79d1788db', '2022-09-05 08:38:23.919694', 24),
('ce077848667eaab20920a82dbc214b0b9e2a1bb2', '2022-09-05 08:37:27.148391', 21),
('f14b2605239d18e03cda82cc19c6aac460209186', '2022-09-05 08:37:44.534777', 22);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Token', 6, 'add_token'),
(22, 'Can change Token', 6, 'change_token'),
(23, 'Can delete Token', 6, 'delete_token'),
(24, 'Can view Token', 6, 'view_token'),
(25, 'Can add token', 7, 'add_tokenproxy'),
(26, 'Can change token', 7, 'change_tokenproxy'),
(27, 'Can delete token', 7, 'delete_tokenproxy'),
(28, 'Can view token', 7, 'view_tokenproxy'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add add_service_ev', 9, 'add_add_service_ev'),
(34, 'Can change add_service_ev', 9, 'change_add_service_ev'),
(35, 'Can delete add_service_ev', 9, 'delete_add_service_ev'),
(36, 'Can view add_service_ev', 9, 'view_add_service_ev'),
(37, 'Can add advertisement', 10, 'add_advertisement'),
(38, 'Can change advertisement', 10, 'change_advertisement'),
(39, 'Can delete advertisement', 10, 'delete_advertisement'),
(40, 'Can view advertisement', 10, 'view_advertisement'),
(41, 'Can add create event', 11, 'add_createevent'),
(42, 'Can change create event', 11, 'change_createevent'),
(43, 'Can delete create event', 11, 'delete_createevent'),
(44, 'Can view create event', 11, 'view_createevent'),
(45, 'Can add emails', 12, 'add_emails'),
(46, 'Can change emails', 12, 'change_emails'),
(47, 'Can delete emails', 12, 'delete_emails'),
(48, 'Can view emails', 12, 'view_emails'),
(49, 'Can add event category', 13, 'add_eventcategory'),
(50, 'Can change event category', 13, 'change_eventcategory'),
(51, 'Can delete event category', 13, 'delete_eventcategory'),
(52, 'Can view event category', 13, 'view_eventcategory'),
(53, 'Can add event company details', 14, 'add_eventcompanydetails'),
(54, 'Can change event company details', 14, 'change_eventcompanydetails'),
(55, 'Can delete event company details', 14, 'delete_eventcompanydetails'),
(56, 'Can view event company details', 14, 'view_eventcompanydetails'),
(57, 'Can add for who', 15, 'add_forwho'),
(58, 'Can change for who', 15, 'change_forwho'),
(59, 'Can delete for who', 15, 'delete_forwho'),
(60, 'Can view for who', 15, 'view_forwho'),
(61, 'Can add get in touch', 16, 'add_getintouch'),
(62, 'Can change get in touch', 16, 'change_getintouch'),
(63, 'Can delete get in touch', 16, 'delete_getintouch'),
(64, 'Can view get in touch', 16, 'view_getintouch'),
(65, 'Can add notification data', 17, 'add_notificationdata'),
(66, 'Can change notification data', 17, 'change_notificationdata'),
(67, 'Can delete notification data', 17, 'delete_notificationdata'),
(68, 'Can view notification data', 17, 'view_notificationdata'),
(69, 'Can add o_ partner companys', 18, 'add_o_partnercompanys'),
(70, 'Can change o_ partner companys', 18, 'change_o_partnercompanys'),
(71, 'Can delete o_ partner companys', 18, 'delete_o_partnercompanys'),
(72, 'Can view o_ partner companys', 18, 'view_o_partnercompanys'),
(73, 'Can add o_ personal skills', 19, 'add_o_personalskills'),
(74, 'Can change o_ personal skills', 19, 'change_o_personalskills'),
(75, 'Can delete o_ personal skills', 19, 'delete_o_personalskills'),
(76, 'Can view o_ personal skills', 19, 'view_o_personalskills'),
(77, 'Can add partner company category', 20, 'add_partnercompanycategory'),
(78, 'Can change partner company category', 20, 'change_partnercompanycategory'),
(79, 'Can delete partner company category', 20, 'delete_partnercompanycategory'),
(80, 'Can view partner company category', 20, 'view_partnercompanycategory'),
(81, 'Can add pc_artist', 21, 'add_pc_artist'),
(82, 'Can change pc_artist', 21, 'change_pc_artist'),
(83, 'Can delete pc_artist', 21, 'delete_pc_artist'),
(84, 'Can view pc_artist', 21, 'view_pc_artist'),
(85, 'Can add pc_decor', 22, 'add_pc_decor'),
(86, 'Can change pc_decor', 22, 'change_pc_decor'),
(87, 'Can delete pc_decor', 22, 'delete_pc_decor'),
(88, 'Can view pc_decor', 22, 'view_pc_decor'),
(89, 'Can add personal skill category', 23, 'add_personalskillcategory'),
(90, 'Can change personal skill category', 23, 'change_personalskillcategory'),
(91, 'Can delete personal skill category', 23, 'delete_personalskillcategory'),
(92, 'Can view personal skill category', 23, 'view_personalskillcategory'),
(93, 'Can add place_ events', 24, 'add_place_events'),
(94, 'Can change place_ events', 24, 'change_place_events'),
(95, 'Can delete place_ events', 24, 'delete_place_events'),
(96, 'Can view place_ events', 24, 'view_place_events'),
(97, 'Can add rooms', 25, 'add_rooms'),
(98, 'Can change rooms', 25, 'change_rooms'),
(99, 'Can delete rooms', 25, 'delete_rooms'),
(100, 'Can view rooms', 25, 'view_rooms'),
(101, 'Can add subscriptionplan', 26, 'add_subscriptionplan'),
(102, 'Can change subscriptionplan', 26, 'change_subscriptionplan'),
(103, 'Can delete subscriptionplan', 26, 'delete_subscriptionplan'),
(104, 'Can view subscriptionplan', 26, 'view_subscriptionplan'),
(105, 'Can add wishlists', 27, 'add_wishlists'),
(106, 'Can change wishlists', 27, 'change_wishlists'),
(107, 'Can delete wishlists', 27, 'delete_wishlists'),
(108, 'Can view wishlists', 27, 'view_wishlists'),
(109, 'Can add video_ event', 28, 'add_video_event'),
(110, 'Can change video_ event', 28, 'change_video_event'),
(111, 'Can delete video_ event', 28, 'delete_video_event'),
(112, 'Can view video_ event', 28, 'view_video_event'),
(113, 'Can add transactions', 29, 'add_transactions'),
(114, 'Can change transactions', 29, 'change_transactions'),
(115, 'Can delete transactions', 29, 'delete_transactions'),
(116, 'Can view transactions', 29, 'view_transactions'),
(117, 'Can add tickets', 30, 'add_tickets'),
(118, 'Can change tickets', 30, 'change_tickets'),
(119, 'Can delete tickets', 30, 'delete_tickets'),
(120, 'Can view tickets', 30, 'view_tickets'),
(121, 'Can add service image', 31, 'add_serviceimage'),
(122, 'Can change service image', 31, 'change_serviceimage'),
(123, 'Can delete service image', 31, 'delete_serviceimage'),
(124, 'Can view service image', 31, 'view_serviceimage'),
(125, 'Can add servic', 32, 'add_servic'),
(126, 'Can change servic', 32, 'change_servic'),
(127, 'Can delete servic', 32, 'delete_servic'),
(128, 'Can view servic', 32, 'view_servic'),
(129, 'Can add redeem coins', 33, 'add_redeemcoins'),
(130, 'Can change redeem coins', 33, 'change_redeemcoins'),
(131, 'Can delete redeem coins', 33, 'delete_redeemcoins'),
(132, 'Can view redeem coins', 33, 'view_redeemcoins'),
(133, 'Can add ps_video', 34, 'add_ps_video'),
(134, 'Can change ps_video', 34, 'change_ps_video'),
(135, 'Can delete ps_video', 34, 'delete_ps_video'),
(136, 'Can view ps_video', 34, 'view_ps_video'),
(137, 'Can add ps_photo', 35, 'add_ps_photo'),
(138, 'Can change ps_photo', 35, 'change_ps_photo'),
(139, 'Can delete ps_photo', 35, 'delete_ps_photo'),
(140, 'Can view ps_photo', 35, 'view_ps_photo'),
(141, 'Can add ps_equipments', 36, 'add_ps_equipments'),
(142, 'Can change ps_equipments', 36, 'change_ps_equipments'),
(143, 'Can delete ps_equipments', 36, 'delete_ps_equipments'),
(144, 'Can view ps_equipments', 36, 'view_ps_equipments'),
(145, 'Can add ps_companyvideos', 37, 'add_ps_companyvideos'),
(146, 'Can change ps_companyvideos', 37, 'change_ps_companyvideos'),
(147, 'Can delete ps_companyvideos', 37, 'delete_ps_companyvideos'),
(148, 'Can view ps_companyvideos', 37, 'view_ps_companyvideos'),
(149, 'Can add ps_companyphotos', 38, 'add_ps_companyphotos'),
(150, 'Can change ps_companyphotos', 38, 'change_ps_companyphotos'),
(151, 'Can delete ps_companyphotos', 38, 'delete_ps_companyphotos'),
(152, 'Can view ps_companyphotos', 38, 'view_ps_companyphotos'),
(153, 'Can add personal skill sub category', 39, 'add_personalskillsubcategory'),
(154, 'Can change personal skill sub category', 39, 'change_personalskillsubcategory'),
(155, 'Can delete personal skill sub category', 39, 'delete_personalskillsubcategory'),
(156, 'Can view personal skill sub category', 39, 'view_personalskillsubcategory'),
(157, 'Can add pc_videos', 40, 'add_pc_videos'),
(158, 'Can change pc_videos', 40, 'change_pc_videos'),
(159, 'Can delete pc_videos', 40, 'delete_pc_videos'),
(160, 'Can view pc_videos', 40, 'view_pc_videos'),
(161, 'Can add pc_photos', 41, 'add_pc_photos'),
(162, 'Can change pc_photos', 41, 'change_pc_photos'),
(163, 'Can delete pc_photos', 41, 'delete_pc_photos'),
(164, 'Can view pc_photos', 41, 'view_pc_photos'),
(165, 'Can add pc_equipments', 42, 'add_pc_equipments'),
(166, 'Can change pc_equipments', 42, 'change_pc_equipments'),
(167, 'Can delete pc_equipments', 42, 'delete_pc_equipments'),
(168, 'Can view pc_equipments', 42, 'view_pc_equipments'),
(169, 'Can add pc_companyvideos', 43, 'add_pc_companyvideos'),
(170, 'Can change pc_companyvideos', 43, 'change_pc_companyvideos'),
(171, 'Can delete pc_companyvideos', 43, 'delete_pc_companyvideos'),
(172, 'Can view pc_companyvideos', 43, 'view_pc_companyvideos'),
(173, 'Can add pc_companyphotos', 44, 'add_pc_companyphotos'),
(174, 'Can change pc_companyphotos', 44, 'change_pc_companyphotos'),
(175, 'Can delete pc_companyphotos', 44, 'delete_pc_companyphotos'),
(176, 'Can view pc_companyphotos', 44, 'view_pc_companyphotos'),
(177, 'Can add o_ rats', 45, 'add_o_rats'),
(178, 'Can change o_ rats', 45, 'change_o_rats'),
(179, 'Can delete o_ rats', 45, 'delete_o_rats'),
(180, 'Can view o_ rats', 45, 'view_o_rats'),
(181, 'Can add notification', 46, 'add_notification'),
(182, 'Can change notification', 46, 'change_notification'),
(183, 'Can delete notification', 46, 'delete_notification'),
(184, 'Can view notification', 46, 'view_notification'),
(185, 'Can add message', 47, 'add_message'),
(186, 'Can change message', 47, 'change_message'),
(187, 'Can delete message', 47, 'delete_message'),
(188, 'Can view message', 47, 'view_message'),
(189, 'Can add membership', 48, 'add_membership'),
(190, 'Can change membership', 48, 'change_membership'),
(191, 'Can delete membership', 48, 'delete_membership'),
(192, 'Can view membership', 48, 'view_membership'),
(193, 'Can add image_ event', 49, 'add_image_event'),
(194, 'Can change image_ event', 49, 'change_image_event'),
(195, 'Can delete image_ event', 49, 'delete_image_event'),
(196, 'Can view image_ event', 49, 'view_image_event'),
(197, 'Can add fcmtoken', 50, 'add_fcmtoken'),
(198, 'Can change fcmtoken', 50, 'change_fcmtoken'),
(199, 'Can delete fcmtoken', 50, 'delete_fcmtoken'),
(200, 'Can view fcmtoken', 50, 'view_fcmtoken'),
(201, 'Can add exceluser', 51, 'add_exceluser'),
(202, 'Can change exceluser', 51, 'change_exceluser'),
(203, 'Can delete exceluser', 51, 'delete_exceluser'),
(204, 'Can view exceluser', 51, 'view_exceluser'),
(205, 'Can add event personal details', 52, 'add_eventpersonaldetails'),
(206, 'Can change event personal details', 52, 'change_eventpersonaldetails'),
(207, 'Can delete event personal details', 52, 'delete_eventpersonaldetails'),
(208, 'Can view event personal details', 52, 'view_eventpersonaldetails'),
(209, 'Can add event company video', 53, 'add_eventcompanyvideo'),
(210, 'Can change event company video', 53, 'change_eventcompanyvideo'),
(211, 'Can delete event company video', 53, 'delete_eventcompanyvideo'),
(212, 'Can view event company video', 53, 'view_eventcompanyvideo'),
(213, 'Can add event company image', 54, 'add_eventcompanyimage'),
(214, 'Can change event company image', 54, 'change_eventcompanyimage'),
(215, 'Can delete event company image', 54, 'delete_eventcompanyimage'),
(216, 'Can view event company image', 54, 'view_eventcompanyimage'),
(217, 'Can add equipments_pskill', 55, 'add_equipments_pskill'),
(218, 'Can change equipments_pskill', 55, 'change_equipments_pskill'),
(219, 'Can delete equipments_pskill', 55, 'delete_equipments_pskill'),
(220, 'Can view equipments_pskill', 55, 'view_equipments_pskill'),
(221, 'Can add equipments_pc', 56, 'add_equipments_pc'),
(222, 'Can change equipments_pc', 56, 'change_equipments_pc'),
(223, 'Can delete equipments_pc', 56, 'delete_equipments_pc'),
(224, 'Can view equipments_pc', 56, 'view_equipments_pc'),
(225, 'Can add discount on equipment', 57, 'add_discountonequipment'),
(226, 'Can change discount on equipment', 57, 'change_discountonequipment'),
(227, 'Can delete discount on equipment', 57, 'delete_discountonequipment'),
(228, 'Can view discount on equipment', 57, 'view_discountonequipment'),
(229, 'Can add discount on bill', 58, 'add_discountonbill'),
(230, 'Can change discount on bill', 58, 'change_discountonbill'),
(231, 'Can delete discount on bill', 58, 'delete_discountonbill'),
(232, 'Can view discount on bill', 58, 'view_discountonbill'),
(233, 'Can add discount advance', 59, 'add_discountadvance'),
(234, 'Can change discount advance', 59, 'change_discountadvance'),
(235, 'Can delete discount advance', 59, 'delete_discountadvance'),
(236, 'Can view discount advance', 59, 'view_discountadvance'),
(237, 'Can add checkouts', 60, 'add_checkouts'),
(238, 'Can change checkouts', 60, 'change_checkouts'),
(239, 'Can delete checkouts', 60, 'delete_checkouts'),
(240, 'Can view checkouts', 60, 'view_checkouts'),
(241, 'Can add chat bot', 61, 'add_chatbot'),
(242, 'Can change chat bot', 61, 'change_chatbot'),
(243, 'Can delete chat bot', 61, 'delete_chatbot'),
(244, 'Can view chat bot', 61, 'view_chatbot'),
(245, 'Can add add_ place_ev', 62, 'add_add_place_ev'),
(246, 'Can change add_ place_ev', 62, 'change_add_place_ev'),
(247, 'Can delete add_ place_ev', 62, 'delete_add_place_ev'),
(248, 'Can view add_ place_ev', 62, 'view_add_place_ev'),
(249, 'Can add discounts', 63, 'add_discounts'),
(250, 'Can change discounts', 63, 'change_discounts'),
(251, 'Can delete discounts', 63, 'delete_discounts'),
(252, 'Can view discounts', 63, 'view_discounts'),
(253, 'Can add otp log', 64, 'add_otplog'),
(254, 'Can change otp log', 64, 'change_otplog'),
(255, 'Can delete otp log', 64, 'delete_otplog'),
(256, 'Can view otp log', 64, 'view_otplog');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-08-23 08:54:33.396440', '2', 'Sweet Love Catering', 1, '[{\"added\": {}}]', 13, 1),
(2, '2022-08-23 08:55:38.736070', '1', 'Cutting Board', 1, '[{\"added\": {}}]', 9, 1),
(3, '2022-08-23 08:56:36.074226', '1', 'Sweet Love Catering', 1, '[{\"added\": {}}]', 11, 1),
(4, '2022-08-23 08:56:52.201923', '1', '10', 1, '[{\"added\": {}}]', 57, 1),
(5, '2022-08-23 08:57:23.416638', '1', '20', 1, '[{\"added\": {}}]', 58, 1),
(6, '2022-08-23 08:57:30.962615', '1', '25', 1, '[{\"added\": {}}]', 59, 1),
(7, '2022-08-23 08:58:29.035181', '1', 'Sweet Love Catering', 1, '[{\"added\": {}}]', 24, 1),
(8, '2022-08-23 09:01:03.987868', '1', 'Sweet Love Catering', 2, '[{\"changed\": {\"fields\": [\"Live\"]}}]', 11, 1),
(9, '2022-08-23 11:28:45.943736', '1', 'Sweet Love Catering', 2, '[{\"changed\": {\"fields\": [\"SerivceId\"]}}]', 11, 1),
(10, '2022-08-24 05:00:25.212040', '1', '10', 1, '[{\"added\": {}}]', 63, 1),
(11, '2022-08-24 05:02:25.722520', '1', 'Sweet Love Catering', 2, '[]', 11, 1),
(12, '2022-08-24 05:03:06.399896', '2', '20', 1, '[{\"added\": {}}]', 63, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(6, 'authtoken', 'token'),
(7, 'authtoken', 'tokenproxy'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(62, 'userApi', 'add_place_ev'),
(9, 'userApi', 'add_service_ev'),
(10, 'userApi', 'advertisement'),
(61, 'userApi', 'chatbot'),
(60, 'userApi', 'checkouts'),
(11, 'userApi', 'createevent'),
(59, 'userApi', 'discountadvance'),
(58, 'userApi', 'discountonbill'),
(57, 'userApi', 'discountonequipment'),
(63, 'userApi', 'discounts'),
(12, 'userApi', 'emails'),
(56, 'userApi', 'equipments_pc'),
(55, 'userApi', 'equipments_pskill'),
(13, 'userApi', 'eventcategory'),
(14, 'userApi', 'eventcompanydetails'),
(54, 'userApi', 'eventcompanyimage'),
(53, 'userApi', 'eventcompanyvideo'),
(52, 'userApi', 'eventpersonaldetails'),
(51, 'userApi', 'exceluser'),
(50, 'userApi', 'fcmtoken'),
(15, 'userApi', 'forwho'),
(16, 'userApi', 'getintouch'),
(49, 'userApi', 'image_event'),
(48, 'userApi', 'membership'),
(47, 'userApi', 'message'),
(46, 'userApi', 'notification'),
(17, 'userApi', 'notificationdata'),
(64, 'userApi', 'otplog'),
(18, 'userApi', 'o_partnercompanys'),
(19, 'userApi', 'o_personalskills'),
(45, 'userApi', 'o_rats'),
(20, 'userApi', 'partnercompanycategory'),
(21, 'userApi', 'pc_artist'),
(44, 'userApi', 'pc_companyphotos'),
(43, 'userApi', 'pc_companyvideos'),
(22, 'userApi', 'pc_decor'),
(42, 'userApi', 'pc_equipments'),
(41, 'userApi', 'pc_photos'),
(40, 'userApi', 'pc_videos'),
(23, 'userApi', 'personalskillcategory'),
(39, 'userApi', 'personalskillsubcategory'),
(24, 'userApi', 'place_events'),
(38, 'userApi', 'ps_companyphotos'),
(37, 'userApi', 'ps_companyvideos'),
(36, 'userApi', 'ps_equipments'),
(35, 'userApi', 'ps_photo'),
(34, 'userApi', 'ps_video'),
(33, 'userApi', 'redeemcoins'),
(25, 'userApi', 'rooms'),
(32, 'userApi', 'servic'),
(31, 'userApi', 'serviceimage'),
(26, 'userApi', 'subscriptionplan'),
(30, 'userApi', 'tickets'),
(29, 'userApi', 'transactions'),
(8, 'userApi', 'user'),
(28, 'userApi', 'video_event'),
(27, 'userApi', 'wishlists');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'userApi', '0001_initial', '2022-08-23 08:45:52.264053'),
(2, 'contenttypes', '0001_initial', '2022-08-23 08:46:07.447718'),
(3, 'admin', '0001_initial', '2022-08-23 08:46:07.575712'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-08-23 08:46:07.601711'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-08-23 08:46:07.627715'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-08-23 08:46:07.717714'),
(7, 'auth', '0001_initial', '2022-08-23 08:46:08.134695'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-08-23 08:46:08.205712'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-08-23 08:46:08.219713'),
(10, 'auth', '0004_alter_user_username_opts', '2022-08-23 08:46:08.233309'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-08-23 08:46:08.247027'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-08-23 08:46:08.256027'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-08-23 08:46:08.278053'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-08-23 08:46:08.293054'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-08-23 08:46:08.306853'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-08-23 08:46:08.364420'),
(17, 'auth', '0011_update_proxy_permissions', '2022-08-23 08:46:08.411407'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-08-23 08:46:08.425422'),
(19, 'authtoken', '0001_initial', '2022-08-23 08:46:08.619372'),
(20, 'authtoken', '0002_auto_20160226_1747', '2022-08-23 08:46:08.707304'),
(21, 'authtoken', '0003_tokenproxy', '2022-08-23 08:46:08.723726'),
(22, 'sessions', '0001_initial', '2022-08-23 08:46:08.783600'),
(23, 'userApi', '0002_auto_20220823_1415', '2022-08-23 08:46:08.878992'),
(24, 'userApi', '0003_auto_20220823_1638', '2022-08-23 11:08:43.730701'),
(25, 'userApi', '0004_auto_20220823_1638', '2022-08-23 11:08:59.111642'),
(26, 'userApi', '0005_auto_20220823_1658', '2022-08-23 11:28:24.455851'),
(27, 'userApi', '0006_auto_20220823_1800', '2022-08-23 12:30:36.618093'),
(28, 'userApi', '0007_auto_20220824_1029', '2022-08-24 04:59:12.963626'),
(29, 'userApi', '0008_auto_20220824_1029', '2022-08-24 04:59:33.422782'),
(30, 'userApi', '0009_auto_20220905_1117', '2022-09-05 05:47:58.459965'),
(31, 'userApi', '0010_auto_20220905_1441', '2022-09-05 09:12:00.278415'),
(32, 'userApi', '0011_auto_20220905_1557', '2022-09-05 10:28:25.755477'),
(33, 'userApi', '0012_auto_20220905_1714', '2022-09-05 11:45:00.397691'),
(34, 'userApi', '0013_auto_20220905_1737', '2022-09-05 12:07:10.368885');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('am42frqcvip9udxiqnusv2400tmjm6w8', '.eJxVy80KAjEMBOB36VmW1pIm9abgc5R0k9LiD2J39SC-u7vgQY8z38zLJJ6nmuau99TE7Iwzm98u83jS6wpr3N_a8Gj67MPxwu18-OLfo3KvyzxoliiePI5ow1acCjtbyIJDH3PEIIUwQkFCgrgIkxNLgOCZuJj3B0PAMZM:1oQPYz:EFoYCGMdpH88MThILURxMUQOBRQEdpayyo6pLzNwcJ4', '2022-09-06 08:47:09.795366'),
('xcj0m2bpvfncynh6vvjeppi5htbjmox2', '.eJxVy80KAjEMBOB36VmW1pIm9abgc5R0k9LiD2J39SC-u7vgQY8z38zLJJ6nmuau99TE7Iwzm98u83jS6wpr3N_a8Gj67MPxwu18-OLfo3KvyzxoliiePI5ow1acCjtbyIJDH3PEIIUwQkFCgrgIkxNLgOCZuJj3B0PAMZM:1oTbsi:fyjL2Hz91kDz_-iIx_z7TR8FL9Fae8HBGccFqkEyQYY', '2022-09-15 04:32:44.477031');

-- --------------------------------------------------------

--
-- Table structure for table `userapi_add_place_ev`
--

CREATE TABLE `userapi_add_place_ev` (
  `Id` int(11) NOT NULL,
  `place_banner` varchar(100) DEFAULT NULL,
  `place_price` double NOT NULL,
  `price_type` varchar(255) NOT NULL,
  `details` varchar(2500) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `timestampe` datetime(6) NOT NULL,
  `event_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_add_place_ev`
--

INSERT INTO `userapi_add_place_ev` (`Id`, `place_banner`, `place_price`, `price_type`, `details`, `is_active`, `timestampe`, `event_id`, `user_id_id`) VALUES
(1, '', 2000, 'per_day', 'description', 1, '2022-09-05 12:11:57.808206', 1, 23),
(2, '', 2000, 'per_day', 'description update', 1, '2022-09-05 12:12:20.717677', 1, 23);

-- --------------------------------------------------------

--
-- Table structure for table `userapi_add_service_ev`
--

CREATE TABLE `userapi_add_service_ev` (
  `Id` int(11) NOT NULL,
  `service_name` varchar(500) NOT NULL,
  `service_price` double NOT NULL,
  `service_price_type` varchar(50) NOT NULL,
  `service_quantity` varchar(50) NOT NULL,
  `service_desc` longtext DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_add_service_ev`
--

INSERT INTO `userapi_add_service_ev` (`Id`, `service_name`, `service_price`, `service_price_type`, `service_quantity`, `service_desc`, `timestamp`, `is_active`) VALUES
(1, 'Cutting Board', 500, 'per_day', '20', 't is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed', '2022-08-23 08:55:38.735073', 1);

-- --------------------------------------------------------

--
-- Table structure for table `userapi_advertisement`
--

CREATE TABLE `userapi_advertisement` (
  `id` int(11) NOT NULL,
  `text` longtext DEFAULT NULL,
  `link` longtext NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `video` varchar(255) DEFAULT NULL,
  `position` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_chatbot`
--

CREATE TABLE `userapi_chatbot` (
  `id` bigint(20) NOT NULL,
  `message` longtext NOT NULL,
  `reply` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `sender_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_checkouts`
--

CREATE TABLE `userapi_checkouts` (
  `chkoId` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `phone_no` varchar(12) NOT NULL,
  `address` longtext NOT NULL,
  `eventId_id` int(11) DEFAULT NULL,
  `partnerId_id` int(11) DEFAULT NULL,
  `personalSkillId_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_createevent`
--

CREATE TABLE `userapi_createevent` (
  `event_type` varchar(50) NOT NULL,
  `eventId` int(11) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `t_and_c` longtext NOT NULL,
  `facebook` varchar(255) DEFAULT NULL,
  `twitter` varchar(255) DEFAULT NULL,
  `youtube` varchar(255) DEFAULT NULL,
  `pinterest` varchar(255) DEFAULT NULL,
  `instagram` varchar(255) DEFAULT NULL,
  `linkedin` varchar(255) DEFAULT NULL,
  `discountId` varchar(50) NOT NULL,
  `calender` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `timestampe` datetime(6) NOT NULL,
  `categoryId_id` int(11) NOT NULL,
  `e_user_id` int(11) NOT NULL,
  `serivceId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_createevent`
--

INSERT INTO `userapi_createevent` (`event_type`, `eventId`, `display_name`, `t_and_c`, `facebook`, `twitter`, `youtube`, `pinterest`, `instagram`, `linkedin`, `discountId`, `calender`, `live`, `is_active`, `timestampe`, `categoryId_id`, `e_user_id`, `serivceId_id`) VALUES
('places', 1, 'Sweet Love Catering', 't is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed', 'www.facebook.com', 'www.twitter.com', 'www.youtube.com', 'www.pinterest.com', 'www.instagram.com', 'www.linkedin.com', '1', '06-08-2022', 1, 1, '2022-08-23 08:56:36.066768', 2, 23, 1);

-- --------------------------------------------------------

--
-- Table structure for table `userapi_discounts`
--

CREATE TABLE `userapi_discounts` (
  `id` bigint(20) NOT NULL,
  `discount_type` varchar(50) NOT NULL,
  `discount` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `equipment_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_discounts`
--

INSERT INTO `userapi_discounts` (`id`, `discount_type`, `discount`, `is_active`, `timestamp`, `equipment_id`, `user_id`) VALUES
(1, 'discount_on_total_bill', '10', 0, '2022-08-24 05:00:25.204038', 1, 2),
(2, 'discount_on_total_bill', '20', 0, '2022-08-24 05:03:06.391895', NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `userapi_emails`
--

CREATE TABLE `userapi_emails` (
  `id` bigint(20) NOT NULL,
  `email` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_equipments_pc`
--

CREATE TABLE `userapi_equipments_pc` (
  `equpmentId` int(11) NOT NULL,
  `equpment` varchar(255) NOT NULL,
  `equpment_price` double NOT NULL,
  `equpment_price_period` double NOT NULL,
  `equpment_price_type` varchar(225) DEFAULT NULL,
  `equpment_details` longtext NOT NULL,
  `pcid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_equipments_pskill`
--

CREATE TABLE `userapi_equipments_pskill` (
  `equpmentId` int(11) NOT NULL,
  `equpment` varchar(255) NOT NULL,
  `equpment_price` double NOT NULL,
  `equpment_price_period` double NOT NULL,
  `equpment_price_type` varchar(225) DEFAULT NULL,
  `equpment_details` longtext NOT NULL,
  `pskillid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_eventcategory`
--

CREATE TABLE `userapi_eventcategory` (
  `categoryId` int(11) NOT NULL,
  `category_name` varchar(500) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `timestampe` datetime(6) NOT NULL,
  `display_name` varchar(500) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_eventcategory`
--

INSERT INTO `userapi_eventcategory` (`categoryId`, `category_name`, `is_active`, `timestampe`, `display_name`, `user_id`) VALUES
(2, 'Sweet Love Catering', 1, '2022-08-23 08:54:33.393441', NULL, 23),
(20, 'Caterers2', 1, '2022-09-05 11:49:18.640776', 'Catering', 23),
(21, 'Test', 1, '2022-09-05 11:49:43.246293', 'Sweet Love Catering', 24);

-- --------------------------------------------------------

--
-- Table structure for table `userapi_eventcompanydetails`
--

CREATE TABLE `userapi_eventcompanydetails` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gst` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `flat_no` varchar(255) NOT NULL,
  `street` varchar(255) NOT NULL,
  `area` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `pincode` varchar(255) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `eventId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_eventcompanyimage`
--

CREATE TABLE `userapi_eventcompanyimage` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `company_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_eventcompanyvideo`
--

CREATE TABLE `userapi_eventcompanyvideo` (
  `id` bigint(20) NOT NULL,
  `video` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `company_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_eventpersonaldetails`
--

CREATE TABLE `userapi_eventpersonaldetails` (
  `Id` int(11) NOT NULL,
  `professional_skill` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) NOT NULL,
  `mobile_no` varchar(20) NOT NULL,
  `is_mobile_no_hidden` tinyint(1) NOT NULL,
  `alt_mobile_no` varchar(20) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `is_email_hidden` tinyint(1) NOT NULL,
  `flat_no` varchar(100) DEFAULT NULL,
  `street` varchar(100) DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `eventId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_exceluser`
--

CREATE TABLE `userapi_exceluser` (
  `id` int(11) NOT NULL,
  `email` longtext DEFAULT NULL,
  `mobile_no` longtext DEFAULT NULL,
  `name` longtext DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `orgID_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_fcmtoken`
--

CREATE TABLE `userapi_fcmtoken` (
  `tokId` int(11) NOT NULL,
  `apptoken` longtext NOT NULL,
  `platform_type` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_forwho`
--

CREATE TABLE `userapi_forwho` (
  `Id` int(11) NOT NULL,
  `for_who` int(11) NOT NULL,
  `plan_name` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_getintouch`
--

CREATE TABLE `userapi_getintouch` (
  `gitId` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `message` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_image_event`
--

CREATE TABLE `userapi_image_event` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `image_details` varchar(255) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_membership`
--

CREATE TABLE `userapi_membership` (
  `id` int(11) NOT NULL,
  `plan_name` varchar(255) NOT NULL,
  `total_price` double DEFAULT NULL,
  `video_count` int(11) NOT NULL,
  `image_count` int(11) NOT NULL,
  `sms` tinyint(1) NOT NULL,
  `notifications` tinyint(1) NOT NULL,
  `emails` tinyint(1) NOT NULL,
  `socialmedia_promotion` tinyint(1) NOT NULL,
  `date_of_purchase` date NOT NULL,
  `date_of_expiry` date DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `payment_id` longtext DEFAULT NULL,
  `order_id` longtext DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_message`
--

CREATE TABLE `userapi_message` (
  `id` bigint(20) NOT NULL,
  `sender` bigint(20) NOT NULL,
  `receiver` bigint(20) NOT NULL,
  `content` longtext NOT NULL,
  `room` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `author_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_notification`
--

CREATE TABLE `userapi_notification` (
  `id` bigint(20) NOT NULL,
  `userIds` longtext DEFAULT NULL,
  `selected_business` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL,
  `membershipplan` varchar(10) NOT NULL,
  `selected_page` longtext DEFAULT NULL,
  `notification_type` longtext DEFAULT NULL,
  `notification_title` longtext DEFAULT NULL,
  `notification_text` longtext DEFAULT NULL,
  `notification_img` varchar(255) NOT NULL,
  `date_time` datetime(6) DEFAULT NULL,
  `organizer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_notificationdata`
--

CREATE TABLE `userapi_notificationdata` (
  `id` int(11) NOT NULL,
  `text` longtext NOT NULL,
  `image` varchar(255) NOT NULL,
  `notification_type` varchar(10) NOT NULL,
  `forwhat` varchar(255) DEFAULT NULL,
  `date_time` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_otplog`
--

CREATE TABLE `userapi_otplog` (
  `id` bigint(20) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `is_verify` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_otplog`
--

INSERT INTO `userapi_otplog` (`id`, `mobile`, `otp`, `is_verify`, `timestamp`) VALUES
(1, '+919328780020', '6764', 1, '2022-09-05 08:53:13.199019');

-- --------------------------------------------------------

--
-- Table structure for table `userapi_o_partnercompanys`
--

CREATE TABLE `userapi_o_partnercompanys` (
  `parcomId` int(11) NOT NULL,
  `category` varchar(250) DEFAULT NULL,
  `categoryId` int(11) DEFAULT NULL,
  `name` varchar(250) NOT NULL,
  `mobile_no` varchar(12) NOT NULL,
  `alt_mobile_no` varchar(12) NOT NULL,
  `email_id` varchar(250) NOT NULL,
  `equip_ids` varchar(255) DEFAULT NULL,
  `artist` varchar(250) DEFAULT NULL,
  `artist_price` double DEFAULT NULL,
  `decor` varchar(250) DEFAULT NULL,
  `decor_price` double DEFAULT NULL,
  `w_price` double NOT NULL,
  `w_discount` varchar(250) DEFAULT NULL,
  `travel_cost` varchar(250) DEFAULT NULL,
  `accommodation` varchar(250) DEFAULT NULL,
  `food` varchar(250) DEFAULT NULL,
  `com_name` varchar(250) NOT NULL,
  `com_gstfile` varchar(255) DEFAULT NULL,
  `com_contact` varchar(12) NOT NULL,
  `com_email` varchar(250) NOT NULL,
  `com_address` longtext NOT NULL,
  `let` longtext NOT NULL,
  `long` longtext NOT NULL,
  `price` double DEFAULT NULL,
  `facebook` varchar(500) NOT NULL,
  `youtube` varchar(500) NOT NULL,
  `twitter` varchar(500) NOT NULL,
  `pinterest` varchar(500) NOT NULL,
  `instagram` varchar(500) NOT NULL,
  `vimeo` varchar(500) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `whishlist_status` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_o_personalskills`
--

CREATE TABLE `userapi_o_personalskills` (
  `perskillId` int(11) NOT NULL,
  `pro_category` varchar(250) NOT NULL,
  `pro_category_id` int(11) DEFAULT NULL,
  `profession` varchar(250) NOT NULL,
  `profession_id` int(11) DEFAULT NULL,
  `name` varchar(250) NOT NULL,
  `mobile_no` varchar(12) NOT NULL,
  `alt_mobile_no` varchar(12) NOT NULL,
  `email` varchar(250) NOT NULL,
  `work_price` double NOT NULL,
  `is_price_per_hr` tinyint(1) NOT NULL,
  `work_discount` varchar(250) DEFAULT NULL,
  `travel_cost` varchar(250) DEFAULT NULL,
  `accommodation` varchar(250) DEFAULT NULL,
  `food` varchar(250) DEFAULT NULL,
  `equip_ids` varchar(255) DEFAULT NULL,
  `com_name` varchar(250) NOT NULL,
  `com_gstfile` varchar(255) DEFAULT NULL,
  `com_contact` varchar(12) NOT NULL,
  `com_email` varchar(250) NOT NULL,
  `com_address` longtext NOT NULL,
  `let` longtext NOT NULL,
  `long` longtext NOT NULL,
  `price` double DEFAULT NULL,
  `facebook` varchar(250) NOT NULL,
  `youtube` varchar(250) NOT NULL,
  `twitter` varchar(250) NOT NULL,
  `pinterest` varchar(250) NOT NULL,
  `instagram` varchar(250) NOT NULL,
  `vimeo` varchar(250) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `whishlist_status` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_o_rats`
--

CREATE TABLE `userapi_o_rats` (
  `ratId` int(11) NOT NULL,
  `stars` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(250) NOT NULL,
  `review` varchar(250) NOT NULL,
  `User_id` int(11) NOT NULL,
  `eventId_id` int(11) DEFAULT NULL,
  `partnerId_id` int(11) DEFAULT NULL,
  `personalId_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_partnercompanycategory`
--

CREATE TABLE `userapi_partnercompanycategory` (
  `Id` int(11) NOT NULL,
  `category` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_pc_artist`
--

CREATE TABLE `userapi_pc_artist` (
  `Id` int(11) NOT NULL,
  `artist` varchar(255) NOT NULL,
  `price` double NOT NULL,
  `price_type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_pc_companyphotos`
--

CREATE TABLE `userapi_pc_companyphotos` (
  `id` bigint(20) NOT NULL,
  `c_photo_file` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `pc_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_pc_companyvideos`
--

CREATE TABLE `userapi_pc_companyvideos` (
  `id` bigint(20) NOT NULL,
  `c_video_file` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `pc_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_pc_decor`
--

CREATE TABLE `userapi_pc_decor` (
  `Id` int(11) NOT NULL,
  `decor_type` varchar(255) NOT NULL,
  `decor_price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_pc_equipments`
--

CREATE TABLE `userapi_pc_equipments` (
  `Id` int(11) NOT NULL,
  `equ_name` varchar(255) NOT NULL,
  `equ_price` double NOT NULL,
  `equ_price_period` double NOT NULL,
  `equ_price_type` varchar(255) NOT NULL,
  `equ_details` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_pc_photos`
--

CREATE TABLE `userapi_pc_photos` (
  `id` bigint(20) NOT NULL,
  `photo_file` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `pc_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_pc_videos`
--

CREATE TABLE `userapi_pc_videos` (
  `id` bigint(20) NOT NULL,
  `video_file` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `pc_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_personalskillcategory`
--

CREATE TABLE `userapi_personalskillcategory` (
  `Id` int(11) NOT NULL,
  `category` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_personalskillsubcategory`
--

CREATE TABLE `userapi_personalskillsubcategory` (
  `Id` int(11) NOT NULL,
  `category` varchar(500) NOT NULL,
  `pscategoryid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_place_events`
--

CREATE TABLE `userapi_place_events` (
  `id` bigint(20) NOT NULL,
  `IncludingFacilities` varchar(100) NOT NULL,
  `person_capacity` double NOT NULL,
  `parking_capacity` double NOT NULL,
  `address` longtext NOT NULL,
  `let` longtext NOT NULL,
  `long` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_place_events`
--

INSERT INTO `userapi_place_events` (`id`, `IncludingFacilities`, `person_capacity`, `parking_capacity`, `address`, `let`, `long`, `is_active`, `timestamp`, `event_id`) VALUES
(1, 'romantic_stay', 250, 500, 't is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed', '27.3336555', '73.25448', 1, '2022-08-23 08:58:29.028688', 1);

-- --------------------------------------------------------

--
-- Table structure for table `userapi_ps_companyphotos`
--

CREATE TABLE `userapi_ps_companyphotos` (
  `id` bigint(20) NOT NULL,
  `c_photo_file` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `p_skill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_ps_companyvideos`
--

CREATE TABLE `userapi_ps_companyvideos` (
  `id` bigint(20) NOT NULL,
  `c_video_file` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `p_skill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_ps_equipments`
--

CREATE TABLE `userapi_ps_equipments` (
  `Id` int(11) NOT NULL,
  `equ_name` varchar(255) NOT NULL,
  `equ_price` double NOT NULL,
  `equ_price_period` double NOT NULL,
  `equ_price_type` varchar(255) NOT NULL,
  `equ_details` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_ps_photo`
--

CREATE TABLE `userapi_ps_photo` (
  `id` bigint(20) NOT NULL,
  `photo_file` varchar(255) NOT NULL,
  `photo_price_period` double NOT NULL,
  `photo_details` longtext NOT NULL,
  `live` tinyint(1) NOT NULL,
  `p_skill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_ps_video`
--

CREATE TABLE `userapi_ps_video` (
  `id` bigint(20) NOT NULL,
  `video_file` varchar(255) NOT NULL,
  `live` tinyint(1) NOT NULL,
  `p_skill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_redeemcoins`
--

CREATE TABLE `userapi_redeemcoins` (
  `id` int(11) NOT NULL,
  `Amount` varchar(50) DEFAULT NULL,
  `upi_id` longtext DEFAULT NULL,
  `price` double DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_rooms`
--

CREATE TABLE `userapi_rooms` (
  `Id` int(11) NOT NULL,
  `user` bigint(20) NOT NULL,
  `name` longtext NOT NULL,
  `roomid` longtext NOT NULL,
  `socketId` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_servic`
--

CREATE TABLE `userapi_servic` (
  `id` bigint(20) NOT NULL,
  `service_name` longtext DEFAULT NULL,
  `service_price` double DEFAULT NULL,
  `event_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_serviceimage`
--

CREATE TABLE `userapi_serviceimage` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `service_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_subscriptionplan`
--

CREATE TABLE `userapi_subscriptionplan` (
  `id` int(11) NOT NULL,
  `plan_name` varchar(255) NOT NULL,
  `plan_type` varchar(10) NOT NULL,
  `price` double NOT NULL,
  `discount_value` double NOT NULL,
  `discount_type` varchar(10) NOT NULL,
  `video_count` int(11) NOT NULL,
  `image_count` int(11) NOT NULL,
  `sms` tinyint(1) NOT NULL,
  `notifications` tinyint(1) NOT NULL,
  `emails` tinyint(1) NOT NULL,
  `socialmedia_promotion` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_tickets`
--

CREATE TABLE `userapi_tickets` (
  `holdername` longtext DEFAULT NULL,
  `holdercontact` varchar(225) DEFAULT NULL,
  `orgId` varchar(255) DEFAULT NULL,
  `ticketId` int(11) NOT NULL,
  `trans_Id` varchar(250) DEFAULT NULL,
  `img` longtext DEFAULT NULL,
  `ticket_no` varchar(250) NOT NULL,
  `payment_status` varchar(250) DEFAULT NULL,
  `amount` double DEFAULT NULL,
  `category` varchar(250) DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `receiver` varchar(255) DEFAULT NULL,
  `roomname` longtext NOT NULL,
  `eventId_id` int(11) DEFAULT NULL,
  `partnerId_id` int(11) DEFAULT NULL,
  `personalSkillId_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_transactions`
--

CREATE TABLE `userapi_transactions` (
  `id` int(11) NOT NULL,
  `img` longtext DEFAULT NULL,
  `translation_type` varchar(255) NOT NULL,
  `details` varchar(255) NOT NULL,
  `Amount` varchar(255) NOT NULL,
  `date` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_user`
--

CREATE TABLE `userapi_user` (
  `password` varchar(128) NOT NULL,
  `userId` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `phone_no` varchar(15) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `refer_code` varchar(8) DEFAULT NULL,
  `users_ref_code` varchar(8) NOT NULL,
  `profile_img` varchar(255) NOT NULL,
  `otp` varchar(4) DEFAULT NULL,
  `coins` varchar(11) NOT NULL,
  `user_type` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userapi_user`
--

INSERT INTO `userapi_user` (`password`, `userId`, `name`, `email`, `phone_no`, `date`, `last_login`, `is_admin`, `is_active`, `is_staff`, `is_superuser`, `refer_code`, `users_ref_code`, `profile_img`, `otp`, `coins`, `user_type`) VALUES
('pbkdf2_sha256$260000$efzZSf5IiPfdpKS1xCcAFy$YevAbWSTyuC2v0zIAWnhzF4/n7jN44fHXpNLAyaRw/0=', 1, 'ep', 'ep@gmail.com', NULL, '2022-08-23 08:46:45.293420', '2022-09-01 04:32:44.473035', 1, 1, 1, 1, NULL, '27f138c9', '../static/media/images.png', NULL, '0', '5'),
('pbkdf2_sha256$260000$GMRoAcShxeHFpUE8d9lVMm$thnlSxW+5+sNP3eUuD3eoKH9dMpK94pX9TWn2iYQHTE=', 2, 'Raj', 'raj@gmail.com', '9328780023', '2022-08-23 08:48:55.929165', '2022-08-23 08:48:55.929165', 0, 1, 0, 0, '84f233d7', '76ca6e30', '../static/media/images.png', NULL, '0', '4'),
('pbkdf2_sha256$260000$jDWLA5g1bXM14qKfgNwNm2$JEQ4hePsFptfhMkQeExgtefIB03k3MJUjYPHp3myqvY=', 20, 'Admin', 'admin@email.com', '9876542310', '2022-09-05 08:35:00.472193', '2022-09-05 08:35:00.472193', 1, 1, 0, 0, NULL, '9de6f829', '../static/media/images.png', NULL, '0', '1'),
('pbkdf2_sha256$260000$jyjFJCxNwvAUXDpIN6ov16$I6tUJ/tNlCqh2XUxViLk2twXntYtTAkxsIxvYEtPBpY=', 21, 'subadmin', 'subadmin@email.com', '9876543211', '2022-09-05 08:37:27.145404', '2022-09-05 08:37:27.145404', 0, 1, 1, 0, NULL, 'e388eb56', '../static/media/images.png', NULL, '0', '2'),
('pbkdf2_sha256$260000$8hFYZPdGFeCnjGExlhkZ8h$ape4PPqhLaxKx5ZQnU5reVo805EYSuEzsges3NrgfCY=', 22, 'Executive', 'executive@email.com', '987654322', '2022-09-05 08:37:44.526782', '2022-09-05 08:37:44.526782', 0, 1, 0, 0, NULL, '87caedef', '../static/media/images.png', NULL, '0', '3'),
('pbkdf2_sha256$260000$bOAe9yVkuunHL6pAXdc9xO$XC4924gTGF7o5vma31rHVSTCE6vEykAEBbxyFHrA9A8=', 23, 'organizer', 'organizer@email.com', '9328780021', '2022-09-05 08:38:07.186916', '2022-09-05 08:38:07.186916', 0, 1, 0, 0, NULL, '0e7fb05e', '../static/media/images.png', NULL, '0', '4'),
('pbkdf2_sha256$260000$KXB5myYltaki13qEWYyk7H$kUpnNCJLO7WIKut/lEQK5uJ+e0WmL/cNofOvobvAMoM=', 24, 'User', 'user@email.com', '9328780024', '2022-09-05 08:38:23.907694', '2022-09-05 08:38:23.907694', 0, 1, 0, 0, NULL, '54eab5b9', '../static/media/images.png', NULL, '0', '5');

-- --------------------------------------------------------

--
-- Table structure for table `userapi_video_event`
--

CREATE TABLE `userapi_video_event` (
  `id` bigint(20) NOT NULL,
  `video` varchar(100) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `detail` longtext DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userapi_wishlists`
--

CREATE TABLE `userapi_wishlists` (
  `wishId` int(11) NOT NULL,
  `img` longtext NOT NULL,
  `category` varchar(250) NOT NULL,
  `name_ev` varchar(250) NOT NULL,
  `place_ev` varchar(250) NOT NULL,
  `price_ev` double NOT NULL,
  `eventId_id` int(11) DEFAULT NULL,
  `partnerId_id` int(11) DEFAULT NULL,
  `personalId_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `userapi_add_place_ev`
--
ALTER TABLE `userapi_add_place_ev`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `userApi_add_place_ev_event_id_2886bf3d_fk_userApi_c` (`event_id`),
  ADD KEY `userApi_add_place_ev_user_id_id_8f0e14f1_fk_userApi_user_userId` (`user_id_id`);

--
-- Indexes for table `userapi_add_service_ev`
--
ALTER TABLE `userapi_add_service_ev`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `userapi_advertisement`
--
ALTER TABLE `userapi_advertisement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userapi_chatbot`
--
ALTER TABLE `userapi_chatbot`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_chatbot_sender_id_7c6422e0_fk_userApi_user_userId` (`sender_id`);

--
-- Indexes for table `userapi_checkouts`
--
ALTER TABLE `userapi_checkouts`
  ADD PRIMARY KEY (`chkoId`),
  ADD KEY `userApi_checkouts_eventId_id_fc38ef43_fk_userApi_c` (`eventId_id`),
  ADD KEY `userApi_checkouts_partnerId_id_ec856529_fk_userApi_o` (`partnerId_id`),
  ADD KEY `userApi_checkouts_personalSkillId_id_af8825e0_fk_userApi_o` (`personalSkillId_id`),
  ADD KEY `userApi_checkouts_user_id_c753b414_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_createevent`
--
ALTER TABLE `userapi_createevent`
  ADD PRIMARY KEY (`eventId`),
  ADD KEY `userApi_createevent_categoryId_id_7e262406_fk_userApi_e` (`categoryId_id`),
  ADD KEY `userApi_createevent_e_user_id_b54b2af1_fk_userApi_user_userId` (`e_user_id`),
  ADD KEY `userApi_createevent_serivceId_id_35f501d5` (`serivceId_id`);

--
-- Indexes for table `userapi_discounts`
--
ALTER TABLE `userapi_discounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_discounts_equipment_id_fce15b93_fk_userApi_a` (`equipment_id`),
  ADD KEY `userApi_discounts_user_id_ecdca5f2_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_emails`
--
ALTER TABLE `userapi_emails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userapi_equipments_pc`
--
ALTER TABLE `userapi_equipments_pc`
  ADD PRIMARY KEY (`equpmentId`),
  ADD KEY `userApi_equipments_p_pcid_id_a2fef32e_fk_userApi_o` (`pcid_id`);

--
-- Indexes for table `userapi_equipments_pskill`
--
ALTER TABLE `userapi_equipments_pskill`
  ADD PRIMARY KEY (`equpmentId`),
  ADD KEY `userApi_equipments_p_pskillid_id_cadc10df_fk_userApi_o` (`pskillid_id`);

--
-- Indexes for table `userapi_eventcategory`
--
ALTER TABLE `userapi_eventcategory`
  ADD PRIMARY KEY (`categoryId`),
  ADD KEY `userApi_eventcategory_user_id_c4857cff_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_eventcompanydetails`
--
ALTER TABLE `userapi_eventcompanydetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_eventcompany_eventId_id_6a88616a_fk_userApi_c` (`eventId_id`);

--
-- Indexes for table `userapi_eventcompanyimage`
--
ALTER TABLE `userapi_eventcompanyimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_eventcompany_company_id_id_bae71b4f_fk_userApi_e` (`company_id_id`);

--
-- Indexes for table `userapi_eventcompanyvideo`
--
ALTER TABLE `userapi_eventcompanyvideo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_eventcompany_company_id_id_18685970_fk_userApi_e` (`company_id_id`);

--
-- Indexes for table `userapi_eventpersonaldetails`
--
ALTER TABLE `userapi_eventpersonaldetails`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `userApi_eventpersona_eventId_id_46e8f2f8_fk_userApi_c` (`eventId_id`);

--
-- Indexes for table `userapi_exceluser`
--
ALTER TABLE `userapi_exceluser`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_exceluser_orgID_id_b09c1771_fk_userApi_user_userId` (`orgID_id`);

--
-- Indexes for table `userapi_fcmtoken`
--
ALTER TABLE `userapi_fcmtoken`
  ADD PRIMARY KEY (`tokId`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `userapi_forwho`
--
ALTER TABLE `userapi_forwho`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `userapi_getintouch`
--
ALTER TABLE `userapi_getintouch`
  ADD PRIMARY KEY (`gitId`);

--
-- Indexes for table `userapi_image_event`
--
ALTER TABLE `userapi_image_event`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_image_event_event_id_b14ad6d1_fk_userApi_c` (`event_id`);

--
-- Indexes for table `userapi_membership`
--
ALTER TABLE `userapi_membership`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_membership_user_id_65f1f5be_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_message`
--
ALTER TABLE `userapi_message`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_message_author_id_e74e92f9_fk_userApi_user_userId` (`author_id`);

--
-- Indexes for table `userapi_notification`
--
ALTER TABLE `userapi_notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_notification_organizer_id_a208d960_fk_userApi_u` (`organizer_id`);

--
-- Indexes for table `userapi_notificationdata`
--
ALTER TABLE `userapi_notificationdata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userapi_otplog`
--
ALTER TABLE `userapi_otplog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userapi_o_partnercompanys`
--
ALTER TABLE `userapi_o_partnercompanys`
  ADD PRIMARY KEY (`parcomId`),
  ADD KEY `userApi_o_partnercom_User_id_dbf01b84_fk_userApi_u` (`User_id`);

--
-- Indexes for table `userapi_o_personalskills`
--
ALTER TABLE `userapi_o_personalskills`
  ADD PRIMARY KEY (`perskillId`),
  ADD KEY `userApi_o_personalskills_User_id_59b5b81e_fk_userApi_user_userId` (`User_id`);

--
-- Indexes for table `userapi_o_rats`
--
ALTER TABLE `userapi_o_rats`
  ADD PRIMARY KEY (`ratId`),
  ADD KEY `userApi_o_rats_User_id_edd6de8e_fk_userApi_user_userId` (`User_id`),
  ADD KEY `userApi_o_rats_eventId_id_c762a653_fk_userApi_c` (`eventId_id`),
  ADD KEY `userApi_o_rats_partnerId_id_638c6c6d_fk_userApi_o` (`partnerId_id`),
  ADD KEY `userApi_o_rats_personalId_id_32facbbd_fk_userApi_o` (`personalId_id`);

--
-- Indexes for table `userapi_partnercompanycategory`
--
ALTER TABLE `userapi_partnercompanycategory`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `userapi_pc_artist`
--
ALTER TABLE `userapi_pc_artist`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `userapi_pc_companyphotos`
--
ALTER TABLE `userapi_pc_companyphotos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_pc_companyph_pc_id_c5cb1ea9_fk_userApi_o` (`pc_id`);

--
-- Indexes for table `userapi_pc_companyvideos`
--
ALTER TABLE `userapi_pc_companyvideos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_pc_companyvi_pc_id_4a1e6d8b_fk_userApi_o` (`pc_id`);

--
-- Indexes for table `userapi_pc_decor`
--
ALTER TABLE `userapi_pc_decor`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `userapi_pc_equipments`
--
ALTER TABLE `userapi_pc_equipments`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `userApi_pc_equipments_user_id_ad43d1cb_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_pc_photos`
--
ALTER TABLE `userapi_pc_photos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_pc_photos_pc_id_3860f0e5_fk_userApi_o` (`pc_id`);

--
-- Indexes for table `userapi_pc_videos`
--
ALTER TABLE `userapi_pc_videos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_pc_videos_pc_id_d9f2927a_fk_userApi_o` (`pc_id`);

--
-- Indexes for table `userapi_personalskillcategory`
--
ALTER TABLE `userapi_personalskillcategory`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `userapi_personalskillsubcategory`
--
ALTER TABLE `userapi_personalskillsubcategory`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `userApi_personalskil_pscategoryid_id_f8b27146_fk_userApi_p` (`pscategoryid_id`);

--
-- Indexes for table `userapi_place_events`
--
ALTER TABLE `userapi_place_events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_place_events_event_id_766871a3_fk_userApi_c` (`event_id`);

--
-- Indexes for table `userapi_ps_companyphotos`
--
ALTER TABLE `userapi_ps_companyphotos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_ps_companyph_p_skill_id_ba5df837_fk_userApi_o` (`p_skill_id`);

--
-- Indexes for table `userapi_ps_companyvideos`
--
ALTER TABLE `userapi_ps_companyvideos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_ps_companyvi_p_skill_id_43ecc754_fk_userApi_o` (`p_skill_id`);

--
-- Indexes for table `userapi_ps_equipments`
--
ALTER TABLE `userapi_ps_equipments`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `userApi_ps_equipments_user_id_ffe6471f_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_ps_photo`
--
ALTER TABLE `userapi_ps_photo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_ps_photo_p_skill_id_270589b5_fk_userApi_o` (`p_skill_id`);

--
-- Indexes for table `userapi_ps_video`
--
ALTER TABLE `userapi_ps_video`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_ps_video_p_skill_id_6d3d2c0a_fk_userApi_o` (`p_skill_id`);

--
-- Indexes for table `userapi_redeemcoins`
--
ALTER TABLE `userapi_redeemcoins`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_redeemcoins_user_id_43bb6924_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_rooms`
--
ALTER TABLE `userapi_rooms`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `userapi_servic`
--
ALTER TABLE `userapi_servic`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_servic_event_id_b7f6137f_fk_userApi_place_events_id` (`event_id`);

--
-- Indexes for table `userapi_serviceimage`
--
ALTER TABLE `userapi_serviceimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_serviceimage_service_id_56e97472_fk_userApi_a` (`service_id`);

--
-- Indexes for table `userapi_subscriptionplan`
--
ALTER TABLE `userapi_subscriptionplan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userapi_tickets`
--
ALTER TABLE `userapi_tickets`
  ADD PRIMARY KEY (`ticketId`),
  ADD UNIQUE KEY `ticket_no` (`ticket_no`),
  ADD KEY `userApi_tickets_eventId_id_191eadfe_fk_userApi_c` (`eventId_id`),
  ADD KEY `userApi_tickets_partnerId_id_7279c002_fk_userApi_o` (`partnerId_id`),
  ADD KEY `userApi_tickets_personalSkillId_id_7c253946_fk_userApi_o` (`personalSkillId_id`),
  ADD KEY `userApi_tickets_user_id_a18fc337_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_transactions`
--
ALTER TABLE `userapi_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_transactions_user_id_5acad74d_fk_userApi_user_userId` (`user_id`);

--
-- Indexes for table `userapi_user`
--
ALTER TABLE `userapi_user`
  ADD PRIMARY KEY (`userId`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `users_ref_code` (`users_ref_code`),
  ADD UNIQUE KEY `phone_no` (`phone_no`),
  ADD UNIQUE KEY `otp` (`otp`);

--
-- Indexes for table `userapi_video_event`
--
ALTER TABLE `userapi_video_event`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApi_video_event_event_id_73f8b273_fk_userApi_c` (`event_id`);

--
-- Indexes for table `userapi_wishlists`
--
ALTER TABLE `userapi_wishlists`
  ADD PRIMARY KEY (`wishId`),
  ADD KEY `userApi_wishlists_eventId_id_9755cf9d_fk_userApi_c` (`eventId_id`),
  ADD KEY `userApi_wishlists_partnerId_id_03a75836_fk_userApi_o` (`partnerId_id`),
  ADD KEY `userApi_wishlists_personalId_id_bcebf92c_fk_userApi_o` (`personalId_id`),
  ADD KEY `userApi_wishlists_user_id_3fa3a12f_fk_userApi_user_userId` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=257;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `userapi_add_place_ev`
--
ALTER TABLE `userapi_add_place_ev`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userapi_add_service_ev`
--
ALTER TABLE `userapi_add_service_ev`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `userapi_advertisement`
--
ALTER TABLE `userapi_advertisement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_chatbot`
--
ALTER TABLE `userapi_chatbot`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_checkouts`
--
ALTER TABLE `userapi_checkouts`
  MODIFY `chkoId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_createevent`
--
ALTER TABLE `userapi_createevent`
  MODIFY `eventId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `userapi_discounts`
--
ALTER TABLE `userapi_discounts`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userapi_emails`
--
ALTER TABLE `userapi_emails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_eventcategory`
--
ALTER TABLE `userapi_eventcategory`
  MODIFY `categoryId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `userapi_eventcompanydetails`
--
ALTER TABLE `userapi_eventcompanydetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_eventcompanyimage`
--
ALTER TABLE `userapi_eventcompanyimage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_eventcompanyvideo`
--
ALTER TABLE `userapi_eventcompanyvideo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_eventpersonaldetails`
--
ALTER TABLE `userapi_eventpersonaldetails`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_exceluser`
--
ALTER TABLE `userapi_exceluser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_fcmtoken`
--
ALTER TABLE `userapi_fcmtoken`
  MODIFY `tokId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_forwho`
--
ALTER TABLE `userapi_forwho`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_getintouch`
--
ALTER TABLE `userapi_getintouch`
  MODIFY `gitId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_image_event`
--
ALTER TABLE `userapi_image_event`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_membership`
--
ALTER TABLE `userapi_membership`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_message`
--
ALTER TABLE `userapi_message`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_notification`
--
ALTER TABLE `userapi_notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_notificationdata`
--
ALTER TABLE `userapi_notificationdata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_otplog`
--
ALTER TABLE `userapi_otplog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `userapi_o_partnercompanys`
--
ALTER TABLE `userapi_o_partnercompanys`
  MODIFY `parcomId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_o_personalskills`
--
ALTER TABLE `userapi_o_personalskills`
  MODIFY `perskillId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_o_rats`
--
ALTER TABLE `userapi_o_rats`
  MODIFY `ratId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_partnercompanycategory`
--
ALTER TABLE `userapi_partnercompanycategory`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_pc_artist`
--
ALTER TABLE `userapi_pc_artist`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_pc_companyphotos`
--
ALTER TABLE `userapi_pc_companyphotos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_pc_companyvideos`
--
ALTER TABLE `userapi_pc_companyvideos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_pc_decor`
--
ALTER TABLE `userapi_pc_decor`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_pc_equipments`
--
ALTER TABLE `userapi_pc_equipments`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_pc_photos`
--
ALTER TABLE `userapi_pc_photos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_pc_videos`
--
ALTER TABLE `userapi_pc_videos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_personalskillcategory`
--
ALTER TABLE `userapi_personalskillcategory`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_personalskillsubcategory`
--
ALTER TABLE `userapi_personalskillsubcategory`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_place_events`
--
ALTER TABLE `userapi_place_events`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `userapi_ps_companyphotos`
--
ALTER TABLE `userapi_ps_companyphotos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_ps_companyvideos`
--
ALTER TABLE `userapi_ps_companyvideos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_ps_equipments`
--
ALTER TABLE `userapi_ps_equipments`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_ps_photo`
--
ALTER TABLE `userapi_ps_photo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_ps_video`
--
ALTER TABLE `userapi_ps_video`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_redeemcoins`
--
ALTER TABLE `userapi_redeemcoins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_rooms`
--
ALTER TABLE `userapi_rooms`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_servic`
--
ALTER TABLE `userapi_servic`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_serviceimage`
--
ALTER TABLE `userapi_serviceimage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_subscriptionplan`
--
ALTER TABLE `userapi_subscriptionplan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_tickets`
--
ALTER TABLE `userapi_tickets`
  MODIFY `ticketId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_transactions`
--
ALTER TABLE `userapi_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_user`
--
ALTER TABLE `userapi_user`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `userapi_video_event`
--
ALTER TABLE `userapi_video_event`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `userapi_wishlists`
--
ALTER TABLE `userapi_wishlists`
  MODIFY `wishId` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_add_place_ev`
--
ALTER TABLE `userapi_add_place_ev`
  ADD CONSTRAINT `userApi_add_place_ev_event_id_2886bf3d_fk_userApi_c` FOREIGN KEY (`event_id`) REFERENCES `userapi_createevent` (`eventId`),
  ADD CONSTRAINT `userApi_add_place_ev_user_id_id_8f0e14f1_fk_userApi_user_userId` FOREIGN KEY (`user_id_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_chatbot`
--
ALTER TABLE `userapi_chatbot`
  ADD CONSTRAINT `userApi_chatbot_sender_id_7c6422e0_fk_userApi_user_userId` FOREIGN KEY (`sender_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_checkouts`
--
ALTER TABLE `userapi_checkouts`
  ADD CONSTRAINT `userApi_checkouts_eventId_id_fc38ef43_fk_userApi_c` FOREIGN KEY (`eventId_id`) REFERENCES `userapi_createevent` (`eventId`),
  ADD CONSTRAINT `userApi_checkouts_partnerId_id_ec856529_fk_userApi_o` FOREIGN KEY (`partnerId_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`),
  ADD CONSTRAINT `userApi_checkouts_personalSkillId_id_af8825e0_fk_userApi_o` FOREIGN KEY (`personalSkillId_id`) REFERENCES `userapi_o_personalskills` (`perskillId`),
  ADD CONSTRAINT `userApi_checkouts_user_id_c753b414_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_createevent`
--
ALTER TABLE `userapi_createevent`
  ADD CONSTRAINT `userApi_createevent_categoryId_id_7e262406_fk_userApi_e` FOREIGN KEY (`categoryId_id`) REFERENCES `userapi_eventcategory` (`categoryId`),
  ADD CONSTRAINT `userApi_createevent_e_user_id_b54b2af1_fk_userApi_user_userId` FOREIGN KEY (`e_user_id`) REFERENCES `userapi_user` (`userId`),
  ADD CONSTRAINT `userApi_createevent_serivceId_id_35f501d5_fk_userApi_a` FOREIGN KEY (`serivceId_id`) REFERENCES `userapi_add_service_ev` (`Id`);

--
-- Constraints for table `userapi_discounts`
--
ALTER TABLE `userapi_discounts`
  ADD CONSTRAINT `userApi_discounts_equipment_id_fce15b93_fk_userApi_a` FOREIGN KEY (`equipment_id`) REFERENCES `userapi_add_service_ev` (`Id`),
  ADD CONSTRAINT `userApi_discounts_user_id_ecdca5f2_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_equipments_pc`
--
ALTER TABLE `userapi_equipments_pc`
  ADD CONSTRAINT `userApi_equipments_p_pcid_id_a2fef32e_fk_userApi_o` FOREIGN KEY (`pcid_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`);

--
-- Constraints for table `userapi_equipments_pskill`
--
ALTER TABLE `userapi_equipments_pskill`
  ADD CONSTRAINT `userApi_equipments_p_pskillid_id_cadc10df_fk_userApi_o` FOREIGN KEY (`pskillid_id`) REFERENCES `userapi_o_personalskills` (`perskillId`);

--
-- Constraints for table `userapi_eventcompanydetails`
--
ALTER TABLE `userapi_eventcompanydetails`
  ADD CONSTRAINT `userApi_eventcompany_eventId_id_6a88616a_fk_userApi_c` FOREIGN KEY (`eventId_id`) REFERENCES `userapi_createevent` (`eventId`);

--
-- Constraints for table `userapi_eventcompanyimage`
--
ALTER TABLE `userapi_eventcompanyimage`
  ADD CONSTRAINT `userApi_eventcompany_company_id_id_bae71b4f_fk_userApi_e` FOREIGN KEY (`company_id_id`) REFERENCES `userapi_eventcompanydetails` (`id`);

--
-- Constraints for table `userapi_eventcompanyvideo`
--
ALTER TABLE `userapi_eventcompanyvideo`
  ADD CONSTRAINT `userApi_eventcompany_company_id_id_18685970_fk_userApi_e` FOREIGN KEY (`company_id_id`) REFERENCES `userapi_eventcompanydetails` (`id`);

--
-- Constraints for table `userapi_eventpersonaldetails`
--
ALTER TABLE `userapi_eventpersonaldetails`
  ADD CONSTRAINT `userApi_eventpersona_eventId_id_46e8f2f8_fk_userApi_c` FOREIGN KEY (`eventId_id`) REFERENCES `userapi_createevent` (`eventId`);

--
-- Constraints for table `userapi_exceluser`
--
ALTER TABLE `userapi_exceluser`
  ADD CONSTRAINT `userApi_exceluser_orgID_id_b09c1771_fk_userApi_user_userId` FOREIGN KEY (`orgID_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_fcmtoken`
--
ALTER TABLE `userapi_fcmtoken`
  ADD CONSTRAINT `userApi_fcmtoken_user_id_72e84506_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_image_event`
--
ALTER TABLE `userapi_image_event`
  ADD CONSTRAINT `userApi_image_event_event_id_b14ad6d1_fk_userApi_c` FOREIGN KEY (`event_id`) REFERENCES `userapi_createevent` (`eventId`);

--
-- Constraints for table `userapi_membership`
--
ALTER TABLE `userapi_membership`
  ADD CONSTRAINT `userApi_membership_user_id_65f1f5be_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_message`
--
ALTER TABLE `userapi_message`
  ADD CONSTRAINT `userApi_message_author_id_e74e92f9_fk_userApi_user_userId` FOREIGN KEY (`author_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_notification`
--
ALTER TABLE `userapi_notification`
  ADD CONSTRAINT `userApi_notification_organizer_id_a208d960_fk_userApi_u` FOREIGN KEY (`organizer_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_o_partnercompanys`
--
ALTER TABLE `userapi_o_partnercompanys`
  ADD CONSTRAINT `userApi_o_partnercom_User_id_dbf01b84_fk_userApi_u` FOREIGN KEY (`User_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_o_personalskills`
--
ALTER TABLE `userapi_o_personalskills`
  ADD CONSTRAINT `userApi_o_personalskills_User_id_59b5b81e_fk_userApi_user_userId` FOREIGN KEY (`User_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_o_rats`
--
ALTER TABLE `userapi_o_rats`
  ADD CONSTRAINT `userApi_o_rats_User_id_edd6de8e_fk_userApi_user_userId` FOREIGN KEY (`User_id`) REFERENCES `userapi_user` (`userId`),
  ADD CONSTRAINT `userApi_o_rats_eventId_id_c762a653_fk_userApi_c` FOREIGN KEY (`eventId_id`) REFERENCES `userapi_createevent` (`eventId`),
  ADD CONSTRAINT `userApi_o_rats_partnerId_id_638c6c6d_fk_userApi_o` FOREIGN KEY (`partnerId_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`),
  ADD CONSTRAINT `userApi_o_rats_personalId_id_32facbbd_fk_userApi_o` FOREIGN KEY (`personalId_id`) REFERENCES `userapi_o_personalskills` (`perskillId`);

--
-- Constraints for table `userapi_pc_companyphotos`
--
ALTER TABLE `userapi_pc_companyphotos`
  ADD CONSTRAINT `userApi_pc_companyph_pc_id_c5cb1ea9_fk_userApi_o` FOREIGN KEY (`pc_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`);

--
-- Constraints for table `userapi_pc_companyvideos`
--
ALTER TABLE `userapi_pc_companyvideos`
  ADD CONSTRAINT `userApi_pc_companyvi_pc_id_4a1e6d8b_fk_userApi_o` FOREIGN KEY (`pc_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`);

--
-- Constraints for table `userapi_pc_equipments`
--
ALTER TABLE `userapi_pc_equipments`
  ADD CONSTRAINT `userApi_pc_equipments_user_id_ad43d1cb_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_pc_photos`
--
ALTER TABLE `userapi_pc_photos`
  ADD CONSTRAINT `userApi_pc_photos_pc_id_3860f0e5_fk_userApi_o` FOREIGN KEY (`pc_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`);

--
-- Constraints for table `userapi_pc_videos`
--
ALTER TABLE `userapi_pc_videos`
  ADD CONSTRAINT `userApi_pc_videos_pc_id_d9f2927a_fk_userApi_o` FOREIGN KEY (`pc_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`);

--
-- Constraints for table `userapi_personalskillsubcategory`
--
ALTER TABLE `userapi_personalskillsubcategory`
  ADD CONSTRAINT `userApi_personalskil_pscategoryid_id_f8b27146_fk_userApi_p` FOREIGN KEY (`pscategoryid_id`) REFERENCES `userapi_personalskillcategory` (`Id`);

--
-- Constraints for table `userapi_place_events`
--
ALTER TABLE `userapi_place_events`
  ADD CONSTRAINT `userApi_place_events_event_id_766871a3_fk_userApi_c` FOREIGN KEY (`event_id`) REFERENCES `userapi_createevent` (`eventId`);

--
-- Constraints for table `userapi_ps_companyphotos`
--
ALTER TABLE `userapi_ps_companyphotos`
  ADD CONSTRAINT `userApi_ps_companyph_p_skill_id_ba5df837_fk_userApi_o` FOREIGN KEY (`p_skill_id`) REFERENCES `userapi_o_personalskills` (`perskillId`);

--
-- Constraints for table `userapi_ps_companyvideos`
--
ALTER TABLE `userapi_ps_companyvideos`
  ADD CONSTRAINT `userApi_ps_companyvi_p_skill_id_43ecc754_fk_userApi_o` FOREIGN KEY (`p_skill_id`) REFERENCES `userapi_o_personalskills` (`perskillId`);

--
-- Constraints for table `userapi_ps_equipments`
--
ALTER TABLE `userapi_ps_equipments`
  ADD CONSTRAINT `userApi_ps_equipments_user_id_ffe6471f_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_ps_photo`
--
ALTER TABLE `userapi_ps_photo`
  ADD CONSTRAINT `userApi_ps_photo_p_skill_id_270589b5_fk_userApi_o` FOREIGN KEY (`p_skill_id`) REFERENCES `userapi_o_personalskills` (`perskillId`);

--
-- Constraints for table `userapi_ps_video`
--
ALTER TABLE `userapi_ps_video`
  ADD CONSTRAINT `userApi_ps_video_p_skill_id_6d3d2c0a_fk_userApi_o` FOREIGN KEY (`p_skill_id`) REFERENCES `userapi_o_personalskills` (`perskillId`);

--
-- Constraints for table `userapi_redeemcoins`
--
ALTER TABLE `userapi_redeemcoins`
  ADD CONSTRAINT `userApi_redeemcoins_user_id_43bb6924_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_servic`
--
ALTER TABLE `userapi_servic`
  ADD CONSTRAINT `userApi_servic_event_id_b7f6137f_fk_userApi_place_events_id` FOREIGN KEY (`event_id`) REFERENCES `userapi_place_events` (`id`);

--
-- Constraints for table `userapi_serviceimage`
--
ALTER TABLE `userapi_serviceimage`
  ADD CONSTRAINT `userApi_serviceimage_service_id_56e97472_fk_userApi_a` FOREIGN KEY (`service_id`) REFERENCES `userapi_add_service_ev` (`Id`);

--
-- Constraints for table `userapi_tickets`
--
ALTER TABLE `userapi_tickets`
  ADD CONSTRAINT `userApi_tickets_eventId_id_191eadfe_fk_userApi_c` FOREIGN KEY (`eventId_id`) REFERENCES `userapi_createevent` (`eventId`),
  ADD CONSTRAINT `userApi_tickets_partnerId_id_7279c002_fk_userApi_o` FOREIGN KEY (`partnerId_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`),
  ADD CONSTRAINT `userApi_tickets_personalSkillId_id_7c253946_fk_userApi_o` FOREIGN KEY (`personalSkillId_id`) REFERENCES `userapi_o_personalskills` (`perskillId`),
  ADD CONSTRAINT `userApi_tickets_user_id_a18fc337_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_transactions`
--
ALTER TABLE `userapi_transactions`
  ADD CONSTRAINT `userApi_transactions_user_id_5acad74d_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);

--
-- Constraints for table `userapi_video_event`
--
ALTER TABLE `userapi_video_event`
  ADD CONSTRAINT `userApi_video_event_event_id_73f8b273_fk_userApi_c` FOREIGN KEY (`event_id`) REFERENCES `userapi_createevent` (`eventId`);

--
-- Constraints for table `userapi_wishlists`
--
ALTER TABLE `userapi_wishlists`
  ADD CONSTRAINT `userApi_wishlists_eventId_id_9755cf9d_fk_userApi_c` FOREIGN KEY (`eventId_id`) REFERENCES `userapi_createevent` (`eventId`),
  ADD CONSTRAINT `userApi_wishlists_partnerId_id_03a75836_fk_userApi_o` FOREIGN KEY (`partnerId_id`) REFERENCES `userapi_o_partnercompanys` (`parcomId`),
  ADD CONSTRAINT `userApi_wishlists_personalId_id_bcebf92c_fk_userApi_o` FOREIGN KEY (`personalId_id`) REFERENCES `userapi_o_personalskills` (`perskillId`),
  ADD CONSTRAINT `userApi_wishlists_user_id_3fa3a12f_fk_userApi_user_userId` FOREIGN KEY (`user_id`) REFERENCES `userapi_user` (`userId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
