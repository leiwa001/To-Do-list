from .back_end import Back
from .front_end import Front
import logging

logging.basicConfig(level=logging.INFO)



def main():
    logging.info("Gui wird gestartet...")
    back = Back()
    e = Front(back)
    
if __name__ == "__main__":
    main()
