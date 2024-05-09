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

ri = nautobot.plugins.bgp.routing_instances.create(**payload)

print(ri)
