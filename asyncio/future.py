from asyncio import Future
import asyncio
from faker import Faker
import json
from time_decorator import async_timed as timer

fake = Faker("uk-UA")


async def get_user_asyncfrom_db(uuid: int, future: Future):
    await asyncio.sleep(0.5)
    future.set_result(
        {
            "id": uuid,
            "name": fake.name(),
            "company": fake.company(),
            "e-mail": fake.email(),
        }
    )


def make_request(uuid: int):
    future = Future()
    asyncio.create_task(get_user_asyncfrom_db(uuid, future))
    return future


@timer()
async def main():
    u1_future = make_request(1)
    u2_future = make_request(2)
    u3_future = make_request(3)
    print(u1_future, u2_future, u3_future)

    result = await asyncio.gather(u1_future, u2_future, u3_future)
    return result


if __name__ == "__main__":
    users = []
    results = asyncio.run(main())
    for res in results:
        users.append(res)
        with open(
            "data.json",
            "w",
            encoding="utf-8",
        ) as fd:
            json.dump(users, fd, indent=4, ensure_ascii=False)
        print(res)
