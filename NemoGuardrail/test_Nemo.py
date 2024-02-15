import os
import asyncio
import logging
import annoy
from nemoguardrails import LLMRails, RailsConfig
from nemoguardrails.streaming import StreamingHandler


logging.basicConfig(level=logging.INFO)

script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the paths relative to the script directory
yaml_path = os.path.join(script_dir, 'config', 'config.yml')
colang_path = os.path.join(script_dir, 'config', 'topics.co')

#get yaml and colang content 
with open(yaml_path, 'r') as yaml_file:
    yaml_content = yaml_file.read()

with open(colang_path, 'r') as colang_file:
    colang_content = colang_file.read()

#create RailsConfig instance
config = RailsConfig.from_content(yaml_content=yaml_content, colang_content=colang_content) 

# Instantiate LLMRails with the configurations
llm_rails = LLMRails(config)
print(llm_rails)

    
