
from nemoguardrails.rails.llm.config import RailsConfig
from nemoguardrails.rails.llm.llmrails import LLMRails


config = RailsConfig.from_path("./config")

rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "idk probably at work i suppose"
}])
print(response)

