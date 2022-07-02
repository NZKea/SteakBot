import asyncio
import aiohttp
from discord.ext import tasks, commands

from blockchainCalls import VEJOE, wei_to_ether
from main import switch_status


async def async_request_txt(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response: 
            return await response.text()


class StatusData:
    def __init__(self):
        self.price = ""
        self.veJoeAmount = ""

    async def update_price(self):
        try:
            newPrice = wei_to_ether(await async_request_txt("https://api.traderjoexyz.com/priceusd/0xb279f8DD152B99Ec1D84A489D32c35bC0C7F5674"))
            self.price = "$" + str(round(newPrice, 3))
        except TypeError:
            self.price = "Error"

    def update_veJoe(self):
        try:
            newVeJoe = wei_to_ether(VEJOE.call("balanceOf", "0x1aB6B2f60A7e8DA9d521cF8f90b2a5b5d314b3A6"))
            newVeJoe = "{:,}".format(newVeJoe)
            self.veJoeAmount = newVeJoe.split(".")[0]
        except TypeError:
            self.price = "Error"


class statusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.botData = StatusData()

    @tasks.loop()
    async def cycle(self):
        await self.botData.update_price()
        self.botData.update_veJoe()
        status_messages = ["Steak @ " + self.botData.price, self.botData.veJoeAmount + " veJoe"]
        for message in status_messages:
            await switch_status(message)
            await asyncio.sleep(15)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Starting Cog Cycle")
        self.cycle.start()


def setup(bot):
    bot.add_cog(statusCog(bot))