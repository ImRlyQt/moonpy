#!/usr/bin/env python
from moon_phase import moon_phase
from ascii_moon import ASCII_MOON 
from date_argument import custom_date

def main(): 
    date = custom_date()
    phase = moon_phase(date)
    ascii_art = ASCII_MOON.get(phase)
    print(ascii_art,"\n")

if __name__ == "__main__":
    main()
