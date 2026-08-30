import time
import asyncio

async def fetch_data(param):
    print(f'Do something with {param}')
    await asyncio.sleep(param)
    print(f'Done with {param}')
    return f'Result for {param}'

async def main():
    task_1 = asyncio.create_task(fetch_data(5))
    task_2 = asyncio.create_task(fetch_data(2))
    result_1 = await task_1
    print('Completed task 1')
    result_2 = await task_2
    print('Completed task 2')
    return [result_1, result_2]

t1 = time.perf_counter()

results = asyncio.run(main())

t2 = time.perf_counter()

print(f'Time taken: {t2-t1:.2f} seconds')