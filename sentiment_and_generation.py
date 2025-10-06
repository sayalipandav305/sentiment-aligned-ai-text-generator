from transformers import pipeline, set_seed
import random

sentiment_analyzer = pipeline("sentiment-analysis")
generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def map_sentiment_label(hf_label, score):
    if hf_label.upper() == "POSITIVE" and score > 0.65:
        return "positive"
    if hf_label.upper() == "NEGATIVE" and score > 0.65:
        return "negative"
    return "neutral"

def detect_sentiment(text):
    res = sentiment_analyzer(text[:512])
    top = res[0]
    label = map_sentiment_label(top['label'], top['score'])
    return label, float(top['score'])

PROMPT_TEMPLATES = {
    "positive": [
        "Write a warm, uplifting paragraph about the following idea: '{}'. Make it encouraging and optimistic.",
        "Compose a positive and hopeful paragraph based on: '{}'. Keep it coherent and friendly."
    ],
    "negative": [
        "Write a candid paragraph expressing concerns or negative aspects about: '{}'. Keep it realistic and critical.",
        "Compose a reflective and somber paragraph about: '{}'. Use a thoughtful tone highlighting issues."
    ],
    "neutral": [
        "Write a balanced, neutral paragraph about: '{}'. Give facts or an impartial viewpoint.",
        "Compose an objective and informational paragraph on: '{}', without taking sides."
    ]
}

def make_prompt(sentiment_label, user_text):
    templates = PROMPT_TEMPLATES.get(sentiment_label, PROMPT_TEMPLATES['neutral'])
    template = random.choice(templates)
    return template.format(user_text)

def generate_text(user_text, sentiment_label=None, max_length=120, num_return_sequences=1):
    if sentiment_label is None:
        label, conf = detect_sentiment(user_text)
    else:
        label, conf = sentiment_label, None

    prompt = make_prompt(label, user_text)

    outputs = generator(
        prompt,
        max_new_tokens=200,           # use this instead of max_length for clarity
        num_return_sequences=num_return_sequences,
        temperature=0.8,              # creativity control
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,       # avoids “Do not make...” loops
        do_sample=True,
        pad_token_id=50256,           # fixes padding warning
        truncation=True
    )

    generated = []
    for output in outputs:
        gen_text = output['generated_text']
        if gen_text.startswith(prompt):
            gen_text = gen_text[len(prompt):].strip()
        generated.append(gen_text)

    return {
        'sentiment': label,
        'confidence': conf,
        'generated': generated if num_return_sequences > 1 else generated[0]
    }

if __name__ == "__main__":
    example = "I just got the internship offer and I'm super excited!"
    res = generate_text(example)
    print("Detected sentiment:", res['sentiment'], "confidence:", res['confidence'])
    print("Generated text:\n", res['generated'])
