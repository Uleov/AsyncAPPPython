import asyncio

async def producer(queue: asyncio.Queue, num_messages: int, num_consumers: int):
    for i in range(1, num_messages + 1):
        message = f"Сообщение {i}"
        print(f"Отправил {message}")
        await queue.put(message)
    
    for _ in range(num_consumers):
        await queue.put(None)

async def consumer(name: str, queue: asyncio.Queue, processed_count: dict):
    processed_count[name] = 0
    while True:
        message = await queue.get()
        if message is None:
            queue.task_done()
            break
        print(f"{name} получил {message}")
        await asyncio.sleep(0.1)
        processed_count[name] += 1
        queue.task_done()

async def main():
    num_messages = 15
    num_consumers = 3
    queue = asyncio.Queue(maxsize=5)
    processed_count = {}

    consumers = [
        asyncio.create_task(consumer(f"Воркер {i}", queue, processed_count))
        for i in range(1, num_consumers + 1)
    ]
    
    producer_task = asyncio.create_task(producer(queue, num_messages, num_consumers))
    
    await queue.join()
    await producer_task
    for c in consumers:
        await c

    print("\nИтог:")
    for name, count in processed_count.items():
        print(f"{name}: {count} шт")

if __name__ == "__main__":
    asyncio.run(main())
