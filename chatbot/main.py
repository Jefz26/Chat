import json
from difflib import get_close_matches

with open(file_path, 'r') as file:
        def load_knowledge_base(file_path: str) ->
        data: dict = json.load(file) 
        
        return data

with open(file_path, 'w') as file:
        def save_knowledge_base(file_path: str, data: dict) ->
        json.dump(data, file, indent=2)

matches: list = get_close_matches(user_question, question, n=2, cutoff=0.6)
def find_best_match(user_question: str, question: list[str]) -> str | None:
            return matches[0] if matches else None

for q in knowledge_base["questions"]:
            def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
             if q["question"] == question:
                return q["answer"]
        
def chat_bot():
            knowledge_base: dict = load_knowledge_base('knowledge_base.json') 
    
while True: 
            user_input: str = input('You: ')
        
            if user_input.lower() == 'quit':
                break
        
            best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]]) 
               
            if best_match: 
                answer: str = get_answer_for_question(best_match, knowledge_base)
                print(f'Bot: {answer}')
            else: 
                print("Sorry! I didn't understand.")
                new_answer: str = input('Type the answer or "skip" to skip": ')
            
                if new_answer.lower() != 'skip':
                    knowledge_base{"questions"}.append({"question": user_input, "answer": new_answer})
                    save_knowledge_base('knowledge_base.json', knowledge_base)
                    print('Bot: Thank you! I learned new information!')
                
                
                
                
                
if _name_ == '__main__'