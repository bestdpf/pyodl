"""
"""
from ODL import *
from TopologyAPI import *
from FlowProgrammerAPI import *
from HostTrackerAPI import *
from StaticRouteAPI import *
from StatisticsAPI import *
from SubnetsAPI import *
from SwitchManagerAPI import *
from UserManagerAPI import *
from ContainerManagerAPI import *
from ConnectionManagerAPI import *
from BridgeDomainAPI import *
import requests


class API(object):

    def __init__(self, odl, container='default', format='json'):
        self.odl = odl
        self.container = container
        self.format = format
        self.topology = TopologyAPI(format=self.format)
        self.flowprogrammer = FlowProgrammerAPI(format=self.format)
        self.hosttracker = HostTrackerAPI(format=self.format)
        self.staticroute = StaticRouteAPI(format=self.format)
        self.statistics = StatisticsAPI(format=self.format)
        self.subnets = SubnetsAPI(format=self.format)
        self.switchmanager = SwitchManagerAPI(format=self.format)
        self.usermanager = UserManagerAPI(format=self.format)
        self.containermanager = ContainerManagerAPI(format=self.format)
        self.connectionmanager = ConnectionManagerAPI(format=self.format)
        self.bridgedomain = BridgeDomainAPI(format=self.format)
        self.request_data = None
        self.base_uri = 'http://' + self.odl.domain + \
            ':' + self.odl.port + '/controller/nb/v2'
        self.base_sec_uri = 'https://' + self.odl.domain + \
            ':' + self.odl.sec_port + '/controller/nb/v2'
        self.full_uri = None
        self.response = None
        self.method_table = {'GET': requests.get, 'PUT': requests.put,
                             'DELETE': requests.delete, 'POST': requests.post}
        self.method = None

    def set_container(self, container):
        self.container = container

    def set_format(self, format):
        self.format = format

    def __request(self, request_data):
        if request_data.sec:
            self.full_uri = self.base_sec_uri + request_data.uri
        else:
            self.full_uri = self.base_uri + request_data.uri
        self.method = self.method_table[request_data.method]
        self.response = self.method(
            self.full_uri, auth=self.odl.auth, data=request_data.data, headers=request_data.headers)
        print('req uri: {2} \n{0}\n{1}'.format(
            self.response.status_code, self.response.text, self.full_uri))
        return self.response

    def __request_top(self, request_data_func, **func_kwargs):
        if 'container' in func_kwargs and func_kwargs['container'] is None:
            func_kwargs['container'] = self.container
        self.request_data = request_data_func(**func_kwargs)
        return self.__request(self.request_data)

    """
    def __request_top_with_config(self,request_data_func,other_parameter,container=None):
        if container is None:
            container=self.container
        self.request_data=request_data_func(container,other_parameter)
        return self.__request(self.request_data)
    """

    """
    Topology API
    """

    def retrieve_the_topology(self, container=None):
        return self.__request_top(request_data_func=self.topology.retrieve_the_topology, container=container)

    def retrieve_userLinks(self, container=None):
        return self.__request_top(request_data_func=self.topology.retrieve_userLinks, container=container)

    def add_userLink(self, container, topologyUserLinkConfig):
        return self.__request_top(request_data_func=self.topology.add_userLink, container=container, topologyUserLinkConfig=topologyUserLinkConfig)

    def del_userLink(self, container, linkName):
        return self.__request_top(request_data_func=self.topology.del_userLink, container=container, linkName=linkName)

    """
    FlowProgrammer API
    """

    def retrieve_flows(self, container=None):
        return self.__request_top(request_data_func=self.flowprogrammer.retrieve_flows, container=container)

    def retrieve_node_flows(self, nodeId, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.flowprogrammer.retrieve_node_flows, nodeId=nodeId, nodeType=nodeType, container=container)

    def retrieve_flow_by_name(self, nodeId, flowName, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.flowprogrammer.retrieve_flow_by_name, nodeId=nodeId, flowName=flowName, nodeType=nodeType, container=container)

    def del_flow_by_name(self, nodeId, flowName, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.flowprogrammer.del_flow_by_name, nodeId=nodeId, flowName=flowName, nodeType=nodeType, container=container)

    def add_or_modify_flow_by_name(self, nodeId, flowName, flowConfig, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.flowprogrammer.add_or_modify_flow_by_name, nodeId=nodeId, flowName=flowName, flowConfig=flowConfig, nodeType=nodeType, container=container)

    """
    HostTracker API
    """

    def retrieve_host_by_address(self, networkAddress, container=None):
        return self.__request_top(request_data_func=self.hosttracker.retrieve_host_by_address, networkAddress=networkAddress, container=container)

    def add_host(self, networkAddress, hostConfig, container=None):
        return self.__request_top(request_data_func=self.hosttracker.add_host, networkAddress=networkAddress, hostConfig=hostConfig, container=container)

    def del_host(self, networkAddress, container=None):
        return self.__request_top(request_data_func=self.hosttracker.del_host, networkAddress=networkAddress, container=container)

    def retrieve_active_hosts(self, container=None):
        return self.__request_top(request_data_func=self.hosttracker.retrieve_active_hosts, container=container)

    def retrieve_inactive_hosts(self, container=None):
        return self.__request_top(request_data_func=self.hosttracker.retrieve_inactive_hosts, container=container)

    """
    StaticRoute API
    """

    def retrieve_all_static_routes(self, container=None):
        return self.__request_top(request_data_func=self.staticroute.retrieve_all_static_routes, container=container)

    def retrieve_static_route_by_name(self, route, container=None):
        return self.__request_top(request_data_func=self.staticroute.retrieve_static_route_by_name, route=route, container=container)

    def add_static_route(self, route, staticRoute, container):
        return self.__request_top(request_data_func=self.staticroute.add_static_route, route=route, staticRoute=staticRoute, container=container)

    def del_static_route(self, route, container):
        return self.__request_top(request_data_func=self.staticroute.del_static_route, route=route, container=container)

    """
    Statistics API
    """

    def retrieve_all_statistics_flow(self, container=None):
        return self.__request_top(request_data_func=self.statistics.retrieve_all_statistics, elementType='flow', container=container)

    def retrieve_all_statistics_port(self, container=None):
        return self.__request_top(request_data_func=self.statistics.retrieve_all_statistics, elementType='port', container=container)

    def retrieve_all_statistics_table(self, container=None):
        return self.__request_top(request_data_func=self.statistics.retrieve_all_statistics, elementType='table', container=container)

    def retrieve_node_statistics_flow(self, nodeId, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.statistics.retrieve_node_statistics, nodeId=nodeId, nodeType=nodeType, elementType='flow', container=container)

    def retrieve_node_statistics_port(self, nodeId, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.statistics.retrieve_node_statistics, nodeId=nodeId, nodeType=nodeType, elementType='port', container=container)

    def retrieve_node_statistics_table(self, nodeId, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.statistics.retrieve_node_statistics, nodeId=nodeId, nodeType=nodeType, elementType='table', container=container)

    """
    Subnets API
    """

    def retrieve_all_subnets(self, container=None):
        return self.__request_top(request_data_func=self.subnets.retrieve_all_subnets, container=container)

    def retrieve_subnet_by_name(self, subnetName, container=None):
        return self.__request_top(request_data_func=self.subnets.retrieve_subnet_by_name, subnetName=subnetName, container=container)

    def add_subnet(self, subnetName, subnetConfig, container=None):
        return self.__request_top(request_data_func=self.subnets.add_subnet, subnetName=subnetName, subnetConfig=subnetConfig, container=container)

    def del_subnet(self, subnetName, container=None):
        return self.__request_top(request_dat_func=self.subnets.del_subnet, subnetName=subnetName, container=container)

    def modify_subnet(self, subnetName, subnetConfig, container=None):
        return self.__request_top(request_data_func=self.subnets.modify_subnet, subnetName=subnetName, subnetConfig=subnetConfig, container=container)

    """
    SwitchManager API
    """

    def retrieve_all_nodes(self, container=None):
        return self.__request_top(request_data_func=self.switchmanager.retrieve_all_nodes, container=container)

    def save_nodes_config(self, container=None):
        return self.__request_top(request_data_func=self.switchmanager.save_nodes_config, container=container)

    def retrieve_node_connectors_by_node(self, nodeId, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.switchmanager.retrieve_node_connectors_by_node, nodeId=nodeId, nodeType=nodeType, container=container)

    def del_node_property(self, nodeId, propertyName, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.switchmanager.del_node_property, nodeId=nodeId, propertyName=propertyName, nodeType=nodeType, container=container)

    def add_node_property(self, nodeId, propertyName, propertyValue, nodeType='OF', container=None):
        return self.__request_top(request_data_func=self.switchmanager.add_node_property, nodeId=nodeId, propertyName=propertyName, propertyValue=propertyValue, nodeType=nodeType, container=container)

    def del_node_connector_property(self, nodeId, nodeConnectorId, nodeType='OF', nodeConnectorType='OF', container=None):
        return self.__request_top(request_data_func=self.switchmanager.del_node_connector_property, nodeId=nodeId, nodeConnectorId=nodeConnectorId, nodeType=nodeType, nodeConnectorType=nodeConnectorType, container=container)

    def add_node_connector_property(self, nodeId, nodeConnectorId, propertyName, propertyValue, nodeType='OF', nodeConnectorType='OF', container=None):
        return self.__request_top(request_data_func=self.switchmanager.add_node_connector_property, nodeId=nodeId, nodeConnectorId=nodeConnectorId, propertyName=propertyName, propertyValue=propertyValue, nodeType=nodeType, nodeConnectorType=nodeConnectorType, container=container)

    """
    UserManager API
    """

    def add_user(self, userConfig):
        return self.__request_top(request_data_func=self.usermanager.add_user, userConfig=userConfig)

    def del_user(self, userName):
        return self.__request_top(request_data_func=self.usermanager.del_user, userName=userName)

    """
    ContainerManager API
    """

    def retrieve_all_containers(self):
        return self.__request_top(request_data_func=self.containermanager.retrieve_all_containers)

    def retrieve_container_config(self, container=None):
        return self.__request_top(request_data_func=self.containermanager.retrieve_container_config, container=container)

    def create_container(self, containerConfig):
        return self.__request_top(request_data_func=self.containermanager.create_container, containerConfig=containerConfig)

    def del_container(self, container=None):
        return self.__request_top(request_data_func=self.containermanager.del_container, container=container)

    def retrieve_flowspecs_by_container(self, container=None):
        return self.__request_top(request_data_func=self.containermanager.retrieve_flowspecs_by_container, container=container)

    def add_node_connectors_to_container(self, nodeConnectors, container=None):
        return self.__request_top(reqeust_data_func=self.containermanager.add_node_connectors_to_container, nodeConnectors=nodeConnectors, container=container)

    def del_node_connectors_from_container(self, nodeConnectors, container=None):
        return self.__request_top(reqeust_data_func=self.containermanager.del_node_connectors_from_container, nodeConnectors=nodeConnectors, container=container)

    def retrieve_flowspec(self, flowspec, container=None):
        return self.__request_top(request_data_func=self.containermanager.retrieve_flowspec, flowspec=flowspec, container=container)

    def add_flowspec_to_container(self, flowSpecConfig, container=None):
        return self.__request_top(reqeust_data_func=self.containermanager.add_flowspec_to_container, flowSpecConfig=flowSpecConfig, container=container)

    def del_flowspec_from_container(self, flowspec, container=None):
        return self.__request_top(request_data_func=self.containermanager.del_flowspec_from_container, flowspec=flowspec, container=container)

    """
    ConnectionManager API
    """

    def retrieve_all_nodes_of_controller(self, controllerIP=None):
        return self.__request_top(request_data_func=self.connectionmanager.retrieve_all_nodes_of_controller, controllerIP=controllerIP)

    def del_connection(self, connectionNodeId, connectionNodeType):
        return self.__request_top(request_data_func=self.connectionmanager.del_connection, conenctionNodeId=connectionNodeId, connectionNodeType=connectionNodeType)

    def add_management_connection_with_node(self, nodeId, nodeIPAddress, serverPort, nodeType=None):
        return self.__request_top(request_data_func=self.connectionmanager.add_nanagement_connection_with_node, nodeId=nodeId, nodeIPAddress=nodeIPAddress, serverPort=serverPort, nodeType=nodeType)

    """
    BridgeDomain API
    """

    def create_bridge(self, nodeType, nodeID, bridgeName):
        return self.__request_top(request_data_func=self.bridgedomain.create_bridge, nodeType=nodeType, nodeID=nodeID, bridgeName=bridgeName)

    def del_bridge(self, nodeType, nodeID, bridgeName):
        return self.__request_top(request_data_func=self.bridgedomain.del_bridge, nodeType=nodeType, nodeID=nodeID, bridgeName=bridgeName)

    def add_port_to_bridge(self, nodeType, nodeID, bridgeName, portName):
        return self.__request_top(request_data_func=self.bridgedomain.add_port_to_bridge, nodeType=nodeType, nodeID=nodeID, bridgeName=bridgeName, portName=portName)

    def del_port_from_bridge(self, nodeType, nodeID, bridgeName, portName):
        return self.__request_top(request_data_func=self.bridgedomain.del_port_from_bridge, nodeType=nodeType, nodeID=nodeID, bridgeName=bridgeName, portName=portName)

    def add_port_vlan_to_bridge(self, nodeType, nodeID, bridgeName, portName, vlan):
        return self.__request_top(request_data_func=self.bridgedomain.add_port_vlan_to_bridge, nodeType=nodeType, nodeID=nodeID, bridgeName=bridgeName, portName=portName, vlan=vlan)
