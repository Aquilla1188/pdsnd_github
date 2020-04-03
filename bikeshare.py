import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = { 'january': 1,
          'february': 2,
          'march': 3, 
          'april': 4,
          'may': 5,
          'june': 6  }

days = { 'sunday': 0,
         'monday': 1,
          'tuesday': 2,
          'wednesday': 3, 
          'thursday': 4,
          'friday': 5,
          'saturday': 6  }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter City Name: ")
        if city in CITY_DATA :
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month =  input("Enter Month Name or 'all' to Preview all : ".lower())
        if month in months or month=='all':
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day =  input("Enter Day of the Week Name or 'all' to Preview all : ".lower())
        if day in days or day=='all' :
            break


    print('-'*40)
    return city , month, day

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] =pd.to_datetime(df['Start Time'] )
    df['End Time'] =pd.to_datetime(df['End Time'] )
    df['trip_duration']=  df['End Time']-df['Start Time']
    
    df['hour'] = df['Start Time'].dt.hour
    df['Day']=df['Start Time'].dt.weekday
    df['Month']=df['Start Time'].dt.month
    print(city+ month+ day)
    if month!='all':
        df=df[df['Month']==months[month]]
    if day!='all':
        df=df[df['Day']==days[day]]
     


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    for key, value in months.items():    
        if value == df['Month'].mode()[0]:
            print('Most Frequent Month:',key.title())

    # TO DO: display the most common day of week
    for key, value in days.items():    
        if value == df['Day'].mode()[0]:
            print('Most Frequent Day:',key.title())

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Frequent Start Station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Frequent End Station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    df['most']=df['Start Station']+df['End Station']
    df[df['most']==df['most'].mode()[0]]
    print('Most Frequent  combination of start station and end station trip: Start :{} & End : {}'.format( df.iloc[0, 4],df.iloc[0, 5]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Tavel Time is :' ,df['trip_duration'].sum())


    # TO DO: display mean travel time
    print('Average Tavel Time is :' ,df['trip_duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Users Count')

    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('Genders Count\n{}'.format(df['Gender'].value_counts())) 
    except:
        print("sorry , there is no gender data")

  
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('earliest Birth year for a user is :{}\nthe most recent Birth year for a user is :{}\nthe most common year of birth is :{}'.format(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode())) 

    except:
        print("sorry , there is no Birth year data")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    #the main thread 
    while True:
    # loading data
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # asking user if he want to see the raw data
        i = 0
        raw = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns',200)
        
        while True:            
            if raw == 'no':
                break
            print(df.iloc[i:i+5,:9])
            raw = input('\nWould you like to see next rows of raw data?\n').lower()
            i += 5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
