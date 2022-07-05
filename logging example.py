import logging
from pathlib import Path
import datetime
def log_inform():
    dir_data = Path("log")
    dir_data.mkdir(parents=True, exist_ok=True)
log_filename = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
print(log_filename)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d-%Y %H:%M:%S',
                    filename=f'log/{log_filename}.log',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
logger1 = logging.getLogger("example")
a = 15 
b = 20
logger1.info(f"the value of a is {a} and the value of b is {b}")
res = a + b
logger1.info(f"the result is {res}")
if __name__ == "__log_inform__":
    log_inform()

