from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.7
)

print("\n🧪 Prompt Playground (LangChain v1)")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Enter your prompt: ")

    if user_input.lower() == "exit":
        print("Exiting playground...")
        print("exited")
        break

    response = llm.invoke(user_input)

    print("\nGemini Response:\n")
    print(response.content)
    print("\n" + "-" * 60)
