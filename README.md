# Business Sales Performance Analytics

This is my project for Task 1 of the Future Interns Data Science & Analytics internship. I took a retail sales dataset, cleaned it using Python, analysed it, and then made a dashboard in Tableau to understand how the business is performing.

## What I wanted to find out

- How sales and profit change over the years
- Which products sell the most
- Which categories and regions do well
- Which sub-categories are making losses
- What happens to profit when the discount is high
- What the business can improve

## Dataset

I used the Superstore Sales dataset. It contains orders, customers, locations, products, categories, sales, quantity, discount and profit. After cleaning, I had 9,993 rows and 21 columns. One row had no Row ID, so I removed it.

Tools used: Python, Pandas, VS Code, Tableau, CSV and GitHub.

## Cleaning the data

I loaded the CSV file in Python using latin1 encoding, because the default one gave errors. After that I did these things:

- Removed the row with the missing Row ID
- Changed Order Date and Ship Date to date format
- Changed Row ID to integer
- Checked for duplicate rows
- Checked the Sales, Quantity, Discount and Profit columns for strange values
- Checked Category, Sub-Category, Region, Segment and Ship Mode
- Saved the cleaned data as Sample_Superstore_Cleaned.csv

I did not remove the negative profit values, because they are real losses and they help to find the weak areas of the business.

## Overall results

- Total Sales: $2,296,468.92
- Total Profit: $286,177.44
- Total Orders: 5,009
- Total Quantity: 37,870
- Profit Margin: 12.46%

The profit margin is Total Profit divided by Total Sales, multiplied by 100.

## Analysis

### Sales and profit by year

- 2014: sales $484,247.50, profit $49,543.97
- 2015: sales $470,532.51, profit $61,618.60
- 2016: sales $609,205.60, profit $81,795.17
- 2017: sales $733,215.26, profit $93,439.27

Sales dropped a little in 2015 and then kept growing after that. 2017 was the best year for both sales and profit. Looking at the months, November had the highest sales at about $352.46K and February had the lowest at about $59.75K.

### Top product

The top selling product was the Canon imageCLASS 2200 Advanced Copier with $61,599.82 in sales. I made a Top 10 products chart in Tableau to compare the products easily.

### Categories

- Technology: sales $836,154.03, profit $145,454.95
- Furniture: sales $741,999.80, profit $18,451.27
- Office Supplies: sales $719,047.03, profit $122,490.80

Technology is the best category for both sales and profit. Furniture was the surprising one for me. Its sales are high, but its profit margin is only about 2.49%, while Technology has 17.40% and Office Supplies has 17.04%.

### Regions

- West: sales $725,457.82, profit $108,418.45
- East: sales $678,781.24, profit $91,522.78
- Central: sales $501,239.89, profit $39,706.36
- South: sales $391,721.90, profit $46,749.43

The West region has the highest sales and profit.

### Sub-categories with losses

Three sub-categories had a negative total profit. Tables lost $17,725.48, Bookcases lost $3,472.56 and Supplies lost $1,189.10. Tables had the biggest loss by a wide margin.

### Discounts

In this dataset, higher discount levels mostly go together with lower profit, and some of the higher discount levels even have negative total profit. This only shows a pattern. It does not prove that discounts caused the losses, and for that more analysis would be needed.

## Main insights

1. The business made about $2.30M in sales and $286.18K in profit, which is a 12.46% margin.
2. 2017 was the best year.
3. Sales change a lot by month. November is the highest and February is the lowest.
4. Technology is the strongest category.
5. The West region performs best.
6. Tables, Bookcases and Supplies lose money overall.
7. Higher discounts are linked with lower profit.
8. High sales do not always mean high profit, and Furniture is a good example of this.

## Recommendations

- Check the transactions with high discounts and see if they are reducing the profit too much.
- Look at the pricing, discounts and costs of Furniture to find out why its margin is so low.
- Study Tables, Bookcases and Supplies at product level to see which products are causing the losses.
- Plan stock and promotions for the busy months, mainly September to December.
- Track the profit of top selling products and not only their sales.
- Judge performance using sales, profit and margin together instead of only sales.

## Tableau dashboard

The dashboard shows Total Sales, Total Profit, Total Orders, Total Quantity and Profit Margin at the top. Below that it has the sales trend over time, sales and profit by category, sales and profit by region, the Top 10 products and profit by sub-category. I also made a separate sheet in the workbook for discount levels and profit.

## Files in this project

- Business_Sales_Performance_Analytics.py : Python code for cleaning and analysis
- Sample_Superstore_Cleaned.csv : cleaned dataset
- Business_Sales_Performance_Dashboard.png : image of the final dashboard
- Business_Sales_Performance_Analytics.twbx : Tableau packaged workbook
- Insights_and_Recommendations.txt : insights and recommendations
- README.md : project documentation

## Project flow

I started with the raw sales data, cleaned it in Python, analysed the cleaned data, made the charts in Tableau, put them together in a dashboard, and then wrote the insights and recommendations.
