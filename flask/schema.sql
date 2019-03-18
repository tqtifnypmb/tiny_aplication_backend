CREATE DATABASE IF NOT EXISTS `bucket_list` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

USE bucket_list;

CREATE TABLE IF NOT EXISTS `users` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id identify user',
    `open_id` varchar(128) NOT NULL DEFAULT '0' COMMENT 'wechat openid',
    `name` varchar(64) NOT NULL DEFAULT '' COMMENT 'nick name',
    `c_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'user create time',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `questions` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id identify question',
    `owner_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'owner',
    `title` varchar(256) NOT NULL DEFAULT '' COMMENT 'title of question',
    `content` varchar(1024) NOT NULL DEFAULT '' COMMENT 'question',
    `c_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'question create time',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`owner_id`) REFERENCES users(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `answers` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id identify question',
    `q_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'question id',
    `owner_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'owner',
    `content` varchar(1024) NOT NULL DEFAULT '' COMMENT 'answer',
    `c_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'answer create time',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`q_id`) REFERENCES questions(`id`),
    FOREIGN KEY (`owner_id`) REFERENCES users(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;