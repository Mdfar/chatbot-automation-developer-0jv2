Staqlt AI Business Orchestrator
Overview

This system combines a GPT-powered conversation layer with an n8n automation backbone. It's designed to handle FAQ queries autonomously while identifying and processing high-value leads.

Deployment

Set up your environment variables: OPENAI_API_KEY and N8N_WEBHOOK_URL.

Build and run the container: docker build -t business-bot . && docker run -p 8000:8000 business-bot.

Import the workflow_template.json into your n8n instance.

Workflow

Input: User sends a message via the /chat endpoint.

Reasoning: FastAPI sends the query to GPT-4o.

Automation: If lead intent is detected, FastAPI triggers the n8n webhook.

Outcome: n8n syncs the lead to HubSpot and alerts the sales team.