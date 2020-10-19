import math

def mean(data):
    size = len(data)
    total = 0
    for item in data:
        total += item
    mean = total / size
    return mean

def standardDeviation(data):
    n = len(data)
    m = mean(data)

    sigma_sum = 0
    for element in data:
        sigma_sum += (element - m)**2
    sd = math.sqrt(sigma_sum/(n-1))
    return sd

def correlation(x, y):
    nx = len(x)
    ny = len(y)
    mx = mean(x)
    my = mean(y)
    sx = standardDeviation(x)
    sy = standardDeviation(y)
    numerator = 0
    for xval,yval in zip(x,y):
        numerator += (xval - mx) * (yval - my)
    sig_x = 0
    sig_y = 0
    for xval,yval in zip(x,y):
        sig_x += (xval - mx)**2
        sig_y += (yval - my)**2
    denominator = math.sqrt(sig_x * sig_y)
    r = numerator / denominator
    return r

def residual(observerd, predicted):
    pass

def slope(x,y):
    """
    // this was the original formula I found that did not seem to work?
    // maybe there is bug somewhere in it but i found a simpler eq that seems to work
    n = len(x)
    sumof_x = 0
    for val in x:
        sumof_x += val
    sumof_y = 0
    for val in y:
        sumof_y += val
    sumof_xsquared = 0
    for val in x:
        sumof_xsquared += (val)**2
    sumof_xy = 0
    for xval, yval in zip(x,y):
        sumof_xy += (xval*yval)
    b = ((n * sumof_xy) - sumof_x * sumof_y)/(n * sumof_xsquared - sumof_xsquared)
    """

    r = correlation(x,y)
    sy = standardDeviation(y)
    sx = standardDeviation(x)

    b = r * (sy/sx)
    
    return b

def intercept(x,y):
    n = len(x)
    sumof_x = 0
    for val in x:
        sumof_x += val
    sumof_y = 0
    for val in y:
        sumof_y += val
    sumof_xsquared = 0
    for val in x:
        sumof_xsquared += (val)**2
    sumof_xy = 0
    for xval, yval in zip(x,y):
        sumof_xy += (xval*yval)
    a = ((sumof_y * sumof_xsquared)-(sumof_x * sumof_xy))/((n * sumof_xsquared) - (sumof_x)**2)
    return a

def linearRegression(x,y):
    xPoints= []
    yPoints = []

    b = slope(x,y)
    a= intercept(x,y)
    for xval in x:
        yval = a + (b * xval)
        xPoints.append(xval)
        yPoints.append(yval)
    return xPoints, yPoints