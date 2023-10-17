from time import time
import asyncio
from faker import Faker


fake = Faker("uk-UA")


# async def get_user_asyncfrom_db(uuid: int):
#     await asyncio.sleep(0.5)
#     return {
#         "id": uuid,
#         "name": fake.name(),
#         "company": fake.company(),
#         "e-mail": fake.email(),
#     }


async def send_metrics(url):
    print(f"Send to {url}:{time()}")

    # async def main():
    #     u1_task = asyncio.create_task(get_user_asyncfrom_db(1))
    #     u2_task = asyncio.create_task(get_user_asyncfrom_db(2))
    #     u3_task = asyncio.create_task(get_user_asyncfrom_db(3))
    #     print(u1_task, u2_task, u3_task)


async def worker():
    while True:
        await asyncio.sleep(1)
        await send_metrics("http://any_url.com")

    # result = await asyncio.gather(u1_task, u2_task, u3_task)
    # return result


if __name__ == "__main__":
    # users = []
    # start = time()
    # results = asyncio.run(main())
    # for res in results:
    #     users.append(res)
    #     with open(
    #         "data.json",
    #         "w",
    #         encoding="utf-8",
    #     ) as fd:
    #         json.dump(users, fd, indent=4, ensure_ascii=False)
    #     print(res)
    # print(time() - start)
    asyncio.run(worker())
