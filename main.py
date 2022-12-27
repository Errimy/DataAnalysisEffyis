import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_excel(r'C:\Users\redat\Downloads\Data Analysis Problem DataSet.xlsx')

# Print the first few rows of the DataFrame
print(df.head())

# Convert the "date" column to a datetime datatype
df['date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Create a new column called "month" with the month values
df['month'] = df['date'].dt.month_name()

# Group the data by month and count the number of transactions in each month
monthly_volume = df.groupby(df['month']).size()

# Sort the data by the month index
# Define a list of months in the correct order
months = ['January', 'February', 'March', 'April', 'May', 'June']

# Reindex the data using the month list
monthly_volume = monthly_volume.reindex(months)

# Plot the monthly transaction volume using matplotlib
plt.plot(monthly_volume)
plt.xlabel('Month')
plt.ylabel('Transaction volume')
plt.title('Transaction volume per month')
plt.show()

# Calculate the total number of transactions
total_transactions = df.shape[0]

print('-----------------------------TOTAL TRANSACTIONS---------------------------')
# Print the result
print(f'Total transactions: {total_transactions}')


print('------------------------AVERAGE NUMBER OF TRANSACTIONS PER CLIENT--------------------------------')
# Assign a name to the transaction ID column
df.rename(columns={df.columns[0]: "transaction_id"}, inplace=True)
# Group the data by client ID and count the number of transactions for each client
transaction_count = df.groupby('ID_User')['transaction_id'].size()
# Count the number of transactions in the DataFrame
transaction_count = df['transaction_id'].count()

# Calculate the average number of transactions by dividing the number of transactions by the number of clients
avg_transactions = transaction_count / df['ID_User'].nunique()

print(avg_transactions)

# Group the data by transaction type and count the number of transactions for each type
transaction_count = df.groupby('Type')['transaction_id'].size()

# Plot the transaction count by type using matplotlib
plt.bar(transaction_count.index, transaction_count.values)
plt.xlabel('Transaction type')
plt.ylabel('Transaction count')
plt.title('Transaction count by type')
plt.show()

# Select the rows that have a value of "RTP" in the "Type" column and a value of 0 in the "Status" column
selected_rows = df[(df['Type'] == 'RTP') & (df['Status'] == 0)]

# Count the number of rows in the resulting DataFrame
count = selected_rows['transaction_id'].count()
print('------------------------RTP TRANSACTIONS NOT YET PROCESSED--------------------------------')

print('The number of RTP transactions arent processed yet :',count)

# Group the data by client ID and calculate the total amount spent by each client
total_spent = df.groupby('ID_User')['Amount'].sum()

# Calculate the average transaction value (ATV) for each client
atv = total_spent / df['ID_User'].value_counts()

# Calculate the number of transactions for each client
transaction_count = df.groupby('ID_User')['transaction_id'].size()

# Calculate the number of periods for each client
period_count = df.groupby('ID_User')['Date'].nunique()

# Calculate the average purchase frequency (APF) for each client
apf = transaction_count / period_count

# Calculate the average customer lifespan (ACL) for each client
acl = period_count / apf

# Calculate the CLV for each client
clv = atv * apf * acl

# Plot the CLV values using matplotlib
plt.bar(clv.index, clv.values)
plt.xlabel('Client ID')
plt.ylabel('CLV')
plt.title('Customer lifetime value (CLV) by client')
plt.show()

print('------------------------TOTAL REVENUE--------------------------------')
# Select the rows that have a value of "RTP" in the "Type" column and a value of 1 in the "Status" column
selected_rows = df[(df['Type'] == 'RTP') & (df['Status'] == 1)]

# Calculate the revenue for each selected row by multiplying the "Amount" column by 0.01
revenue = selected_rows['Amount'] * 0.01

# Sum the revenue values to get the total revenue
total_revenue = revenue.sum()

print(total_revenue)

print('------------------------BALANCE OF CLIENTS--------------------------------')

# Group the data by client ID and sum the "Volume" column for each group
volume_by_client = df.groupby('ID_User')['Volume'].sum()

# Select the rows that have a value of 1 in the "Status" column
selected_rows = df[df['Status'] == 1]

# Group the selected rows by client ID and sum the "Volume" column for each group
selected_volume_by_client = selected_rows.groupby('ID_User')['Volume'].sum()

# Add the sums to get the balance for each client
balance_by_client = volume_by_client + selected_volume_by_client
balance_by_client = balance_by_client/100
print(balance_by_client.head())

print('------------------------VOLUME PAR TYPE DE TRANSACTION--------------------------------')
# Select the rows that have a value of "Recharge" in the "Type" column
selected_rows_recharge = df[df['Type'] == 'Recharge']

# Sum the "Volume" column for the selected rows
volume_recharge = selected_rows_recharge['Volume'].sum()

print('Volume totale des Recharges:',volume_recharge)

# Select the rows that have a value of "RTP" in the "Type" column
selected_rows = df[df['Type'] == 'RTP']

# Sum the "Volume" column for the selected rows
volume_rtp = selected_rows['Volume'].sum()

print('Volume totale des RTPs:',volume_rtp)