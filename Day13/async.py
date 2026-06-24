import asyncio

async def api_call():
    print("API Started")
    await asyncio.sleep(5)
    print("API Completed")

async def db_call():
    print("DB Started")
    await asyncio.sleep(2)
    print("DB Completed")


async def main():
    await asyncio.gather(api_call(),db_call())
asyncio.run(main())