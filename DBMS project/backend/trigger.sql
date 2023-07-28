create table book_backup (ISBN varchar(10),title varchar(20),category varchar(10),price int,staffid varchar(10),publisherid varchar(10),userid varchar(10));

delimiter $$
create trigger book_backup
before delete
on Book for each row
begin
insert into book_backup select * from Book where ISBN = old.ISBN;
end$$
delimiter ;
delete from book where ISBN = 'book3091';
select * from book_backup;

