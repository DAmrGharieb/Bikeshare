
import time




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('='*40)
    print('='*40)

    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    print('Most frequent month is ' + str(months[df.month.mode()[0]-1]))
    print('\n\n')

    # display the most common day of week
    print('Most frequent day is ' + str(df.day_of_week.mode()[0]))
    print('\n\n')


    # display the most common start hour
    print('Most frequent start hour is ' +str(df.month.mode()[0]))
    print('\n\n')


    print('='*40)
    print('='*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
    print('='*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('='*40)
    print('='*40)
    print('\n\n')

    start_time = time.time()

    # display most commonly used start station
    print('commonly used start station ' + str(df['Start Station'].mode()[0]))
    print('\n\n')


    # display most commonly used end station
    print('Commonly used end station ' + str(df['End Station'].mode()[0]))
    print('\n\n')


    # display most frequent combination of start station and end station trip


    print('='*40)
    print('='*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
    print('='*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time' )
    print(df['Trip Duration'].sum())
    print('\n\n')

    # display mean travel time
    print('average travel time')
    print(df['Trip Duration'].mean())
    print('\n\n')

    print('='*40)
    print('='*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
    print('='*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User types statistics' )
    print(df['User Type'].value_counts())
    print('\n\n')


    if(city != 'washington'):
        # Display counts of gender
        print('Gender statistics')
        print(df['Gender'].value_counts())
        print('\n\n')


        # Display earliest, most recent, and most common year of birth
        print('Earliest year of birth is ' + str(df['Birth Year'].min()))
        print('The most recent year of birth is ' + str(df['Birth Year'].max()))
        print('The most common year of birth is ' + str(df['Birth Year'].mode()[0]))
        print('\n\n')




    print('='*40)
    print('='*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)
    print('='*40)
