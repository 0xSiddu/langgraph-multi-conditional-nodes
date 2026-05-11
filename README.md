markdown# LangGraph Exercise - Graph IV: Conditional Routing

A LangGraph implementation demonstrating conditional edges with dual mathematical operation routing.

## Overview

This graph performs two sequential mathematical operations with conditional routing based on operation type (addition or subtraction).

## Graph Structure
start → router → [add_node OR subtract_node] → router2 → [add_node2 OR subtract_node2] → end

### Nodes
- **router**: First routing decision point
- **add_node**: Performs `number1 + number2`
- **subtract_node**: Performs `number1 - number2`
- **router2**: Second routing decision point
- **add_node2**: Performs `number3 + number4`
- **subtract_node2**: Performs `number3 - number4`

### Conditional Edges
1. **First conditional edge**: Routes to `add_node` if `operation="+"`, else `subtract_node`
2. **Second conditional edge**: Routes to `add_node2` if `operation2="+"`, else `subtract_node2`

## Installation

```bash
pip install langgraph
```

## Usage

```python
python graph_iv.py
```

### Example Input

```python
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
```

### Expected Output
First operation result (finalNumber): 5    # 10 - 5
Second operation result (finalNumber2): 9   # 7 + 2

## Key Features

- ✅ Two conditional routing points
- ✅ Parallel operation paths (addition/subtraction)
- ✅ State management across multiple nodes
- ✅ Sequential processing with branching logic

## State Structure

| Field | Type | Description |
|-------|------|-------------|
| `number1` | int | First operand for first operation |
| `operation` | str | First operation type ("+" or "-") |
| `number2` | int | Second operand for first operation |
| `number3` | int | First operand for second operation |
| `number4` | int | Second operand for second operation |
| `operation2` | str | Second operation type ("+" or "-") |
| `finalNumber` | int | Result of first operation |
| `finalNumber2` | int | Result of second operation |

## Course

From: **LangGraph Complete Course for Beginners - Complex AI Agents with Python**
