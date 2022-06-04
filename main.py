from lev.whtcjdtc2008.nmap import nmap

async def test_alive(ip:list, disable_arp:bool, ignore_rst:bool):
    res = await nmap.alive(ip, disable_arp, ignore_rst)
    data = await res.get()
    print(data)

async def test_typical(ip:str):
    res = await nmap.typical(ip)
    data = await res.get()

async def test_port_os(ip:str):
    res = await nmap.port_os(ip)
    data = await res.get()

async def test_raw():
    res = await nmap.raw(["-sL", "192.168.1-3.1-3"])
    data = await res.get()
    print(data)

if __name__ == "__main__":
    import levrt
    import logging

    # pdb.set_trace()
    logging.basicConfig()
    logger = logging.getLogger("lev")
    logger.setLevel(logging.DEBUG)

    # levrt.run(test_typical("lev.zone"))
    # levrt.run(test_port_os("lev.zone"))
    levrt.run(test_alive(["lev.zone", "mituan.zone"], True, False))
    # levrt.run(test_raw())
