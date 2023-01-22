# import packages
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    while True:
       city = input('Which city would you like to explore? Enter: chicago, new york city, or washington?').lower()
       if (city in['chicago', 'new york city', 'washington']):
          break
       else:
          print('Please enter city: chicago, new york city, or washington')

    # get user input for month (all, january, february, ... , june)
    while True:
       month = input('Which month would you like to explore? Enter: january, february, march, april, may, june or all?:').lower()
       if (month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
          break
       else: 
          print('Please Enter a valid month: january, february, march, april, may, june or all.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day = input('Which day of the weekday would you like to explore? Enter: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?').lower()
       if (day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']):
            break
       else:
            print('Please enter a valid weekday: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all')

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
    df = pd.read_csv(CITY_DATA[city])

   # adding month and weekday column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_common_month = df['month_name'].mode()[0]
    print("The most common month is: " + str(month_common_month).title())  

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + str(most_common_day)) 

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ' + str(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("The most common start station is: " + most_common_start_station)

    # display most commonly used end station
    most_common_end_station = str(df['End Station'].mode()[0])
    print("The most common start end station is: " + most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start-End-Combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    most_common_start_end_combination = str(df['Start-End-Combination'].mode()[0])
    print("The most common start-end combination of stations is: " + most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types is:") 
    print(user_types)

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("Gender distribution:")
        print(gender_counts)
    except:
        print("No data for gender available in the filtered data")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth_Year'].min()
        print("The earliest birth year is:" + earliest_birth_year)
        most_recent_birth_year = df['Birth_Year'].max()
        print("The most recent birth year is: " + most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("The most common birth year is: " + most_common_birth_year)
    except:
        print("No data of birth year available in the filtered data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays 5 rows of raw data on request."""
    raw_data = 0
    while True:
        choice = input("Do you want to see the raw data? Yes or No: ").lower()
        if choice not in ['yes', 'no']:
            choice = input("Please type Yes or No: ").lower()
        elif choice == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            more = input("Do you want to see more rows? Yes or No?").lower()
            if more == 'no':
                break
        elif choice == 'no':
            return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
