delimiter $$
create function final_price1(price int)
returns int
begin
declare vv int;
if price < 500 then
set vv = price - 5/100 * price;
elseif price >= 500 and price <= 1000 then
set vv = price - 10/100 * price;
elseif price > 1000 then
set vv = price - 15/100 * price;
end if;
return vv;
end$$
delimiter ;
select ISBN,title,category,final_price1(price) from Book;

