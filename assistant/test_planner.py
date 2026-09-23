from assistant.graph import build_graph
from assistant.tools import list_tools


print("================================")
print("        DOT PHASE 2 TEST")
print("================================")

print("\nAvailable tools:")
print(list_tools())

app = build_graph()


# Test 1: Open application
print("\n--- TEST 1: Open Notepad ---")

result = app.invoke({
    "user_input": "Open Notepad"
})

print("Intent:", result["intent"])
print("Tool:", result["tool"])
print("Response:", result["response"])


# Test 2: List files
print("\n--- TEST 2: List Files ---")

result = app.invoke({
    "user_input": "list files in ."
})

print("Intent:", result["intent"])
print("Tool:", result["tool"])
print("Response:")
print(result["response"])


# Test 3: General request
print("\n--- TEST 3: General Request ---")

result = app.invoke({
    "user_input": "Hello DOT"
})

print("Intent:", result["intent"])
print("Tool:", result["tool"])
print("Response:", result["response"])


print("\n================================")
print("       PHASE 2 TEST DONE")
print("================================")