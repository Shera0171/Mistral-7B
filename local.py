# pip3 install optimum 
# pip3 install git+https://github.com/huggingface/transformers.git@72958fcd3c98a7afdc61f953aa58c544ebda2f79


# git clone https://github.com/PanQiWei/AutoGPTQ

# git checkout v0.4.2

# pip install .

import os

from langchain.llms import CTransformers

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain

from langchain.chains.conversation.memory import ConversationBufferMemory

model_id = 'TheBloke/Mistral-7B-codealpaca-lora-GGUF'

os.environ['XDG_CACHE_HOME'] = './model/cache/'

config = { 'temperature':0.00, "context_length":4000,}

llm = CTransformers(model=model_id,model_type='mistral',config=config, callbacks=[StreamingStdOutCallbackHandler()])

llm("write a function to accept a dataframe and a column, and return a dataframe with all the null")
