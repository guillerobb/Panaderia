-- SQLite
select * from sales_sale;
select * from sales_detail;
select * from sales_detail where price is NULL;
UPDATE sales_detail SET price = 1 where price is NULL;