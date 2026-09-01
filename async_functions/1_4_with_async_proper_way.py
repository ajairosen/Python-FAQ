import asyncio
import time

def create_task(t):
    print(f"Started task {t}")
    time.sleep(t)
    print(f'Finished task {t}')
    return f'Result for {t}'

async def main():
    task1 = asyncio.to_thread(create_task, 1)
    task2 = asyncio.to_thread(create_task, 2)
    result = await asyncio.gather(task1, task2)
    return result

if __name__ == "__main__":
    t1 = time.perf_counter()
    result = asyncio.run(main())
    t2 = time.perf_counter()
    print(f"Time taken: {t2-t1:.2f} Seconds")
    print(result)