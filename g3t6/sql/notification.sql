DROP SCHEMA IF EXISTS Notification;
create schema Notification; /*creating schema */
use Notification;


CREATE TABLE UserChatID /*creating course table*/
(
TelegramHandle  varchar(100)    not null,
ChatID	int(100)    not null				,
CONSTRAINT	notification_pk	PRIMARY KEY (TelegramHandle)
);