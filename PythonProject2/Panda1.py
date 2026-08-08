import pandas as pd

customer_data = {
    'SignupDate': [
        '2026-01-15',
        '2026-02-01',
        '2026-02-10',
        '2026-03-05',
        '2026-03-12',
        '2026-04-01',
    ],
    'Email': [
        'user1@gmail.com',
        'user2@yahoo.com',
        'user3@gmail.com',
        'user4@outlook.com',
        'user5@gmail.com',
        'user6@yahoo.com',
    ],
    'Status': [' Active ', 'INACTIVE', ' active ', 'Active', ' inactive ', 'ACTIVE'],
    'TotalSpent': ['$1,200.50', '$450.00', '$890.25', '$2,100.00', '$50.75', '$620.00'],
}

# Must match the length of the lists in customer_data (6 items)
row_labels = ['C-01', 'C-02', 'C-03', 'C-04', 'C-05', 'C-06']

df_customers = pd.DataFrame(customer_data, index=row_labels)
print(df_customers)