delimiter $$
create procedure final_price2()
begin
select ISBN,title,category,price + 12/100 * price as price from Book;
end$$
delimiter ;
call final_price2();