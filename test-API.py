#!/usr/bin/python
"""
"""
from API import *
import time
myodl = ODL(auth=HTTPBasicAuth('admin', 'admin'),
            domain='localhost', port='8080')
api = API(odl=myodl)
"""
test TopologyAPI
"""
api.retrieve_the_topology()
api.retrieve_userLinks()
link1 = {}
# api.add_userLink()

"""
test FlowProgrammerAPI
"""
api.retrieve_flows()

"""
test HostTrackerAPI
"""
api.retrieve_active_hosts()
api.retrieve_inactive_hosts()

"""
test StaticRouteAPI
"""
api.retrieve_all_static_routes()

"""
test StatisticsAPI
"""
api.retrieve_all_statistics_flow()
api.retrieve_all_statistics_port()
api.retrieve_all_statistics_table()

"""
test SubnetsAPI
"""
api.retrieve_all_subnets()

"""
test SwitchManagerAPI
"""
api.retrieve_all_nodes()
api.save_nodes_config()  # save failed ???

"""
test UserManagerAPI
HTTPS is not enabled, I think
"""

userConfig1 = {
    'user': 'testdpf',
    'password': 'testdpf',
    'roles': ['Network-Admin']
}

# api.add_user(userConfig1)
# time.sleep(3)
# api.del_user('testdpf')

"""
ContainerManager API
"""
api.retrieve_all_containers()
api.retrieve_container_config()  # can't get 'default'

"""
ConnectionManager API
"""
api.retrieve_all_nodes_of_controller('127.0.0.1')
