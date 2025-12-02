from moon_phase import moon_phase
from ascii_moon import ASCII_MOON 

def main():
    phase = moon_phase()
    ascii_art = ASCII_MOON.get(phase)
    print(ascii_art,"\n")

if __name__ == "__main__":
    main()
