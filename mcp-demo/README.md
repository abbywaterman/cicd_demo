# In-class Activity 22 

## Step 4 – Test the prediction API

I sent the measurements `5.1, 3.5, 1.4, 0.2` to `POST /predict`. The API returned status `200` and identified the flower as `setosa`.

![FastAPI response showing the predicted species as setosa](<screenshots/Screenshot 2026-11-18 at 7.05.09 PM.png>)

## Step 6 – Which function makes the prediction, and what does MCP add?

The `predict` function in `api.py` passes the four measurements to the trained model and returns the predicted species. The `classify_iris` function in `mcp_server.py` sends those measurements to `/predict` and passes the result back to the client. MCP lets an AI app discover the tool, see which inputs it requires, and call it.

## Step 7 – Discover and call the MCP tool

The client listed `classify_iris`, displayed its description and four inputs, and returned `Predicted species: virginica` for this test.

![Terminal showing the classify_iris tool and its virginica prediction](<screenshots/Screenshot 2026-11-18 at 7.10.08 PM.png>)

## Step 8 – Where does the tool information come from, and who uses it?

The tool name comes from the function name, `classify_iris`. The description comes from its docstring. The input names come from the four function parameters, and their `float` type hints tell the client to supply numbers. The `@mcp.tool()` decorator registers the function so the client can discover it.

FastAPI’s `/docs` page is designed for a person who wants to enter measurements and test an endpoint. The MCP output is designed for an AI application that needs to discover available tools, understand what they do, and supply the right inputs.

## Step 9 – What happens when the docstring says “Does a calculation”?

If I were an LLM, I could guess from the name `classify_iris`, but “Does a calculation” gives me little guidance about whether the tool answers “What kind of iris is this?” My Python client could still call it because the tool name was hard-coded. A specific docstring helps an LLM decide when to use the tool.

## Step 10 – Test the probabilities endpoint

For the measurements `5.1, 3.5, 1.4, 0.2`, the `/probabilities` endpoint returned status `200`. The rounded probabilities were 100% setosa, 0% versicolor, and 0% virginica.

![FastAPI probabilities response for the setosa sample](<screenshots/Screenshot 2026-11-18 at 9.31.11 PM.png>)

## Step 12 – How sure is the model?

For the measurements `6.0, 2.7, 5.1, 1.6`, the model predicted **versicolor** with an estimated probability of **68%**. It assigned **32%** to virginica and **0%** to setosa. Versicolor was the most likely species, although the model still gave virginica a substantial probability.

![Terminal showing both MCP tools and the 68% versicolor result](<screenshots/Screenshot 2026-11-18 at 9.36.14 PM.png>)

## Step 13 – Does our team’s prototype need an MCP server?

Our sales qualification prototype doesn’t currently need an MCP server. Our app already controls the qualification flow, so it can call its scoring and booking functions directly. MCP would make sense if we wanted an outside AI assistant to discover and use those functions. For example, a sales rep could ask their assistant to generate a closer brief for a qualified lead.