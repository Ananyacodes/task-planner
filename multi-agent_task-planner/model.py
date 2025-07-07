from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model(model_choice="7b"):
    """Load model with automatic configuration based on available hardware"""
    model_id = f"tiiuae/falcon-{model_choice}-instruct"
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            model_id,
            trust_remote_code=True,
            padding_side="left"
        )
        tokenizer.pad_token = tokenizer.eos_token

        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            trust_remote_code=True,
            torch_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
            device_map="auto",
            load_in_4bit=True,
            low_cpu_mem_usage=True
        )
        
        print(f"✅ Successfully loaded {model_id}")
        return tokenizer, model
        
    except Exception as e:
        print(f"⚠️ Error loading {model_choice} model: {str(e)}")
        if model_choice != "7b":
            print("🔄 Falling back to Falcon-7B...")
            return load_model("7b")
        raise RuntimeError("Failed to load any model version")

# Initialize with best available option
try:
    tokenizer, model = load_model("40b")  # Try 40B first
except RuntimeError:
    print("❌ No suitable model could be loaded")
    exit(1)