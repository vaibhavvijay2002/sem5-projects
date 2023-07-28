set foreign_key_checks = 0;

insert into Report values (12345,87,'2022-10-30','staff159'),(89895,23,'2022-11-28','staff123'),(90931,28,'2022-8-17','staff619'),(47883,66,'2022-12-20','staff179'),(93840,37,'2022-10-15','staff896');

insert into Staff values ('staff159','Ram','login9093'),('staff179','Raju','login8343'),('staff678','Krishna','login2321'),('staff999','Ravan','login5767'),('staff896','Bheeshma','login9981');

insert into Reader values ('user4341','user4341@gmail.com','Pawan Kumar','staff159'),('user9037','user9037@gmail.com','Ajay Thakur','staff179'),('user7844','user7844@gmail.com','Rohit Sharma','staff981'),('user9112','user9122@gmail.com','Harshal Patel','staff129'),('user7891','user7891@gmail.com','Ravi Shastri','staff619');

insert into Book values ('book8939','Drishyam','Crime',500,'staff179','publ38','user9037'),('book9891','KGF','Action',1000,'staff169','publ77','user7891'),('book3091','Birbal','Thriller',300,'staff159','publ45','user8192'),('book9121','Brahmastra','Fantasy',1500,'staff962','publ81','user9112'),('book1239','Aake','Horror',700,'staff981','publ95','user7644');

insert into Publisher values ('publ38','Hrithik Roshan',2018),('publ28','Thalapathy Vijay',2020),('publ95','Puneeth Rajkumar',2015),('publ81','Mahesh Babu',2011),('publ30','Ram Charan',2021);

insert into Authentication values ('login9093','password8'),('login5588','password5'),('login2321','password3'),('login3873','password7'),('login5767','password3');

insert into Readerphone values ('user4341',4798989401),('user7844',8387811401),('user8563',8989384934),('user9112',8032562250),('user1005',5999092026);

set foreign_key_checks = 1;
