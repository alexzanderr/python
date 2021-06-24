
import asyncio as asinc

async def iterate(content):
    for _ in range(10):
        print(content, end=" ")
        await asinc.sleep(0.001)

async def count(symbol):
    await iterate(symbol)

async def main_function():
    await asinc.gather(count("A"), count("B"), count("C"))

async def second_main():
    await count("A")
    await count("B")
    await count("C")

# asinc.run(main_function())
asinc.run(second_main())