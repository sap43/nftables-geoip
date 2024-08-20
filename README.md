nftables-geoip

Python code that sets up geoip based blocking for nftables. Code checks APNIC for list of ips mapped to countries, downloads this list, searches for ips mapped to India, places these ips into a whitelist that gets imported into nftables.

All files in the PF1 folder can be placed anywhere on your linux file system, the folder name is unimportant, however all files in the /etc folder need to be placed in the linux /etc folder.

Additional notes, relating to the nftables firewall:

1) Services are running at port 5500 in this codebase, nftables will only allow all traffic originating from or destined for ips in the whitelist, using port 5500.
2) The rules also contain an exception for whatsapp, all global ips used by the whatsapp service are placed within the wapp3.nft file and updated daily (code for whatsapp ip updates not included). Ports 443 and 80 are used by whatsapp for providing https and http traffic.
3) Port 5322 is used for ssh traffic, 53 for whatsapp dns resolution.
4) Ports 27017 and 27018 are used by the 2 voting members of a mongodb replica set hosted locally on the same system, to enable the use of multi-document/collection, atomic transactions in mongodb.
5) The rules rate limit all established connections, and use rate limiting to protect against syn, syn/ack, and ack flood attacks.
6) Only established and related connection types are permitted on the outgoing interface handling public connections.
7) New, established and related connections are all permitted on the incoming interface.
8) The default policy for the input and output chains is to drop all packets that dont explicitly match an accept rule.
9) All icmp packets are dropped, protecting against ping flood attacks.
10) Realtime blacklists are maintained that have a timeout of 5-10 minutes.
11) Any ips found to be violating rate limiting parameters get temporarily timed out.
12) Any ips generating more than 5 new connection requests a second get permanently banned, to protect against slowloris attacks.
13) Access to the internet is denied except for whatsapp.
14) Rules have been tested on a debian 11 machine.
15) Protection from layer 7 attacks is added by code hosted in another repo that analyzes logs at the application layer and then blacklists ips found to be generating junk requests at a rate beyond a specific maximum level.

If anyone has any thoughts on the roadmap for the firewall, please dm me. Maybe we can find a large enough, annotated database of traffic, train some ai algo on this, and then run it in realtime to build a more responsive rulebase? Anyone knows how well such a firewall may perform? Or other rules that could be added? Other attacks to protect against, or a means to speed this up?

Load testing, performance, stress testing, using nping (on a mac m1 system) upcoming.

Please reduce your LoginGraceTime value in your ssh config to protect from ssh based dos attacks.

A shell script has been provided (geoip.sh), that can be referenced using cron to update the country specific ip maps at a time of the user's choosing.

Is permanently WIP. Will keep updating with more rules.
