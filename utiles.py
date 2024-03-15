import random
from colorama import Fore, Style
from datetime import datetime, timedelta
from data import ubicaciones
 
def random_number_ranges(minimo, maximo):
    return random.randint(minimo, maximo)


def random_number_decimal_ranges(minimo, maximo, precision):
    return round(random.uniform(minimo, maximo), precision)


def generate_location():
    return ubicaciones[random_number_ranges(0,len(ubicaciones)-1)]


def generate_random_date(start_date, end_date):
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime('%Y-%m-%dT%H:%M:%SZ')


def generate_random_date_MARCO(start_date, end_date, start_time, end_time):
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    random_time = timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))
    random_datetime = random_date + random_time
    return random_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')


def print_styled(text, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{text}{Style.RESET_ALL}")
