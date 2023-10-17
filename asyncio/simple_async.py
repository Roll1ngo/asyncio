import asyncio


async def second():
    await asyncio.sleep(3)

    return "I am second and sleep 3 sec"


async def baz() -> str:
    print("Before sleep")
    cor_sleep = second()
    result_second = await cor_sleep
    print(result_second)
    print("After sleep")
    return "Hello World"


async def main():
    cor = baz()
    print(cor)
    result = await cor
    return result


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)
