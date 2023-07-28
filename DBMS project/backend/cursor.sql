create table backup_book (ISBN varchar(10),title varchar(20),category varchar(10),price int,staffid varchar(10),publisherid varchar(10),userid varchar(10));

delimiter $$
create procedure backup_of_book()
begin
declare done int default 0;
declare vISBN varchar(10);
declare vtitle varchar(20);
declare vcategory varchar(10);
declare vprice int;
declare vstaffid varchar(10);
declare vpublisherid varchar(10);
declare vuserid varchar(10);
declare book_cursor cursor for select * from Book;
declare continue handler for not found set done = 1;
open book_cursor;
label: loop
fetch book_cursor into vISBN,vtitle,vcategory,vprice,vstaffid,vpublisherid,vuserid;
insert into backup_book values (vISBN,vtitle,vcategory,vprice,vstaffid,vpublisherid,vuserid);
if done = 1 then leave label;
end if;
end loop;
close book_cursor;
end$$
delimiter ;
call backup_of_book;
select * from backup_book;