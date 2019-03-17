CREATE DATABASE `bucket_list` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

USE bucket_list;

CREATE TABLE `users` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id identify user',
    `open_id` varchar(128) NOT NULL DEFAULT '0' COMMENT 'wechat openid',
    `name` varchar(64) NOT NUll DEFAULT '' COMMENT 'nick name',
    `c_time` int(11) unsigned NOT NUll DEFAULT '0' COMMENT 'user create time',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `questions` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id identify question',
    `owner_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'owner',
    `content` varchar(1024) NOT NULL DEFAULT '' COMMENT 'question',
    `c_time` int(11) unsigned NOT NUll DEFAULT '0' COMMENT 'question create time',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`owner_id`) REFERENCES users(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `answers` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id identify question',
    `q_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'question id',
    `owner_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'owner',
    `content` varchar(1024) NOT NULL DEFAULT '' COMMENT 'answer',
    `c_time` int(11) unsigned NOT NUll DEFAULT '0' COMMENT 'answer create time',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`q_id`) REFERENCES questions(`id`),
    FOREIGN KEY (`owner_id`) REFERENCES users(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;