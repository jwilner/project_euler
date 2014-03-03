from datetime import datetime


def first_sundays(start_year, end_year):
    years = range(start_year, end_year + 1)
    months = range(1, 13)
    firsts_of_months = (datetime(year, month, 1)
                        for year in years for month in months)

    return sum(1 for date in firsts_of_months if date.isoweekday() == 7)

if __name__ == '__main__':
    print first_sundays(1901, 2000)
