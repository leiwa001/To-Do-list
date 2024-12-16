from .back_end import Back
from .front_end import Front

def main():
    print("GUI wird gestartet")
    back = Back()
    e = Front(back)
    
if __name__ == "__main__":
    main()
