from time import time
import asyncio
from faker import Faker
from concurrent.futures import ProcessPoolExecutor


fake = Faker("uk-UA")
url = "www.some_url.com"


# async def get_user_asyncfrom_db(uuid: int):
#     await asyncio.sleep(0.5)
#     return {
#         "id": uuid,
#         "name": fake.name(),
#         "company": fake.company(),
#         "e-mail": fake.email(),
#     }
def cpu_bound_task(num):
    counter = num
    while num>0:
        num-=1
    print(f"Completed cpu_bound_task with{counter}")
    return f"Completed cpu_bound_task with{counter}"


async def send_metrics(url):
    while True:
        await asyncio.sleep(1)
        print(f"Send to {url}:{time()}")

async def worker():
    loop  = asyncio.get_running_loop()
    sd = loop.create_task(send_metrics(url))


    with ProcessPoolExecutor(4) as pool:
        futures = [loop.run_in_executor(pool, cpu_bound_task,num) for num in [60_000_000, 70_000_000, 80_000_000]]
        result = await asyncio.gather(*futures)
        sd.cancel()
        return result


    # async def main():
    #     u1_task = asyncio.create_task(get_user_asyncfrom_db(1))
    #     u2_task = asyncio.create_task(get_user_asyncfrom_db(2))
    #     u3_task = asyncio.create_task(get_user_asyncfrom_db(3))
    #     print(u1_task, u2_task, u3_task)



    
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
    r=asyncio.run(worker())
    print(r)
