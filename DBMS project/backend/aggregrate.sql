select min(price) as minimum_price_of_book from Book;

select count(phoneno) as number_of_phone_numbers from Readerphone;

select avg(price) as average_price_of_book from Book;

select sum(price) as sum_of_prices_of_books from Book where price > (select avg(price) from Book);
