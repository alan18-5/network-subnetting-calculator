<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/CLI-Tool-000000?style=for-the-badge&logo=gnometerminal&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Subnetting-V4-00FF00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-00aa00?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/USERNAME/network-subnetting-calculator?style=social" />
</p>

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
