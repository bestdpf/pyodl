#!/usr/bin/python
"""
"""
import sys
import pprint
from API import *
import time

myodl = ODL(auth=HTTPBasicAuth('admin', 'admin'),
            domain='localhost', port='8080',sec_port='8443')
api = API(odl=myodl,format='json')
"""
test TopologyAPI
"""
reponse=api.retrieve_the_topology()
topo=reponse.text
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(topo)

api.retrieve_userLinks()
#topologyUserLinkConfig
print('adding link named link1')
link1 = {
'status':'Success',
'name': 'link1',
'srcNodeConnector':'OF|2@OF|00:00:00:00:00:00:00:01',
'dstNodeConnector':'OF|2@OF|00:00:00:00:00:00:00:03'
}
api.add_userLink(topologyUserLinkConfig=link1)
time.sleep(1)
api.retrieve_userLinks()
time.sleep(1)
print('deleting link link1')
api.del_userLink(linkName='link1')

"""
test FlowProgrammerAPI
"""
api.retrieve_flows()
api.retrieve_node_flows(nodeId='00:00:00:00:00:00:00:01')
api.retrieve_flow_by_name(nodeId='00:00:00:00:00:00:00:01',flowName='NORMAL')
flow1={
'installInHw' : 'true',
'name' : 'flow1',
'node' : {
'id':'00:00:00:00:00:00:00:01',
'type':'OF'
},
'ingressPort':'1',
'priority' : '5',
'etherType' : '0x800',
'actions':[
'DROP'
]
}
print('add a flow')
api.add_or_modify_flow(flowConfig=flow1)
time.sleep(1)
api.retrieve_node_flows(nodeId='00:00:00:00:00:00:00:01')
print('toggle a flow')
api.toggle_flow_by_name(nodeId='00:00:00:00:00:00:00:01',flowName='flow1',nodeType='OF')
time.sleep(1)
print('del a flow')
api.del_flow_by_name(nodeId='00:00:00:00:00:00:00:01',flowName='flow1',nodeType='OF')
api.retrieve_node_flows(nodeId='00:00:00:00:00:00:00:01')

"""
test HostTrackerAPI
"""
print('HostTrackerAPI')
api.retrieve_active_hosts()
api.retrieve_inactive_hosts()
api.retrieve_host_by_address(networkAddress='10.0.0.1')
#hostConfig
host1={
'dataLayerAddress' : '00:00:00:00:00:00:10:01',
'nodeType' : 'OF' ,
'nodeId' : '00:00:00:00:00:00:00:01',
'nodeConnectorId' : '39',
'vlan' : '1',
'staticHost' : 'true',
'networkAddress' : '10.0.1.1'
}
#I may add a nodeConnector to a switch, and then to add a host1
"""
print('add a host')
api.add_host(hostConfig=host1)
time.sleep(15)
print('del a host')
api.del_host(networkAddress='10.0.1.1')
sys.exit()
"""

"""
test StaticRouteAPI
"""
api.retrieve_all_static_routes()
route1={
'name': 'route1',
'prefix' : '10.0.1.0/24',
'nextHop' : '10.0.0.1'
}
api.retrieve_static_route_by_name(route='test-route1')
print('add route1')
api.add_static_route(staticRoute=route1)
time.sleep(1)
api.del_static_route(route='route1')

"""
test StatisticsAPI
"""
api.retrieve_all_statistics_flow()
api.retrieve_all_statistics_port()
api.retrieve_all_statistics_table()

"""
test SubnetsAPI Not Tested Now!!!
"""
api.retrieve_all_subnets()

"""
test SwitchManagerAPI
"""
api.retrieve_all_nodes()
api.save_nodes_config()  # save failed ???
api.retrieve_node_connectors_by_node(nodeId='00:00:00:00:00:00:00:01')
api.add_node_property(nodeId='00:00:00:00:00:00:00:01',
propertyName='description', propertyValue='switch1')
time.sleep(1)
api.del_node_property(nodeId='00:00:00:00:00:00:00:01',propertyName='testp')


"""
test UserManagerAPI
"""
"""
userConfig1 = {
    'user': 'testdpf',
    'password': 'testdpf',
    'roles': ['Network-Admin']
}
print('add_user')
api.add_user(userConfig1)
time.sleep(1)
print('del_user')
api.del_user('testdpf')
"""

"""
ContainerManager API
"""
api.retrieve_all_containers()
api.retrieve_container_config()  # can't get 'default'

"""
ConnectionManager API
"""
api.retrieve_all_nodes_of_controller('127.0.0.1')
