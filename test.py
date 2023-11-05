import streamlit as st
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Function to generate questions using GPT-3.5
def generate_questions(text, max_tokens=50):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Generate questions from the following text: {text}\n\nQuestions:",
        max_tokens=max_tokens,
        stop=None
    )
    questions = response.choices[0].text.strip()
    return questions

# Streamlit app
def main():
    st.title("Text to Questions Generator")

    input_text = st.text_area("Enter your text:", height=200)
    if st.button("Generate Questions"):
        generated_questions = generate_questions(input_text)
        st.subheader("Generated Questions:")
        st.write(generated_questions)

if __name__ == "__main__":
    main()
