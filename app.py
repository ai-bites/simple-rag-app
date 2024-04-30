import streamlit as st
from typing import Optional

from langflow import load_flow_from_json 


TWEAKS = {
  "PyPDFLoader-meyB2": {},
  "RecursiveCharacterTextSplitter-aIe6R": {},
  "OllamaEmbeddings-FzJxP": {},
  "BaseChatModel-uQUH3": {},
  "ConversationBufferMemory-adobv": {},
  "ConversationalRetrievalChain-RD8zz": {},
  "FAISS-I7M5T": {},
  "PyPDFLoader-BqluX": {},
  "PyPDFLoader-wBYkk": {},
  "PyPDFLoader-cvTr4": {}
}


def run_flow(inputs: dict, flow_id: str, tweaks: Optional[dict] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{FLOW_ID}"

    payload = {"inputs": inputs}
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()



def chat(prompt: str):
  with current_chat_message:
    # Block input to prevent sending messages whilst AI is responding
    st.session_state.disabled = True

    # Add user message to chat history
    st.session_state.messages.append(("human", prompt))

    # Display user message in chat message container
    with st.chat_message("human"):
      st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("ai"):
      # Get complete chat history, including latest question as last message
      history = "\n".join(
        [f"{role}: {msg}" for role, msg in st.session_state.messages]
      )

      query = f"{history}\nAI:"

      # Setup any tweaks you want to apply to the flow
      inputs = {"question": query}

      # output = run_flow(inputs, flow_id=FLOW_ID, tweaks=TWEAKS)
      flow = load_flow_from_json(flow="RAG_app_demo_2.json", tweaks=TWEAKS)
      output = flow(inputs)
      print("output from the model is: ")
      print(output)
      try:
        output = output['chat_history'][-1].content
      except Exception :
        output = f"Application error : {output}"

      placeholder = st.empty()

      # write response without "▌" to indicate completed message.
      with placeholder:
        st.markdown(output)

    # Log AI response to chat history
    st.session_state.messages.append(("ai", output))
    # Unblock chat input
    st.session_state.disabled = False

    st.rerun()


st.set_page_config(page_title="AI for AI")
st.title("Welcome to the AI explains AI world!")

system_prompt = "You´re a helpful assistant who can explain concepts"
if "messages" not in st.session_state:
    st.session_state.messages = [("system", system_prompt)]
if "disabled" not in st.session_state:
    # `disable` flag to prevent user from sending messages whilst the AI is responding
    st.session_state.disabled = False


with st.chat_message("ai"):
  st.markdown(
    f"Hi! I'm your AI assistant."
  )

# Display chat messages from history on app rerun
for role, message in st.session_state.messages:
    if role == "system":
        continue
    with st.chat_message(role):
        st.markdown(message)

current_chat_message = st.container()
prompt = st.chat_input("Ask your question here...", disabled=st.session_state.disabled)

if prompt:
    chat(prompt)

