
###################################################### CONFIGURE YOUR TOOLS HERE ######################################################


# Login Credentials for LinkedIn (Optional)
username = ""       # Enter your username in the quotes
password = ""           # Enter your password in the quotes


## Artificial Intelligence (Beta Not-Recommended)
# Use AI
use_AI = False                          # True or False, Note: True or False are case-sensitive
'''
Note: Set it as True only if you want to use AI, and If you either have a
1. Local LLM model running on your local machine, with it's APIs exposed. Example softwares to achieve it are:
    a. Ollama - https://ollama.com/
    b. llama.cpp - https://github.com/ggerganov/llama.cpp
    c. LM Studio - https://lmstudio.ai/ (Recommended)
    d. Jan - https://jan.ai/
2. OR you have a valid OpenAI API Key, and money to spare, and you don't mind spending it.
CHECK THE OPENAI API PIRCES AT THEIR WEBSITE (https://openai.com/api/pricing/). 
'''

##> ------ Yang Li : MARKYangL - Feature ------
# Select AI Provider
ai_provider = "openai"               # "openai", "deepseek"
'''
Note: Select your AI provider.
* "openai" - OpenAI API (GPT models)
* "deepseek" - DeepSeek API (DeepSeek models)
'''

# DeepSeek Configuration
deepseek_api_url = "https://api.deepseek.com"       # Examples: "https://api.deepseek.com", "https://api.deepseek.com/v1"
'''
Note: DeepSeek API URL. 
This URL is compatible with OpenAI interface. The full endpoint will be {deepseek_api_url}/chat/completions.
'''

deepseek_api_key = "YOUR_OPENAI_API_KEY"                # Enter your DeepSeek API key in the quotes
'''
Note: Enter your DeepSeek API key here. Leave it empty as "" or "not-needed" if not needed.
'''

deepseek_model = "deepseek-chat"     # Examples: "deepseek-chat", "deepseek-reasoner"
'''
Note: DeepSeek model selection
* "deepseek-chat" - DeepSeek-V3, general conversation model
* "deepseek-reasoner" - DeepSeek-R1, reasoning model
'''
##<

# Your Local LLM url or other AI api url and port
llm_api_url = "https://api.openai.com/v1/"       # Examples: "https://api.openai.com/v1/", "http://127.0.0.1:1234/v1/", "http://localhost:1234/v1/"
'''
Note: Don't forget to add / at the end of your url
'''

# Your Local LLM API key or other AI API key 
llm_api_key = "YOUR_OPENAI_API_KEY"              # Enter your API key in the quotes, make sure it's valid, if not will result in error.
'''
Note: Leave it empyt as "" or "not-needed" if not needed. Else will result in error!
'''

# Your local LLM model name or other AI model name
llm_model = "gpt-3.5-turbo"          # Examples: "gpt-3.5-turbo", "gpt-4o", "llama-3.2-3b-instruct"


#
llm_spec = "openai"                # Examples: "openai", "openai-like", "openai-like-github", "openai-like-mistral"
'''
Note: Currently "openai" and "openai-like" api endpoints are supported.
'''

# # Yor local embedding model name or other AI Embedding model name
# llm_embedding_model = "nomic-embed-text-v1.5"

# Do you want to stream AI output?
stream_output = False                    # Examples: True or False. (False is recommended for performance, True is recommended for user experience!)
'''
Set `stream_output = True` if you want to stream AI output or `stream_output = False` if not.
'''
##
