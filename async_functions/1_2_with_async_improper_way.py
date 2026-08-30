import time
import asyncio

async def fetch_data(param):
    print(f'Do something with {param}')
    await asyncio.sleep(param)
    print(f'Done with {param}')
    return f'Result for {param}'

async def main():
    task1 = fetch_data(1)
    task2 = fetch_data(2)
    result1 = await task1
    print('Task 1 completed successfully')
    result2 = await task2
    print('Task 2 completed successfully')
    return [result1, result2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()

print(f"Time taken: {t2-t1:.2f} seconds")