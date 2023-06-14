from sequence.network_management.network_manager import NetworkManager
from sequence.network_management.network_manager import StaticRoutingProtocol
from sequence.network_management.network_manager import ResourceReservationProtocol
from sequence.topology.node import QuantumRouter
import matplotlib.pyplot as plt
import numpy as np
def NewNetworkManager(owner: "QuantumRouter") -> "NetworkManager":
    manager = NetworkManager(owner, [])
    routing = StaticRoutingProtocol(owner, owner.name + ".StaticRoutingProtocol", {})
    rsvp = ResourceReservationProtocol(owner, owner.name + ".RSVP")
    routing.upper_protocols.append(rsvp)
    rsvp.lower_protocols.append(routing)
    manager.load_stack([routing, rsvp])
    return manager

from sequence.topology.router_net_topo import RouterNetTopo




def set_parameters(topology: RouterNetTopo,distance, freq):
    # set memory parameters
    nodes_len = len(topology.get_nodes_by_type(RouterNetTopo.QUANTUM_ROUTER))
    DISTANCE = distance/nodes_len
    MEMO_FREQ = freq
    MEMO_EXPIRE = 10e-3
    MEMO_EFFICIENCY = 0.5
    MEMO_FIDELITY = 0.99 #F
    WAVE_LENGTH = 1550
    for node in topology.get_nodes_by_type(RouterNetTopo.QUANTUM_ROUTER):
        memory_array = node.get_components_by_type("MemoryArray")[0]
        memory_array.update_memory_params("frequency", MEMO_FREQ)
        memory_array.update_memory_params("coherence_time", MEMO_EXPIRE)
        memory_array.update_memory_params("efficiency", MEMO_EFFICIENCY)
        memory_array.update_memory_params("raw_fidelity", MEMO_FIDELITY)
        memory_array.update_memory_params("wavelength", WAVE_LENGTH)

    # set detector parameters
    DETECTOR_EFFICIENCY = 0.39
    
    for node in topology.get_nodes_by_type(RouterNetTopo.BSM_NODE):
        bsm = node.get_components_by_type("SingleAtomBSM")[0]
        bsm.update_detectors_params("efficiency", DETECTOR_EFFICIENCY)
    # set entanglement swapping parameters
    SWAP_SUCC_PROB = 0.5
    for node in topology.get_nodes_by_type(RouterNetTopo.QUANTUM_ROUTER):
        node.network_manager.protocol_stack[1].set_swapping_success_rate(SWAP_SUCC_PROB)
        
    # set quantum channel parameters
    
    QC_FREQ = 1e11
    for qc in topology.get_qchannels():
        qc.distance=DISTANCE
        qc.frequency = QC_FREQ
    # set classical channel parameters
    for cc in topology.get_cchannels():
         cc.distance = DISTANCE


"""def execute_if_called(func,node):
    def wrapper(*args, **kwargs):
        # Check if the specific function is being called
        if func.__name__ == 'update':
            # Execute the script only if the function is being called
            print('Executing the special script...')
            for info in node.resource_manager.memory_manager:
                print("{:6}\t{:15}\t{:9}\t{}\t{}".format(str(info.index),
                                           str(info.remote_node),
                                           str(info.fidelity),
                                           str(info.entangle_time * 1e-12),
                                           str(info.state)))

            # Put your code here that should be executed only if the function is called
        # Call the original function
        return func(*args, **kwargs)
    return wrapper

# Define a new function that calls the original function and applies the decorator to it
def my_special_function_wrapper(obj,node):
    # Get a reference to the original function
    original_func = obj.update
    # Apply the decorator to the original function
    wrapped_func = execute_if_called(original_func,node)
    # Replace the original function with the wrapped function
    obj.update = wrapped_func
    # Return the object
    return obj"""

def simulate(distance, freq):
    
    network_topo = RouterNetTopo(network_config)
    tl = network_topo.get_timeline()
    set_parameters(network_topo,distance,freq)
    # the start and end nodes may be edited as desired 
    
    start_time=1e10
    node1 = network_topo.get_nodes_by_type(RouterNetTopo.QUANTUM_ROUTER)[0]
    node2 = network_topo.get_nodes_by_type(RouterNetTopo.QUANTUM_ROUTER)[-1]
    nm = node1.network_manager
    nm.request(node2.name, start_time, end_time=3e12, memory_size=1,target_fidelity = 0)
    
    #node1.resource_manager.memory_manager = my_special_function_wrapper(node1.resource_manager.memory_manager,node1)
    tl.init()
    
    tl.run()
    print("Index:\tEntangled Node:\tFidelity:\tEntanglement Time:")
    for info in node1.resource_manager.memory_manager:
            print("{:6}\t{:15}\t{:9}\t{}".format(str(info.index),
                                            str(info.remote_node),
                                            str(info.fidelity),
                                            str(info.entangle_time * 1e-12)))
    info =  node1.resource_manager.memory_manager[0]
    eg_gen_rate = 1e12 / (info.entangle_time-start_time)
    print(eg_gen_rate)
    return eg_gen_rate



freqList = [1.2e9,1.2e8,1.2e7,1.2e5]
freqDict = {"10us":1.2e9}#,"100us":1.2e8,"1ms":1.2e7,"100ms":1.2e5}
network_config = "networks/4nodes.json"
start_index = network_config.find("/networks/") + len("/networks/")
end_index = network_config.find(".json")
network = network_config[start_index:end_index]
final_distance = 300000
distances = list(range(1, final_distance+1, 10000))
for freq in freqDict:
    rates = []
    for L in distances:
        rates.append(simulate(L,freqDict[freq]))
    # Save rates to a file
    filename = "rates/freq/"+freq+".txt"
    # Save rates to a file
    np.savetxt(filename, rates)




"""# Create plot with logarithmic scale for y-axis
fig, ax = plt.subplots()
ax.set_xscale('linear')
ax.set_yscale('log')
ax.set_ylim([10**(-1), 10**4])
ax.plot(distances, rates)

# Add labels and titles
ax.set_xlabel('Distance')
ax.set_ylabel('Rate')
ax.set_title('Rates vs. Distance')

# Show the plot
plt.show()"""

