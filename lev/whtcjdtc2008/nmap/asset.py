from levrt import ctx, annot, Concurrent
from . import nmap

@annot.meta(
    desc = "检测局域网中存活的主机，并且获取主机端口信息",
    params = [annot.Param("ip", "进行安全检查的ip段", holder="192.168.1.1/24"),
              annot.Param("con_num", "并发扫描端口的任务数", holder="1")],
)
async def gatherNetworkInfo(ip:str, con_num:int):
    """
    检测局域网中存活主机并且获取主机端口信息
    ```
    await gatherNetworkInfo("192.168.1.1/24", 1)
    ```
    """

    # scan the whole network to find machines alive
    result = await nmap.alive(ip)
    data = await result.get()

    alive_ip = data['alive']

    os_res = []
    task_list = []

    # scan the port info
    async with Concurrent(limit=con_num) as c:
        for domain in alive_ip:
            print(domain)
            t = c.start(nmap.port_os(domain))
            task_list.append(t)

    # get the result
    for t in task_list:
        t_res = await t
        async for doc in t_res.all():
            os_res.append(doc)

    print(os_res)
