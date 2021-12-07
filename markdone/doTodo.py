import logging
import os
import time
import random
import requests
from pprint import pprint

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def main():

    url = f"http://{os.environ['API_URL']}/todos"
    r = requests.get(url, timeout=10)
    try:
        todos = r.json()
        count_of_todos = len(todos)
        if count_of_todos > 0:
            random_todo = random.randint(0, count_of_todos-1)
            url = f"{url}/{random_todo-1}"
            try:
                r = requests.put(url, timeout=10)
                if r.status_code == 200:
                    logger.info(f"successfully marked {todos[random_todo-1]} done")
            except Exception as error:
                logger(f"put request failed {url}, error: {error}")
        else:
            logger.info("no todos to do")
    except Exception as error:
        logger.error(f"get request failed {url}, error: {error}")


if __name__ == "__main__":
    main()
