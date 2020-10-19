from stats import *
import pandas as pd
import matplotlib.pyplot as plt

def labelName(xVal):
    if xVal == 'population':
        return 'population'
    elif xVal == 'med_hh_income':
        return 'median household income'
    elif xVal == 'med_age':
        return 'median age'
    elif xVal == 'med_home_value':
        return 'median home value'

def main():

    file = input('enter name of data file: > ')

    df = pd.read_csv(f'data/{file}.csv') # create data frame from csv file
    print(df) # print data frame

    print('\nWhen choosing the explanatory variable below, make sure use the correct column name')
    print('Make sure to not choose COVID-19 column')
    explanatory_var = input('\nEnter an explanatory variable to model with COVID-19 cases: > ')

    x = df[explanatory_var]
    y = df["case_rate_per_100k"]

    # create scattor plot
    plt.scatter(x,y, s=5)
    # create x and y labels
    plt.xlabel(labelName(explanatory_var))
    plt.ylabel('COVID-19 cases per 100k')

    # get slope
    b = slope(x,y)
    # get intercept
    a = intercept(x,y)
    # get mean of x and y
    x_mean = mean(x)
    y_mean = mean(y)
    # get sample size
    sample_size = len(x)
    # get correlation
    r = correlation(x,y)
    # get standard deviation
    standard_dev_x = standardDeviation(x)
    standard_dev_y = standardDeviation(y)

    # create regression line
    regx, regy = linearRegression(x,y)
    plt.plot(regx,regy,color='red',linewidth=1.5)
    # console log
    print('\n')
    print('---------------------------')
    print(labelName(explanatory_var))
    print('---------------------------')
    print('mean: ',round(x_mean,3))
    print('standard deviation: ',round(standard_dev_x,3))
    print('\n')
    print('---------------------------')
    print('cases per 100k population')
    print('---------------------------')
    print('mean: ',round(y_mean,3))
    print('standard deviation: ',round(standard_dev_y, 3))
    print('\n')
    print('---------------------------')
    print('other stats')
    print('---------------------------')
    print('sample size: ',sample_size)
    print('correlation: ',round(r,3))
    print('slope: ',b,3)
    print('intercept',round(a,3))

    # show plot
    plt.show()

if __name__ == "__main__":
    main()
