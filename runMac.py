import os
os.system('source venv/bin/activate')
os.system('pip install -r requirements.txt')
#run program
os.system('python3 LLM-agent-backend/retrieving_data.py')