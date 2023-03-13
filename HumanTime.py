import time

def Time(seconds_time,mode):
    """This is a program which contructs a string given a time in seconds
    Selecting mode m displays a time in seconds and minutes
    Selecting mode m displays a time in seconds, minutes and hours
    Selecting mode m displays a time in seconds, minutes, hours, and days
    Plurality and singularity is perserved by this code for minutes, hours, and days but not seconds
    It expects a float as an input which has a non integer remainder when divided by 60 yeilding a float for seconds"""
    if mode=='m':
        if seconds_time//60!=1:
            m='mins'
        else:
            m='min'
        return '{} {} {} seconds'.format(int(seconds_time//60),m,seconds_time%60)
    if mode=='h':
        if seconds_time//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%3600//60!=1:
            m='mins'
        else:
            m='min'
        return '{} {} {} {} {} seconds'.format(int(seconds_time//3600),h,int(seconds_time%3600//60),m,seconds_time%3600%60)
    if mode=='d':
        if seconds_time//86400!=1:
            d='days'
        else:
            d='day'
        if seconds_time%86400//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%86400%3600//60!=1:
            m='mins'
        else:
            m='min'
        return '{} {} {} {} {} {} {} seconds'.format(int(seconds_time//86400),d,int(seconds_time%86400//3600),h,int(seconds_time%86400%3600//60),m,seconds_time%86400%3600%60)
    if mode=='w':
        if seconds_time//604800!=1:
            w='weeks'
        else:
            w='week'
        if seconds_time%604800//86400!=1:
            d='days'
        else:
            d='day'
        if seconds_time%604800%86400//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%604800%86400%3600//60!=1:
            m='mins'
        else:
            m='min'
        return '{} {} {} {} {} {} {} {} {} seconds'.format(int(seconds_time//604800),w,int(seconds_time%604800//86400),d,int(seconds_time%604800%86400//3600),h,int(seconds_time%604800%86400%3600//60),m,seconds_time%604800%86400%3600%60)
    if mode=='y':
        if seconds_time//31536000!=1:
            y='years'
        else:
            y='year'
        if seconds_time%31536000//604800!=1:
            w='weeks'
        else:
            w='week'
        if seconds_time%31536000%604800//86400!=1:
            d='days'
        else:
            d='day'
        if seconds_time%31536000%604800%86400//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%31536000%604800%86400%3600//60!=1:
            m='mins'
        else:
            m='min'
        return '{} {} {} {} {} {} {} {} {} {} {} seconds'.format(int(seconds_time//31536000),y,int(seconds_time%31536000//604800),w,int(seconds_time%31536000%604800//86400),d,int(seconds_time%31536000%604800%86400//3600),h,int(seconds_time%31536000%604800%86400%3600//60),m,seconds_time%31536000%604800%86400%3600%60)
def TimeShort(seconds_time,mode,decimals):
    while decimals<0:
        try:
            decimals=eval(input('decimals must be non_negative\nPlease enter a positive integer:\n'))
        except:
            pass
    """This is a program which contructs a string given a time in seconds
    The user has the ability to specify how many digits are displayed for the seconds
    Selecting mode 'm' displays a time in seconds and minutes
    Selecting mode 'h' displays a time in seconds, minutes and hours
    Selecting mode 'd' displays a time in seconds, minutes, hours, and days
    Selecting mode 'w' displays a time in seconds, minutes, hours, days, and weeks
    Selecting mode 'y' displays a time in seconds, minutes, hours, days, weeks, and years
    Specify how many digits you want using the paramater decimals
    If decimals==0 then seconds will be converted to an int
    Plurality and singularity is perserved by this code for minutes, hours, and days but not seconds"""
    de=decimals//1
    if mode=='m':
        if seconds_time//60!=1:
            m='mins'
        else:
            m='min'
        if de!=0:
            B='{} {} {:.'+str(de)+'f} seconds'
            return B.format(int(seconds_time//60),m,seconds_time%60)
        else:
            if int(seconds_time%60)!=1:
                return '{} {} {} seconds'.format(int(seconds_time//60),m,int(seconds_time%60))
            else:
                return '{} {} {} second'.format(int(seconds_time//60),m,int(seconds_time%60))
    if mode=='h':
        if seconds_time//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%3600//60!=1:
            m='mins'
        else:
            m='min'
        if de!=0:
            B='{} {} {} {} {:.'+str(de)+'f} seconds'
            return B.format(int(seconds_time//3600),h,int(seconds_time%3600//60),m,seconds_time%3600%60)
        else:
            if int(seconds_time%3600%60)!=1:
                return '{} {} {} {} {} seconds'.format(int(seconds_time//3600),h,int(seconds_time%3600//60),m,int(seconds_time%3600%60))
            else:
                return '{} {} {} {} {} second'.format(int(seconds_time//3600),h,int(seconds_time%3600//60),m,int(seconds_time%3600%60))
    if mode=='d':
        if seconds_time//86400!=1:
            d='days'
        else:
            d='day'
        if seconds_time%86400//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%86400%3600//60!=1:
            m='mins'
        else:
            m='min'
        if de!=0:
            B='{} {} {} {} {} {} {:.'+str(de)+'f} seconds'
            return B.format(int(seconds_time//86400),d,int(seconds_time%86400//3600),h,int(seconds_time%86400%3600//60),m,seconds_time%86400%3600%60)
        else:
            if int(seconds_time%86400%3600%60)!=1:
                return '{} {} {} {} {} {} {} seconds'.format(int(seconds_time//86400),d,int(seconds_time%86400//3600),h,int(seconds_time%86400%3600//60),m,int(seconds_time%86400%3600%60))
            else:
                return '{} {} {} {} {} {} {} second'.format(int(seconds_time//86400),d,int(seconds_time%86400//3600),h,int(seconds_time%86400%3600//60),m,int(seconds_time%86400%3600%60))
    if mode=='w':
        if seconds_time//604800!=1:
            w='weeks'
        else:
            w='week'
        if seconds_time%604800//86400!=1:
            d='days'
        else:
            d='day'
        if seconds_time%604800%86400//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%604800%86400%3600//60!=1:
            m='mins'
        else:
            m='min'
        if de!=0:
            B='{} {} {} {} {} {} {} {} {:.'+str(de)+'f} seconds'
            return B.format(int(seconds_time//604800),w,int(seconds_time%604800//86400),d,int(seconds_time%604800%86400//3600),h,int(seconds_time%604800%86400%3600//60),m,seconds_time%604800%86400%3600%60)
        else:
            if int(seconds_time%604800%86400%3600%60)!=1:
                return '{} {} {} {} {} {} {} {} {} seconds'.format(int(seconds_time//604800),w,int(seconds_time%604800//86400),d,int(seconds_time%604800%86400//3600),h,int(seconds_time%604800%86400%3600//60),m,int(seconds_time%604800%86400%3600%60))
            else:
                return '{} {} {} {} {} {} {} {} {} second'.format(int(seconds_time//604800),w,int(seconds_time%604800//86400),d,int(seconds_time%604800%86400//3600),h,int(seconds_time%604800%86400%3600//60),m,int(seconds_time%604800%86400%3600%60))
    if mode=='y':
        if seconds_time//31536000!=1:
            y='years'
        else:
            y='year'
        if seconds_time%31536000//604800!=1:
            w='weeks'
        else:
            w='week'
        if seconds_time%31536000%604800//86400!=1:
            d='days'
        else:
            d='day'
        if seconds_time%31536000%604800%86400//3600!=1:
            h='hours'
        else:
            h='hour'
        if seconds_time%31536000%604800%86400%3600//60!=1:
            m='mins'
        else:
            m='min'
        if de!=0:
            B='{} {} {} {} {} {} {} {} {} {} {:.'+str(de)+'f} seconds'
            return B.format(int(seconds_time//31536000),y,int(seconds_time%31536000//604800),w,int(seconds_time%31536000%604800//86400),d,int(seconds_time%31536000%604800%86400//3600),h,int(seconds_time%31536000%604800%86400%3600//60),m,seconds_time%31536000%604800%86400%3600%60)
        else:
            if int(seconds_time%31536000%604800%86400%3600%60)!=1:
                return '{} {} {} {} {} {} {} {} {} {} {} seconds'.format(int(seconds_time//31536000),y,int(seconds_time%31536000//604800),w,int(seconds_time%31536000%604800//86400),d,int(seconds_time%31536000%604800%86400//3600),h,int(seconds_time%31536000%604800%86400%3600//60),m,int(seconds_time%31536000%604800%86400%3600%60))
            else:
                return '{} {} {} {} {} {} {} {} {} {} {} second'.format(int(seconds_time//31536000),y,int(seconds_time%31536000//604800),w,int(seconds_time%31536000%604800//86400),d,int(seconds_time%31536000%604800%86400//3600),h,int(seconds_time%31536000%604800%86400%3600//60),m,int(seconds_time%31536000%604800%86400%3600%60))
def TimeAuto(time):
    """This function allows the user to simply pass one paramater, time (in seconds)
    Tt clevarly calls on Time in a way which uses only the units of time necessary based on the duration of time"""
    if time<60:
        return('{} seconds'.format(time))
    elif time<60*60:
        return(Time(time,'m'))
    elif time<60*60*24:
        return(Time(time,'h'))
    elif time<60*60*24*7:
        return(Time(time,'d'))
    elif time<60*60*24*365:
        return(Time(time,'w'))
    else:
        return(Time(time,'y'))
def TimeAutoShort(time,decimals):
    """Similarly to TimeAuto, this function allows the user to pass two paramaters
    Time (in seconds) and decimals
    The user can use the second paramater to indicate how many digits are wanted in seconds
    Tt clevarly calls on TimeShort in a way which uses only the units of time necessary based on the duration of time"""
    if time<60:
        while decimals<0:
            try:
                decimals=eval(input('decimals must be non_negative\nPlease enter a positive integer:\n'))
            except:
                pass
        d=decimals//1
        B='{:.'+str(d)+'f} seconds'
        return(B.format(time))
    elif time<60*60:
        return(TimeShort(time,'m',decimals))
    elif time<60*60*24:
        return(TimeShort(time,'h',decimals))
    elif time<60*60*24*7:
        return(TimeShort(time,'d',decimals))
    elif time<60*60*24*365:
        return(TimeShort(time,'w',decimals))
    else:
        return(TimeShort(time,'y',decimals))

def StopWatch(endTime = 0, wait = .5):
    iTime = time.time()
    if endTime == 0:
        while True:
            StopWatchHelper(iTime, wait)
    else:
        while time.time() < iTime + endTime:
            StopWatchHelper(iTime, wait)
        StopWatchHelper(iTime, wait)

def StopWatchHelper(iTime, wait):
    print(TimeAuto(time.time() - iTime))
    time.sleep(wait)

def Timer(amount, wait = .5):
    iTime = time.time()
    while time.time() < iTime + amount:
        TimerHelper(amount, iTime, wait)

def TimerShort(amount, precision = 2, wait = .5):
    iTime = time.time()
    while time.time() < iTime + amount:
        TimerHelperShort(amount, iTime, wait, precision)

def TimerHelper(amount, iTime, wait):
    print(TimeAuto(amount + iTime - time.time()))
    time.sleep(wait)

def TimerHelperShort(amount, iTime, wait, precision):
    print(TimeAutoShort(amount + iTime - time.time(), precision))
    time.sleep(wait)

def Dab(a, b, c):
    "Takes three paramaters preperation time, warm up time, and cool down time all in seconds as an int/float"
    t = Timer
    print("Get Ready");t(a);print("Heat Up");t(b);print("Cool Down");t(c);print("Dab Time!!!")
    
