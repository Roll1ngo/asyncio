import asyncio
import concurrent


def io_bound():
    with open(__file__, "r") as fd:
        return fd.read(15)


def cpu_bound(power: int, p: int):
    r = [i**power for i in range(10**p)]
    return sum(r)


async def main():
    loop = asyncio.get_running_loop()

    file = loop.run_in_executor(None, io_bound)
    print(file)
    r = await file
    print(r)

    result = loop.run_in_executor(None, cpu_bound, 2, 6)
    print(result)
    r1 = await result
    print(r1)


if __name__ == "__main__":
    asyncio.run(main())
