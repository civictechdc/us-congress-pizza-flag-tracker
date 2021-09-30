import pandas as pd
import json

def df_to_list(df):
    cols = df.columns
    df_list = []
    for row in df.itertuples(): 
        df_list.append({cols[0]:row[1],cols[1]:row[2]})
    return df_list

def create_offices_df():
    '''Creates a JSON file containing list of records for each congressional office.
    Each record includes 1. state_code 2. office_number 3. office_name.
    EG: {"state_code":"MA","office_number":"06","office_name":"MA-06"}'''

    url_csv = 'https://raw.githubusercontent.com/CivilServiceUSA/us-house/master/us-house/data/us-house.csv'
    # Get dataframe listing congressional offices
    offices = pd.read_csv(url_csv,header=0)
    # Save only states and district numbers. Fill empty values (At large    offices)
    offices = offices[['state_code','district']].fillna(1)
    # Convert floats to integers
    offices['district'] = offices['district'].astype(int) 
    # Convert ints to strings in proper format
    offices['district'] = offices['district'].apply(lambda x: f"{x:02}")
    # Create new column from two previous columns.
    offices['home_office_code'] = offices['state_code'] + '-' + offices['district'] 
    # Rename state columns
    offices.rename(columns= {'state_code':'usa_state'},inplace=True)
    offices.drop(columns=['district'],inplace=True) 
    # group by states
    offices_gp = pd.DataFrame(offices.groupby('usa_state')['home_office_code'].apply(list).reset_index()) 
    return offices_gp

if __name__ == '__main__':
    offices_df = create_offices_df()
    offices_list = df_to_list(offices_df)
    offices_json = json.dumps(offices_list)
    with open('home_office_codes.json','w') as file:
        json.dump(offices_list,file)