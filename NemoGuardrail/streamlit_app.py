import streamlit as st
import utils
import streamlit as st
from streaming import StreamHandler

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

import streamlit as st

st.set_page_config(page_title="test_bufferMemory")
st.header('test_bufferMemory -10thFeb')

class ContextChatbot:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"
        self.instructions = ("In less than 50 words, Be a compassionate listening ear for the user. Empathize, validate, and encourage. Be professional. Only after you have understood and questioned like a therapist should you offer advice appropriately. Respond efficiently and human-like. If you dont know any factual information, be honest about it.")
    
    @st.cache_resource
    def setup_chain(_self):
        memory = ConversationBufferMemory()
        llm = OpenAI(model_name=_self.openai_model, 
                     temperature=0,
                     streaming=True)
        chain = ConversationChain(llm=llm,
                                  memory=memory,
                                  verbose=True)
        return chain
    
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Type here...")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(self.instructions + user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    obj = ContextChatbot()
    obj.main()
