/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50096
Source Host           : localhost:3306
Source Database       : imooc

Target Server Type    : MYSQL
Target Server Version : 50096
File Encoding         : 65001

Date: 2015-08-22 18:03:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `account`
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `acctid` int(11) NOT NULL auto_increment,
  `name` varchar(255) NOT NULL,
  `money` bigint(20) NOT NULL,
  PRIMARY KEY  (`acctid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES ('1', 'john', '79');
INSERT INTO `account` VALUES ('2', 'lucy', '1510');

-- ----------------------------
-- Table structure for `tuser`
-- ----------------------------
DROP TABLE IF EXISTS `tuser`;
CREATE TABLE `tuser` (
  `userid` int(11) NOT NULL auto_increment,
  `usrname` varchar(50) default NULL,
  PRIMARY KEY  (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tuser
-- ----------------------------
INSERT INTO `tuser` VALUES ('1', 'jhon');
INSERT INTO `tuser` VALUES ('3', 'user3');
INSERT INTO `tuser` VALUES ('4', 'hell');
INSERT INTO `tuser` VALUES ('9', 'lucy');
INSERT INTO `tuser` VALUES ('11', 'lucy');
