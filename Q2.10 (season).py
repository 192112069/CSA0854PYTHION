month=input("input the month:")

day=int(input("input the day:"))

if month in ('january','february','march'):

    season='spring'
    
elif month in ('april','may','june'):

    season ='summer'

elif month in ('july','august','september'):

    season='autumn'

else:
    season='winter'

if (month=='march') and (day>19):

    season='spring'

elif (month=='june') and (day>20):

    season='summer'

elif (month=='september') and (day>21):

    season='autumn'

elif (month== 'december') and (day>28):

    season = 'winter'

print("season is",season)
                                      

        
