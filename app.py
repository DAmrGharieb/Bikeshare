from helpers.mainParameters import get_filters
from helpers.filters import load_data
from helpers.statistics import time_stats, station_stats, trip_duration_stats, user_stats
from helpers.rawData import getRawData

def main():
     while True:
        city, month, day, option = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        print('*==*'*40)
        print('*==*'*40)

        station_stats(df)
        print('*==*'*40)
        print('*==*'*40)

        trip_duration_stats(df)
        print('*==*'*40)
        print('*==*'*40)

        user_stats(df,city)

        print('*==*'*40)
        print('*==*'*40)

        getRawData(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
