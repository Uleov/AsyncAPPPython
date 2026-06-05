import asyncio
import time
import argparse

async def run_timer(name: str, delay: float):
    print(f"Старт {name} ({delay} сек)")
    await asyncio.sleep(delay)
    print(f"Финиш {name}")

async def sequential_mode(tasks):
    print("Последовательно:")
    start = time.perf_counter()
    for name, delay in tasks:
        await run_timer(name, delay)
    print(f"Время: {time.perf_counter() - start:.2f} сек\n")

async def concurrent_mode(tasks):
    print("Конкурентно:")
    start = time.perf_counter()
    await asyncio.gather(*(run_timer(name, delay) for name, delay in tasks))
    print(f"Время: {time.perf_counter() - start:.2f} сек\n")

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="both")
    args = parser.parse_args()

    tasks = [
        ("Таймер 1", 1.5),
        ("Таймер 2", 2.0),
        ("Таймер 3", 1.0)
    ]

    if args.mode == "sequential":
        await sequential_mode(tasks)
    elif args.mode == "concurrent":
        await concurrent_mode(tasks)
    else:
        await sequential_mode(tasks)
        await concurrent_mode(tasks)

if __name__ == "__main__":
    asyncio.run(main())
