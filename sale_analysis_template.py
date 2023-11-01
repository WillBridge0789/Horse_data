"""
    Please write a script to read in the sale results csv file, remove all rows where out is true ('t')
    Using pandas plot method to create the following 4 png files
    - Total sales for the top 10 sires by total sale price
    - Avg sale price for the top 10 buyers by total sale price
    - Avg sale price by book and by sex
    - Avg sale price by month of birth
"""
# Need to install pandas library 
import pandas as pd
import plotly.express as px

# Need to install plotly library 
pd.options.plotting.backend = "plotly"

# File path
# file_path = #Path to the supplied CSV file "keesep_2023_results.csv"
file_path = "keesep_2023_results.csv"


# Your code here
# 1. Read in the csv file to pandas dataframe
df = pd.read_csv(file_path)

# 2. Remove outs from the data
df = df[df['out'] != 't']
# print(df)

# 3. Total sale for the top 10 sires by gross sale price
top_10_sires = df.groupby('sire_name').sum().sort_values(by='sale_price', ascending=False).head(10)
fig1 = top_10_sires['sale_price'].plot.bar(title='Total Sales for the Top 10 Sires by Total Sale Price')
print(top_10_sires)
fig1.show()


# 4. Avg sale price for top 10 buyers by gross sale price
top_10_buyers = df.groupby(['buyer'])['sale_price'].mean().sort_values(ascending=False).head(10)
# Creates a new DataFrame with the buyer names and average sale prices
top_10_buyers_df = pd.DataFrame({
    'buyer': top_10_buyers.index, # Show buyers column by index
    'average_sale_price': top_10_buyers.values # Use values of series for average sale prices
})
# Displays data in line chart
fig4 = px.line(top_10_buyers_df, x='buyer', y='average_sale_price', title='Avg Sale Price for the Top 10 Buyers by Gross Sale Price')
fig4.show()

# 5. Avg sale price by book by sex
pivot_table = df.groupby(['book', 'sex'])['sale_price'].mean().unstack()

fig5 = px.bar(pivot_table, title='Avg Sale Price by Book and Sex')
fig5.show()

# 6. Avg sale price by month of birth
avg_price_by_dob = df.groupby('dob')['sale_price'].mean().reset_index()

fig6 = px.bar(avg_price_by_dob, x='dob', y='sale_price', title='Avg Sale Price by Date of Birth', labels={'dob': 'Date of Birth'})
fig6.show()
