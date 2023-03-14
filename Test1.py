import requests
import json
import pandas as pd
import cx_Oracle

# Define the API endpoint URL
#url = "https://api.github.com/users/hadley/orgs"

# Make a GET request to the API endpoint
response = requests.get("https://api.covid19api.com/summary").text
#data = response.json()
response_info = json.loads(response)
print(type(response_info))
country_list = []
for country_info in response_info['Countries']:
    country_list.append([country_info['Country'], country_info['TotalConfirmed'], country_info['TotalRecovered']])
#print(country_list)

country_df = pd.DataFrame(data=country_list, columns=['Country', 'Total_Confirmed','TotalRecovered'])
print(country_df.head(10))

cx_Oracle.init_oracle_client(lib_dir="/Users/shekaragrawal/Downloads/instantclient_19_8")

dsn = cx_Oracle.makedsn("10.232.13.74", 1521, service_name="ofsdevdb_pdb1.ofsaanpdb.ofsaanpvcn.oraclevcn.com")

con = cx_Oracle.connect(user="Atomic", password="ECO_nomical_12",
                               dsn=dsn,
                               encoding="UTF-8")
cur = con.cursor()

sql = """insert into a_xx (col2,col3,col4)
          values (:col1,:col2,:col3)"""

for country_info in response_info['Countries']:
    cur.execute(sql, [country_info['Country'],country_info['TotalConfirmed'],country_info['TotalRecovered']])
con.commit()



# Check the status code of the response to ensure the request was successful
#if response.status_code == 200:
    # Get the JSON data from the response
#    data = response.json()
#    response_info = json.loads(data)
    # Do something with the data
#    print(response_info)
   # json_string = json.loads(data)
   # type(json_string)
    #print(json_string['login'])

#else:
    # Handle the error
 #   print("Request failed with status code", response.status_code)