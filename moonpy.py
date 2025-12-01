from datetime import date 
def get_phase():
    todays_date = date.today().toordinal()
    def_full_moon = date(2020,1,24).toordinal()
    phase = (todays_date - def_full_moon)%29
    return phase
today = get_phase()
print(type(today))   
print(today)   
