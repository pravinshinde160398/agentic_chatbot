from src.langgraphagenticai.state.state import State


class BasicChatbotNode():
    """_summary_
    """
    
    def __init__(self,model):
        self.llm=model
        
    def process(self,state:State)->dict:
        """_summary_

        """
        return {"messages":self.llm.invoke(state["messages"])}