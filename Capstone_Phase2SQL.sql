create database CapstoneTable1;
show databases;
use CapstoneTable1;

#query1: 1 Write a query  to retrieve all shoe names and their corresponding prices for men's shoes:
SELECT * FROM TABLE_1;
SELECT Shoe_Name, Shoe_Price from Table_1 where Category = "Men";

#Query2: Write a query to retrieve the number of different colors available for each category.
SELECT category, COUNT(DISTINCT color) AS num_colors
FROM products
GROUP BY category;


#Query3: Write a query to find the most expensive men's shoe.
Select max(Shoe_Price) from table_1 where Category= "Men";

#Query4: Write a query to find the cheapest women's shoe in a specific color (e.g., 'Black ').


Select min(Shoe_Price) from table_1 where Category= "women";


#query5: Write a query to retrieve all shoe names and their corresponding prices for men's shoes.
Select Shoe_Name, Shoe_Price from table_1 where Category= "Men";







#Table_2

show databases;
use capstonetable1;
select * from table_2;

#Query1:  Write a query that retrieves the count of sizes for all styles.

select Style_code, count(Count_Size) from table_2 group by Style_code;

#Query2: Write a query to list all styles with their associated colors.

Select Colour1, Colour2, Colour3, Colour4, Colour5, Style_code from table_2;


 #Query3: Write a to find styles that have more than one color.
SELECT style_code from table_2 where Colour2="NA";

#Query4: Write a query to find the count of sizes available for each color for a specific style code.


#Query5: Write a query to find styles that have a specific color(Black).
Select Style_code from table_2 where Colour1="Black" or Colour2= "Black" or Colour3= "Black" or Colour4= "Black" or Colour5= "Black";




#Table3



show databases;
use capstonetable1;
select * from table_3;


#Query1:Write a query calculates the average comfort rating for a specific product based on its reviews.
select avg(Star_Rate) as Comfort from table_3;



#Query2:   Write a query to retrieve products with high star ratings (e.g., 4 stars or above)
Select * from table_3 where Star_Rate>=4;

#Quer3: Write a query that counts the number of reviews for each product.
Select Review from table_3;

#Query4: Write a To retrieve products that have a quantified durability/quality/performance rating above a certain threshold (e.g., above 7).

#Query5:Write a query that  calculates the average comfort rating for each size.
select Size, AVG(Comfort) AS avg_Comfort FROM table_3 GROUP BY Size;

#7  Join SQL Queries  using all 3 tables:

#Query1:#Write a query finds the top-rated men's shoes along with their sizes from "Table1" and "Table3."
Show databases;
Use capstonetable1;

Select Table_1.Shoe_Name, Table_3.Size from Table_1 JOIN Table_3 on Table_1.Shoe_Name = Table_3.Star_Rate Where Table_1.Category="Men"
ORDER BY Table_3.Star_Rate DESC;


#Quer2::Write a  query calculates the average comfort rating for each category from "Table1" and "Table3."


SELECT table_3.Comfort, AVG(table_1.Category) AS avg_Comfort from table_1 JOIN table_3 ON table_1.Category=table_3.Comfort GROUP BY table_3.Comfort;
use capstonetable1;

#Query3::Write a  query identifies products with a durability/quality/performance rating higher than the average from "Table1" and "Table3."

SELECT table_1.Shoe_Name, table_3.Durability FROM table_1 JOIN table_3 ON table_1.Shoe_Name = table_3.Durability;
	
#Query4:Write a  subquery finds products with comfort ratings above the average comfort rating using "Table1" and "Table3."
SELECT table_1.Shoe_Name, table_3.Comfort FROM table_1 JOIN table_3 where Comfort="Very Comfortable";

#Query5:: Write a  query joins Table 1  and Table 2  using the "Style code/Product code" column, allowing you to retrieve shoe information along with product details.
SELECT table_1.Shoe_Name, table_2.Style_Code FROM table_1 JOIN table_2;

#Query6:  Write a  query that  identifies products with a star rating above the average star rating for their respective size.
SELECT table_1.Shoe_Name, table_3.Star_Rate, table_3.Size FROM table_1 JOIN table_3 where Star_Rate>=4;

#Query7: Write  a  query finds products with the highest comfort rating in each category
SELECT table_1.Shoe_Name, table_3.Comfort FROM table_1 JOIN table_3 where Comfort="Very Comfortable";