CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(20) NOT NULL AUTO_INCREMENT,
  `last_challenge_time` int(20) NOT NULL,
  `last_challenge_group` int(20) NOT NULL,
  `join_count` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;