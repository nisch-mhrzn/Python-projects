import random
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class LearningAssistant:
    def __init__(self):
        self.model_name = "google/flan-t5-base"
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.user_progress = {}
        self.topics = ["Python", "Machine Learning", "Data Structures", "Algorithms", "Statistics"]

    def generate_content(self, topic, difficulty):
        prompt = f"Generate a long lesson about {topic} for a {difficulty} level student."
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_length=200, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def answer_question(self, question):
        prompt = f"Answer the following question: {question}"
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_length=100, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def generate_question(self, topic, difficulty):
        prompt = f"Generate a {difficulty} level question about {topic}."
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_length=50, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def update_progress(self, topic, score):
        if topic not in self.user_progress:
            self.user_progress[topic] = {"score": 0, "questions_answered": 0}
        self.user_progress[topic]["score"] += score
        self.user_progress[topic]["questions_answered"] += 1

    def get_difficulty(self, topic):
        if topic not in self.user_progress or self.user_progress[topic]["questions_answered"] < 5:
            return "beginner"
        avg_score = self.user_progress[topic]["score"] / self.user_progress[topic]["questions_answered"]
        if avg_score < 0.4:
            return "beginner"
        elif avg_score < 0.7:
            return "intermediate"
        else:
            return "advanced"

    def interactive_session(self):
        print("Welcome to your personalized learning assistant!")
        while True:
            print("\nWhat would you like to do?")
            print("1. Learn about a topic")
            print("2. Answer questions")
            print("3. View progress")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                topic = random.choice(self.topics)
                difficulty = self.get_difficulty(topic)
                content = self.generate_content(topic, difficulty)
                print(f"\nHere's a {difficulty} level lesson about {topic}:")
                print(content)

            elif choice == "2":
                topic = random.choice(self.topics)
                difficulty = self.get_difficulty(topic)
                question = self.generate_question(topic, difficulty)
                print(f"\n{question}")
                user_answer = input("Your answer: ")
                correct_answer = self.answer_question(question)
                print(f"Model's answer: {correct_answer}")
                score = float(input("Rate your answer (0-1): "))
                self.update_progress(topic, score)

            elif choice == "3":
                print("\nYour progress:")
                for topic, data in self.user_progress.items():
                    avg_score = data["score"] / data["questions_answered"]
                    print(f"{topic}: {avg_score:.2f} ({self.get_difficulty(topic)})")

            elif choice == "4":
                print("Thank you for learning with us!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    assistant = LearningAssistant()
    assistant.interactive_session()