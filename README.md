# 🕶️ Network Subnetting Calculator 


**Subnet like a pro.** CLI tool to compute IPv4 subnets fast — crafted for networking practice, interviews, and flexing on GitHub.


> Terminal-friendly. ASCII banner. Lightweight Python. MIT Licensed.


## Features


- Parse network or host IP + prefix (e.g. `192.168.10.0/24`)
- Calculate subnets by **number of subnets** or **hosts required per subnet**
- Outputs: network address, broadcast, first host, last host, usable hosts, prefix
- CLI with easy flags and example usage
- Tests included (pytest)


## Quick usage


```bash
# Clone
git clone <repo>
cd network-subnetting-calculator


# Run
python -m src.subnet_calc 192.168.10.0/24 --subnets 4


# Or by hosts
python -m src.subnet_calc 10.0.0.0/8 --hosts 500
