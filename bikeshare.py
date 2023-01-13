import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n\n')



    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('choose a city name (chicago, new york city, washington):\n').lower()
    while city not in CITY_DATA:
        city = input('the entered city is not valid\nchoose a city name (chicago, new york city, washington):\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = [ 'january', 'february','march','april','may','june','all']
    while True:
        month = input('\nnow choose one of these months ( january, february, march ,april , june), or (all) if you don\'t want to filter by months:\n').lower()
        if month not in months :
             print('\nthats not one of the listed months!')
        else:
           break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
        day = input('\nnow choose a day( Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday), or (all) if you don\'t want to filter by days :\n').lower()
        if day not in days :
             print('\nthats not a valid day!')
        else:
           break



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #load data from CSV files
    df = pd.read_csv(CITY_DATA[city])

    #convert to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    #extract months, weekdays, hours
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour




    #filtering by month
    if month != 'all':
        months = [ 'january', 'february','march','april', 'may','june' ]
        month = months.index(month) + 1
        df = df[df['month'] == month]

   #filtering by day
    if day !='all':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is:', df['month'].mode()[0])


    # TO DO: display the most common day of week
    print('the most common day of the week is:', df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    print('the most common start hour is:', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station is:', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('the most commonly used end station is:', df['End Station'].mode()[0])



    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station']+","+df['End Station']
    print('the most frequent combination of start station and end station trip is:', df['trip'].mode()[0])




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time : ',(df['Trip Duration'].sum()).round())


    # TO DO: display mean travel time
    print('total travel time : ',(df['Trip Duration'].mean()).round())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print(df['User Type'].value_counts().to_frame())


    # TO DO: Display counts of gender
    # washington file doe not have a column for gender and birth year
    if city != 'washington':
        print('\n')
        print(df['Gender'].value_counts().to_frame())


    # TO DO: Display earliest, most recent, and most common year of birth
        print('\nthe most common year of birth is:', int(df['Birth Year'].mode()[0]))
        print('the most recent year of birth is:', int(df['Birth Year'].max()))
        print('the earliest year of birth is:', int(df['Birth Year'].min()))
    else:
        print('there is no gender and birth year data for this city')





    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    print('\nRaw data is available to check\n')
    index=0
    user_input = input('would you like to display 6 rows or raw data?, YES or NO\n').lower()
    if user_input not in ['yes','no']:
        print('that\'s invalid choice, please type yes or no')
        user_input = input('would you like to display 6 rows or raw data?, YES or NO\n').lower()
    elif user_input != 'yes':
        print('thank you')
    else:
        while index+6 < df.shape[0]:
            print(df.iloc[index:index+6])
            index += 5
            user_input = input('would you like to display another 6 rows or a raw data?\n').lower()
            if user_input !='yes':
                print('thank you')
                break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? YES or NO.\n')
        if restart.lower() != 'yes':
            print("thank you")
            break




if __name__ == "__main__":
	main()
