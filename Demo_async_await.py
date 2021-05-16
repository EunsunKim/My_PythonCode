import asyncio
import time


async def sleepTest():
	print(f'Time: {time.time() - startTime:.2f}')
	await asyncio.sleep(1)


async def sumTest(key, values):
	total = 0
	for value in values:
		# print(f'Job {key} : {total}+{value}') #for debug
		await sleepTest()
		total += value
	print('----------')
	print(f'Job {key} Sum : {total}\n----------')


startTime = time.time()

loop = asyncio.get_event_loop()
jobs = [loop.create_task(sumTest("A", [12, 20])), loop.create_task(sumTest("B", [5, 3, 60]))] # previous version(before3.7) - asyncio.ensure_future()
loop.run_until_complete(asyncio.wait(jobs))
loop.close()

endTime = time.time()
print(f'Total Compute Time : {endTime - startTime:.2f} sec')
