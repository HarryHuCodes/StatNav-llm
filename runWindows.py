import os
os.system('/venv/Scripts/activate')
os.system('pip install -r requirements.txt')
#run program
os.system('python LLM-agent-backend/retrieving_data.py')