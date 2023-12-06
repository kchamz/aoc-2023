import json
from datetime import datetime

with open("api_result.json") as file:
    content = json.loads(file.read())

members = content["members"]

reformatted = {}
for member, member_stats in members.items():
    stats = {}

    for day, info in member_stats["completion_day_level"].items():
        if info.get("1", None) and info.get("2", None):
            star_1_ts = datetime.utcfromtimestamp(info["1"]["get_star_ts"])
            star_2_ts = datetime.utcfromtimestamp(info["2"]["get_star_ts"])

            diff = star_2_ts - star_1_ts

            stats[day] = str(diff)
    if stats:
        reformatted[member_stats["name"]] = stats
    else:
        reformatted[member_stats["name"]] = member_stats


print(reformatted)
