import random

def generate_place_value_question_identify_tu(max_number=99):
    """
    Asks: 'How many tens and units does X have?'
    Example: 'How many tens and units does 56 have?'
    """
    number = random.randint(10, max_number)  # ensures at least 2 digits
    tens = number // 10
    units = number % 10

    question_text = f"How many tens and units does {number} have?"
    correct_answer = f"{tens} tens and {units} units"

    return {
        "topic": "place_value",
        "skill": "identify_tens_units",
        "questionText": question_text,
        "correctAnswer": correct_answer
    }

def generate_place_value_question_from_tu(max_tens=9, max_units=9):
    """
    Asks: 'What number is X tens and Y units?'
    Example: 'What number is 3 tens and 7 units?'
    """
    tens = random.randint(1, max_tens)  # at least 1 tens
    units = random.randint(0, max_units)
    number = 10 * tens + units

    question_text = f"What number is {tens} tens and {units} units?"
    correct_answer = str(number)

    return {
        "topic": "place_value",
        "skill": "combine_tens_units",
        "questionText": question_text,
        "correctAnswer": correct_answer
    }

# commit comment

def generate_questions(n=5):
    """
    Creates a list of 'n' questions, mixing up the two sub-question types.
    """
    # A list of functions that can generate questions.
    generators = [
        generate_place_value_question_identify_tu,
        generate_place_value_question_from_tu
    ]

    questions = []
    for _ in range(n):
        # Pick one generator at random
        gen_func = random.choice(generators)
        question = gen_func()
        questions.append(question)

    return questions

if __name__ == "__main__":
    # If you run this file directly (e.g., python generator.py),
    # we'll generate 5 example questions and print them out.
    example_questions = generate_questions(n=5)
    for i, q in enumerate(example_questions, start=1):
        print(f"Question {i}: {q['questionText']}")
        print(f"  Correct Answer: {q['correctAnswer']}")
        print()
