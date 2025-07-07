from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "sshleifer/tiny-gpt2"  # Lightweight model for CPU

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True
)

# Load generation pipeline
text_gen = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)

def generate_text(prompt: str) -> str:
    """Generates text using the model pipeline."""
    output = text_gen(prompt)[0]["generated_text"]
    return output[len(prompt):].strip()  # return only the generated part

print("✅ Tiny GPT-2 model loaded")
