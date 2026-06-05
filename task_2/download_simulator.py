import asyncio
import time

async def download(url: str, delay: float) -> dict:
    print(f"Старт: {url}")
    await asyncio.sleep(delay)
    if "error" in url:
        raise ValueError(f"Ошибка на {url}")
    size = len(url) * 1024
    print(f"Готово: {url}")
    return {"url": url, "delay": delay, "size": size}

async def run_with_error_raise(urls):
    print("Запуск без return_exceptions")
    tasks = [asyncio.create_task(download(url, delay), name=url) for url, delay in urls]
    try:
        results = await asyncio.gather(*tasks, return_exceptions=False)
        for r in results:
            print(r)
    except Exception as e:
        print(f"Поймали ошибку: {e}")
        for t in tasks:
            if not t.done():
                t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

async def run_with_error_return(urls):
    print("\nЗапуск с return_exceptions")
    tasks = [asyncio.create_task(download(url, delay), name=url) for url, delay in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            print(f"Результат-ошибка {r}")
        else:
            print(f"Результат-успех {r}")

async def main():
    urls = [
        ("https://example.com/file1", 1.0),
        ("https://example.com/file2", 1.5),
        ("https://example.com/error_file", 0.8),
        ("https://example.com/file4", 0.5)
    ]
    await run_with_error_raise(urls)
    await run_with_error_return(urls)

if __name__ == "__main__":
    asyncio.run(main())
