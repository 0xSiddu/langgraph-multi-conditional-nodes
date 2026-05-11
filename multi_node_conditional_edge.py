from langgraph.graph import StateGraph, END
from typing import TypedDict, Literal

# Define the state structure
class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    number3: int
    number4: int
    operation2: str
    finalNumber: int
    finalNumber2: int

# Define the nodes
def router(state: AgentState) -> AgentState:
    """Router node that passes state through"""
    print(f"Router: Current state - number1={state['number1']}, operation={state['operation']}")
    return state

def add_node(state: AgentState) -> AgentState:
    """Addition node: number1 + number2"""
    result = state['number1'] + state['number2']
    print(f"Add_node: {state['number1']} + {state['number2']} = {result}")
    state['finalNumber'] = result
    return state

def subtract_node(state: AgentState) -> AgentState:
    """Subtraction node: number1 - number2"""
    result = state['number1'] - state['number2']
    print(f"Subtract_node: {state['number1']} - {state['number2']} = {result}")
    state['finalNumber'] = result
    return state

def router2(state: AgentState) -> AgentState:
    """Second router node"""
    print(f"Router2: Current state - number3={state['number3']}, operation2={state['operation2']}")
    return state

def add_node2(state: AgentState) -> AgentState:
    """Second addition node: number3 + number4"""
    result = state['number3'] + state['number4']
    print(f"Add_node2: {state['number3']} + {state['number4']} = {result}")
    state['finalNumber2'] = result
    return state

def subtract_node2(state: AgentState) -> AgentState:
    """Second subtraction node: number3 - number4"""
    result = state['number3'] - state['number4']
    print(f"Subtract_node2: {state['number3']} - {state['number4']} = {result}")
    state['finalNumber2'] = result
    return state

# Conditional edge functions
def route_operation(state: AgentState) -> Literal["add_node", "subtract_node"]:
    """Route based on first operation"""
    if state['operation'] == '+':
        return "add_node"
    else:
        return "subtract_node"

def route_operation2(state: AgentState) -> Literal["add_node2", "subtract_node2"]:
    """Route based on second operation"""
    if state['operation2'] == '+':
        return "add_node2"
    else:
        return "subtract_node2"

# Build the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("router", router)
workflow.add_node("add_node", add_node)
workflow.add_node("subtract_node", subtract_node)
workflow.add_node("router2", router2)
workflow.add_node("add_node2", add_node2)
workflow.add_node("subtract_node2", subtract_node2)

# Set entry point
workflow.set_entry_point("router")

# Add conditional edges from router
workflow.add_conditional_edges(
    "router",
    route_operation,
    {
        "add_node": "add_node",
        "subtract_node": "subtract_node"
    }
)

# Both add_node and subtract_node go to router2
workflow.add_edge("add_node", "router2")
workflow.add_edge("subtract_node", "router2")

# Add conditional edges from router2
workflow.add_conditional_edges(
    "router2",
    route_operation2,
    {
        "add_node2": "add_node2",
        "subtract_node2": "subtract_node2"
    }
)

# Both paths end at END
workflow.add_edge("add_node2", END)
workflow.add_edge("subtract_node2", END)

# Compile the graph
app = workflow.compile()

# Test with the provided input
if __name__ == "__main__":
    initial_state = AgentState(
        number1=10,
        operation="-",
        number2=5,
        number3=7,
        number4=2,
        operation2="+",
        finalNumber=0,
        finalNumber2=0
    )
    
    print("=" * 50)
    print("Starting execution with initial state:")
    print(f"number1={initial_state['number1']}, operation='{initial_state['operation']}'")
    print(f"number2={initial_state['number2']}, number3={initial_state['number3']}")
    print(f"number4={initial_state['number4']}, operation2='{initial_state['operation2']}'")
    print("=" * 50)
    
    # Run the graph
    result = app.invoke(initial_state)
    
    print("=" * 50)
    print("Final Results:")
    print(f"First operation result (finalNumber): {result['finalNumber']}")
    print(f"Second operation result (finalNumber2): {result['finalNumber2']}")
    print("=" * 50)
