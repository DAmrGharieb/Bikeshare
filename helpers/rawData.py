
def getRawData(df):
    """Returns the raw data from the data frame. """
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    if(view_data.lower() == 'no'):
        return 

    if(view_data.lower() == 'yes'):    
        while view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: yes or no \n").lower()