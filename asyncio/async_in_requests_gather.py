from time import sleep, time
import asyncio
from faker import Faker
import json

fake = Faker("uk-UA")


def get_user_from_db(uuid: int):
    sleep(0.5)
    return {
        "id": uuid,
        "name": fake.name(),
        "company": fake.company(),
        "e-mail": fake.email(),
    }


async def get_user_asyncfrom_db(uuid: int):
    await asyncio.sleep(0.5)
    return {
        "id": uuid,
        "name": fake.name(),
        "company": fake.company(),
        "e-mail": fake.email(),
    }


async def main():
    result = await asyncio.gather(
        get_user_asyncfrom_db(1),
        get_user_asyncfrom_db(2),
        get_user_asyncfrom_db(3),
    )
    return result


if __name__ == "__main__":
    start = time()
    users = []
    for uuid in range(3):
        users.append(get_user_from_db(uuid))
        with open(
            "data.json",
            "w",
            encoding="utf-8",
        ) as fd:
            json.dump(users, fd, indent=4, ensure_ascii=False)
    print(users)
    print(time() - start)
    print("-------------------------------------------------------------------------")
    start = time()
    results = asyncio.run(main())
    for res in results:
        print(res)
    print(time() - start)
