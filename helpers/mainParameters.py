from helpers.cityData import CITY_DATA



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    #  HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see data for chicago , New York or Washington.\n').lower()
    while city not in CITY_DATA:
        city = input('\nWould you like to see data for chicago , New York or Washington.\n')

    #get user desire filteration option 
    filterOptions = ['day', 'month','both' ,'none']
    option = input('\nWould you like to filter data by month , day , both or not at all? type none for no time filter.\n').lower()
    
    while option not in filterOptions:
        option = input('\nWould you like to filter data by month , day , both or not at all? type none for no time filter.\n').lower()

    if(option == 'none'):
        month = 'all'
        day = 'all'
        return city, month, day , option

    if(option == 'both'):
        # get user input for month (all, january, february, ... , june)
        month = input('\nWhich month ? January, February, March, April, May, June ... type (all) if you want all months\n').lower()
        while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            month = input('\nWhich month ? January, February, March, April, May, June ... type (all) if you want all months\n').lower()

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('\nWhich day ? Sunday , Monday , Tuesday , Wedenesday , Thuresday , Friday ... type (all) if you want all days\n').lower()
        while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            day = input('\nWhich day ? Sunday , Monday , Tuesday , Wednesday , Thuresday , Friday, Saturday ... type all if you want all days\n').lower()

        print('-'*40)
        return city, month, day , option

    if(option == 'day'):

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('\nWhich day ? Sunday , Monday , Tuesday , Wedenesday , Thuresday , Friday , Saturday... type (all) if you want all days\n').lower()
        while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            day = input('\nWhich day ? Sunday , Monday , Tuesday , Wednesday , Thuresday , Friday, Saturday ... type all if you want all days\n').lower()

        month = 'all'

        print('-'*40)
        return city, month, day , option

    if(option == 'month'):

       # get user input for month (all, january, february, ... , june)
        month = input('\nWhich month ? January, February, March, April, May, June ... type (all) if you want all months\n').lower()
        while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            month = input('\nWhich month ? January, February, March, April, May, June ... type (all) if you want all months\n').lower()

        day = 'all'
        
        print('-'*40)
        return city, month, day , option