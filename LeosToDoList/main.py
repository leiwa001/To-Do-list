from .back_end import Back
from .front_end import Front
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="all_data.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    )


def main():
    logging.info("Gui wird gestartet...")
    back = Back()
    e = Front(back)
    
if __name__ == "__main__":
    main()
