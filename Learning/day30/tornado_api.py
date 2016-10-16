#!/usr/bin/env python

import json
import docker
import requests

basejson = ['{\
    "Name":"container-testing-3",\
    "Hostname": "container-testing-1",\
    "Domainname": "",\
    "User": "",\
    "AttachStdin": true,\
    "AttachStdout": true,\
    "AttachStderr": true,\
    "Tty": true,\
    "OpenStdin": true,\
    "StdinOnce": false,\
    "Env": null,\
    "Cmd": ["/bin/bash"],\
    "Entrypoint": null,\
    "Image": "registry.docker.meicai.cn/allinone-14.04:1.0.2",\
    "Labels": {},\
    "Mounts": [],\
    "WorkingDir": "",\
    "NetworkDisabled": false,\
    "MacAddress": "",\
    "ExposedPorts": {},\
    "StopSignal": "SIGTERM",\
    "HostConfig": {\
        "Binds": null,\
        "Links": null,\
        "LxcConf": {},\
        "Memory": 858993459,\
        "MemorySwap": 0,\
        "MemoryReservation": 0,\
        "KernelMemory": 0,\
        "CpuShares": 1024,\
        "CpuPeriod": 100000,\
        "CpuQuota": 800000,\
        "CpusetCpus": "",\
        "CpusetMems": "",\
        "BlkioWeight": 300,\
        "MemorySwappiness": 0,\
        "OomKillDisable": false,\
        "PortBindings": {},\
        "PublishAllPorts": false,\
        "Privileged": false,\
        "ReadonlyRootfs": false,\
        "Dns": ["114.114.114.114"],\
        "DnsOptions": [""],\
        "DnsSearch": [""],\
        "ExtraHosts": null,\
        "VolumesFrom": null,\
        "CapAdd": ["NET_ADMIN"],\
        "CapDrop": ["MKNOD"],\
        "RestartPolicy": { "Name": "", "MaximumRetryCount": 0 },\
        "NetworkMode": "bridge",\
        "Devices": [],\
        "Ulimits": [],\
        "LogConfig": { "Type": "json-file", "Config": {} },\
        "CgroupParent": "",\
        "VolumeDriver": ""\
    }\
}']

conf = json.loads(basejson[0])

client_ins = docker.Client(base_url='tcp://' + '127.0.0.1' + ":" + '2375', version='1.20', timeout=10)
print ("      Create the container......")
container_ret = client_ins.create_container(image=conf['Image'],
                            stdin_open=conf['OpenStdin'],
                            tty=conf['Tty'],
                            command=conf['Cmd'],
                            name=conf['Name'],
                            hostname=conf['Hostname'],
                            host_config=conf['HostConfig'])
client_ins.start(container_ret['Id'])
