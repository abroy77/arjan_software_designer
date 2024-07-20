import random
import string
from datetime import datetime
""" 
Original code


def generate_id(length: int) -> str:
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def weekday() -> str:
    today = datetime.today()
    return f"{today:%A}"


def main() -> None:
    print(f"Today is a {weekday()}")
    print(f"Your id = {generate_id(10)}")


if __name__ == "__main__":
    main()
"""

def generate_id(length: int, input_seed: int | None = None) -> str:
    if not input_seed:
       input_seed = random.randint(0,200)
    
    random.seed(input_seed)
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def weekday(time: datetime) -> str:
    return f"{time:%A}"

def main() -> None:
  print(f"Today is a {weekday(datetime.now())}")
  print(f"Your id = {generate_id(10)}")

if __name__ == "__main__":
  main()