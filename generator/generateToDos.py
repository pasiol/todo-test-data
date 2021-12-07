import logging
import os
import time
import random
import requests
from faker import Faker

count = 3

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def main():
    fake = Faker(["fi_FI"])
    helth_check_url = f"http://{os.environ['API_URL']}/health"
    url = f"http://{os.environ['API_URL']}/todos"


    r = requests.get(helth_check_url, timeout=10)
    if r.status_code == 200:
        for n in range(count):
            new_todo = {"task": fake.paragraph(nb_sentences=1)}
            try:
                r = requests.post(url, json=new_todo, timeout=10)
                logger.info(f"response: {r.status_code} {r.content}")
            except Exception as error:
                logger.error(f"posting request failed: {error}")
            time.sleep(random.randint(1, 10))
    else:
        logger.info(f"service is down or request failed, statuscode: {r.status_code}")


if __name__ == "__main__":
    main()
