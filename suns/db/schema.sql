CREATE TABLE IF NOT EXISTS `texts` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `conetnt` varchar(1024) NOT NULL DEFAULT '',
    `c_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'create time',
    `a_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'access time',
    `used` int(1) unsigned NOT NULL DEFAULT '0' COMMENT 'is used',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `songs` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `url` varchar(2084) NOT NULL DEFAULT '',
    `a_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'access time',
    `used` int(1) unsigned NOT NULL DEFAULT '0' COMMENT 'is used',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `images` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL DEFAULT '',
    `a_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'access time',
    `used` int(1) unsigned NOT NULL DEFAULT '0' COMMENT 'is used',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;