from .quant.moving_average_crossover import mac1

import asyncio

loop = asyncio.get_event_loop()

loop.run_until_complete(mac1())