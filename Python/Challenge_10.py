

charlotte_count = 0

for crash in all_crashes:
    if crash["COUNTY_TXT"] == "CHARLOTTE":
        charlotte_count += 1

print(f"Charlotte County crashes: {charlotte_count}")

