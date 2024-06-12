from pynautobot import api


url = "https://demo.nautobot.com"
token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

nautobot = api(url=url, token=token)

payload = {
    "device": {"name": "ams01-dist-01"},
    "autonomous_system": {"asn": "65535"},
    "status": "Active",
    "router_id": {"address": "104.94.130.210/29"}
}


payload = {
    "prefix": "9.9.9.9/10",
    "status": "Active",
    "role": "pop",
    "cf_date_added": "1/1/2024, 0:00",  # this seems to be not working
}

ri = nautobot.ipam.prefixes.create(**payload)
print(ri.custom_fields["date_added"])  # still None
from pprint import pprint
pprint(dict(ri))

# Let's try to add it on the object level
ri.custom_fields["date_added"] = payload["cf_date_added"]
# and save the object
ri.save()

# Refresh the object with .get()
ri = nautobot.ipam.prefixes.get(prefix="9.9.9.9/10", depth=1)
print(ri.custom_fields["date_added"])  # Now the value is present.
pprint(dict(ri))

ri.delete()
