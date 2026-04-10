# Fuel Agent: Google ADK MCP Demo


This repository contains the **Fuel Agent**, a demonstration of an AI-powered agent built with Google Agent Development Kit (ADK) that leverages Model Context Protocol (MCP) to integrate BigQuery and Google Maps services. The agent provides real-time fuel price information and location-based services for users in India.

## Table of Contents

- [Features](#features)
- [Demo Overview](#demo-overview)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Real-time Fuel Price Queries**: Get current petrol and diesel prices by city and state
- **Tax Information**: Access fuel tax percentages across Indian states
- **Location Services**: Find nearby fuel stations and get directions using Google Maps
- **Secure Data Access**: Uses MCP for secure, remote access to Google Cloud services
- **AI-Powered Responses**: Leverages Gemini 2.5 Flash for intelligent query processing

## Demo Overview

The Fuel Agent demonstrates how AI agents can orchestrate multiple enterprise data sources and geospatial services to provide comprehensive answers to user queries. For example:

> *"What's the current petrol price in Mumbai?"*  
> *"Find the nearest fuel stations to my location in Delhi."*  
> *"What are the fuel taxes in Gujarat?"*

The agent autonomously:
1. Parses user queries to identify data requirements
2. Queries BigQuery datasets for fuel price and tax information
3. Uses Google Maps for location-based services
4. Provides clear, actionable responses with relevant context

## Architecture

The agent is built using Google ADK and integrates with remote MCP servers for secure access to:

- **BigQuery**: Enterprise data warehouse containing fuel price and tax datasets
- **Google Maps Platform**: Geospatial services for location analysis and directions

### Architecture Diagram


The diagram shows how the agent orchestrates data flow between user queries, BigQuery datasets, and Google Maps services through MCP toolset

## Prerequisites

- **Google Cloud Project** with billing enabled
- **Google Cloud SDK** (`gcloud` CLI) installed
- **Python 3.8+** installed
- **Git** for cloning the repository

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Fuel_Agent.git
cd Fuel_Agent
```

### 2. Set Up Google Cloud Environment

Configure your Google Cloud project:

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

### 3. Run Environment Setup

Execute the setup scripts to configure required services:

```bash
# Make scripts executable (Linux/Mac)
chmod +x setup/setup_env.sh setup/setup_bigquery.sh

# Configure environment and APIs
./setup/setup_env.sh

# Provision BigQuery datasets
./setup/setup_bigquery.sh
```

The setup scripts will:
- Enable required Google Cloud APIs
- Create a restricted Google Maps API key
- Set up BigQuery datasets and load sample data
- Generate environment configuration files

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Agent

After setup, launch the ADK web interface:

```bash
cd adk_agent
adk web
```

Open the provided URL in your browser to interact with the Fuel Agent.

### Example Queries

Try these sample queries to test the agent's capabilities:

- *"What is the current petrol price in Delhi?"*
- *"Show me nearby fuel stations in Mumbai"*
- *"What is the diesel tax rate in Gujarat?"*
- *"Find fuel stations within 5km of Connaught Place, Delhi"*

### API Usage

The agent can also be integrated programmatically using the ADK SDK:

```python
from Fuel_Agent_App.agent import root_agent

# Query the agent
response = root_agent.query("petrol price in Bangalore")
print(response)
```

## Data Sources

The agent accesses the following BigQuery datasets in the `petrol` project:

### fuel_prices
- **state**: Indian state name
- **city**: City name
- **petrol_price**: Current petrol price (INR/liter)
- **diesel_price**: Current diesel price (INR/liter)
- **last_updated**: Date of last price update

### fuel_tax
- **state**: Indian state name
- **petrol_tax_pct**: Petrol tax percentage
- **diesel_tax_pct**: Diesel tax percentage

### Additional Datasets
- **fuel_trends**: Historical price trends
- **fuel_consumption**: State-wise fuel consumption statistics


Example queries:
- "What is the petrol price in Delhi?"
- "Show me nearby fuel stations in Mumbai."
- "What is the diesel tax in Gujarat?"

