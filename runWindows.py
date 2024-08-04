import os
os.system('/venv/Scripts/activate')
os.system('pip install -r requirements.txt')
#run program
os.system('python LLM-agent-backend/retrieving_data.py')
os.system('python LLM-agent-backend/full_text_search.py')
os.system('python LLM-agent-backend/currency_exchanger.py')
os.system('python LLM-agent-backend/filtering_data.py')
