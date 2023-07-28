create database pes1ug20cs479_library_management_system;

use pes1ug20cs479_library_management_system;

create table Report (regno int,bookno int,issuedate date,staffid varchar(10));

create table Staff (staffid varchar(10),staffname varchar(20),loginid varchar(10));

create table Reader (userid varchar(10),email varchar(30),readername varchar(20),staffid varchar(10));

create table Book (ISBN varchar(10),title varchar(20),category varchar(10),price int,staffid varchar(10),publisherid varchar(10),userid varchar(10));

create table Publisher (publisherid varchar(10),publishername varchar(20),yearofpublication int);

create table Authentication (loginid varchar(10),password varchar(15));

create table Readerphone (userid varchar(10),phoneno char(10));

alter table Report add primary key(regno,staffid);

alter table Staff add primary key(staffid,loginid);

alter table Reader add primary key(userid,staffid);

alter table Book add primary key(ISBN,staffid,publisherid,userid);

alter table Publisher add primary key(publisherid);

alter table Authentication add primary key(loginid);

alter table Readerphone add primary key(userid);

alter table Report add foreign key(staffid) references Staff(staffid);

alter table Staff add foreign key(loginid) references Authentication(loginid);

alter table Reader add foreign key(staffid) references Staff(staffid);

alter table Book add foreign key(staffid) references Staff(staffid),add foreign key(publisherid) references Publisher(publisherid),add foreign key(userid) references Reader(userid);

alter table Readerphone add foreign key(userid) references Reader(userid);