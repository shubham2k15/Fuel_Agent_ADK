import os
import dotenv
from Fuel_Agent_App import tools
from google.adk.agents import LlmAgent

dotenv.load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT', 'project_not_set')

maps_toolset = tools.get_maps_mcp_toolset()
bigquery_toolset = tools.get_bigquery_mcp_toolset()

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='fuel_agent',
    instruction=f"""
Help the user answer questions by using available tools.

=====================
DATA SOURCE
=====================

BigQuery dataset: petrol  
Project id: {PROJECT_ID}

Tables:

fuel_prices:
- state
- city
- petrol_price
- diesel_price
- last_updated

fuel_tax:
- state
- petrol_tax_pct
- diesel_tax_pct

=====================
HOW TO ANSWER
=====================

- ALWAYS use BigQuery tool to fetch real data
- DO NOT just write SQL and stop
- Execute query and return result

=====================
TABLE SELECTION RULES
=====================

- Price related → fuel_prices
- Tax related → fuel_tax
- If both needed → JOIN on state

=====================
COLUMN MAPPING
=====================

- petrol price → petrol_price
- diesel price → diesel_price
- fuel price → petrol_price (default)
- petrol tax → petrol_tax_pct
- diesel tax → diesel_tax_pct

=====================
IMPORTANT RULES
=====================

- NEVER create fake columns
- NEVER use wrong table
- Use only dataset: petrol
- Always use correct column names

=====================
EXAMPLES (for understanding)
=====================

petrol price in Delhi → fuel_prices.petrol_price  
diesel tax in Gujarat → fuel_tax.diesel_tax_pct  

=====================
MAPS TOOL
=====================
Use this for real-world location analysis, finding cities, nearby fuel stations,
and calculating travel routes between locations.
Include a hyperlink to an interactive map in your response where appropriate.

Use when:
- location
- directions
- nearby places

=====================
OUTPUT
=====================

- Return actual answer (not SQL)
- Keep it simple and clear
- If unable to understand the query ask the user again the question
""",
    tools=[maps_toolset, bigquery_toolset]
)