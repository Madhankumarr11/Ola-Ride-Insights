import pandas as pd

ola = pd.read_excel('D:/SRMK/Guvi/Ola-Ride-Insights/OLA_DataSet.xlsx')

# # 🔹 1. Sample OLA DataFrame (or replace this with your actual data)
# ola = pd.DataFrame({'Ride_DateTime' : ['2024-07-26 14:00:00', '2024-07-25 22:20:00']})

# # 🔹 2. Convert string to datetime format

# ola['Ride_DateTime'] = pd.to_datetime(ola['Ride_DateTime'])

# # 🔹 3. Create new column for Date
# ola['Ride_Date'] =ola['Ride_DateTime'].dt.date

# # 🔹 4. Create new column for Time
# ola['Ride_Time'] = ola['Ride_DateTime'].dt.time

# # 🔹 5. Retrieve all successful bookings
# Successful_Bookings = ola[ola['Booking_Status'] == 'Completed']

# 🔹 6 Total number of cancelled rides by customers 

cancelled_by_customer = ola[
    (ola['Booking_Status'] == 'Cancelled') &
    (ola['Cancel Reason'] == 'Canceled by Customer')
]

# Count how many such rides
# print("Total cancelled by customers:", cancel_by_customer.shape[0])


# # 🔹 6. Average ride distance for each vehicle type
# Avg_Distance = ola.groupby('Vehicle_Type')['Ride_Distance'].mean()







