# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to UserBot by @MoveAngel

from datetime import datetime
from covid import Covid
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^\.covid (.*)")
async def corona(event):
    await event.edit("Sedang Di Proses hehe")
    country = event.pattern_match.group(1)
    covid = Covid()
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text =  f"`Confirmed   : {country_data['confirmed']}`\n"
        output_text += f"`Active      : {country_data['active']}`\n"
        output_text += f"`Deaths      : {country_data['deaths']}`\n"
        output_text += f"`Recovered   : {country_data['recovered']}`\n"
        output_text += (
            "`Last update : "
            f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%Y-%m-%d %H:%M:%S')}`\n"
        )
        output_text += f"Data provided by [Johns Hopkins University](https://j.mp/2xf6oxF)\nCopyright © Daeng Server Bot"
    else:
        output_text = "Tidak Ditemukan Informasi Di Negara Ini!"
    await event.edit(f"Corona Virus Info in {country}:\n\n{output_text}")


CMD_HELP.update({
        "covid": 
        ".covid <country>"
        "\nUsage: Get an information about data covid-19 in your country.\n"
    })