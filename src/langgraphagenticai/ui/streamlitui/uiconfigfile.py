from configparser import ConfigParser


class Config:
    def __init__(self,config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        value = self.config["DEFAULT"].get("LLM_OPTIONS", "Groq")
        return value.split(", ")

    def get_usecase_options(self):
        value = self.config["DEFAULT"].get("USECASE_OPTIONS", "Basic Chatbot")
        return value.split(", ")

    def get_groq_model_options(self):
        value = self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "llama3-8b-8192")
        return value.split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraph Agentic AI")
    
