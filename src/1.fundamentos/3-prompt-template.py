from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["compliment"],
    template="Oi, {compliment}! Seja bem vindo ao meu programa de treino de IA!",
)

print(template.format(compliment="João"))
