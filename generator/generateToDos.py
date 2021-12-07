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

    not_ready = True
    while not_ready:
        r = requests.get(helth_check_url)
        if r.status_code == 200:
            not_ready = False
            logger.info("api seems to be ready")

    for n in range(count):
        new_todo = {"task": f"{n}: {fake.paragraph(nb_sentences=1)}"}
        try:
            r = requests.post(url, json=new_todo)
            logger.info(f"response: {r.status_code} {r.content}")
        except Exception as error:
            logger.error(f"posting request failed: {error}")
        time.sleep(random.randint(1, 10))


if __name__ == "__main__":
    main()
