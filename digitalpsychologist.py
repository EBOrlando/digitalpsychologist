import streamlit as st
import openai

# Initialize the messages list with a system message
messages = [{"role": "system", "content": "You are a psychologist expert in Freud."}]

def CustomChatGPT(user_input):
    global messages
    try:
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    except openai.error.OpenAIError as e:
        if "quota" in str(e).lower():
            return "Seu saldo é insuficiente para continuar usando a ferramenta. Por favor atualize suas opções de pagamento."
        else:
            return "An error occurred: " + str(e)

def main():
    st.title("Digital Psychologist")

    st.write("Welcome! Please enter your OpenAI API key to begin the session.")
    api_key = st.text_input("API Key", type="password")

    if api_key:
        openai.api_key = api_key  # Set the OpenAI API key
        st.write("You can now chat with the digital psychologist.")
        user_input = st.text_input("You:")
        
        if user_input:
            response = CustomChatGPT(user_input)
            st.text_area("Psychologist:", value=response, height=200, max_chars=None)

if __name__ == "__main__":
    main()
