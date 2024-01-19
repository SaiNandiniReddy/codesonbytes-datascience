#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests

# Define the API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts"

# Make a request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()

    # Create a Pandas DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Specify the columns you want to include in the CSV file
    columns_to_include = ["userId", "id", "title", "body"]

    # Save the DataFrame to a CSV file
    df[columns_to_include].to_csv("dataset.csv", index=False)

    print("CSV file created successfully.")
else:
    print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")


# In[ ]:




