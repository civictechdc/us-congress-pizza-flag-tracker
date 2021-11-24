import pandas as pd
import json

# Run this script to update the office_codes.json with updated congressional offices.

def add_fed_offices_to_list(offices_list): 
    fed_offices = {"usa_state": "FED", "office_code": ["HOSS","AOC","MAIL"]}
    offices_list.insert(0,fed_offices)

def df_to_list(df):
    cols = df.columns
    df_list = []
    for row in df.itertuples(): 
        df_list.append({cols[0]:row[1],cols[1]:row[2]})
    return df_list

def create_offices_df():
    '''
    Creates a pandas df with 
    columns: usa_state, office_code
    row (EG): "CA", ["CA-01","CA-02",...]
    '''

    # Public updated list of congressional offices.
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
    offices['office_code'] = offices['state_code'] + '-' + offices['district'] 
    # Rename state columns
    offices.rename(columns= {'state_code':'usa_state'},inplace=True)
    offices.drop(columns=['district'],inplace=True) 
    # group by states
    offices_gp = pd.DataFrame(offices.groupby('usa_state')['office_code'].apply(list).reset_index()) 
    return offices_gp

if __name__ == '__main__':
    offices_df = create_offices_df()
    offices_list = df_to_list(offices_df)
    add_fed_offices_to_list(offices_list)
    #offices_json = json.dumps(offices_list)
    with open('../office_codes.json', 'w') as file:
        json.dump(offices_list,file)