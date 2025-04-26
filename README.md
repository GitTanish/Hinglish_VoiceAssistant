# Hinglish Voice-AI Fine-Tuning

## 📖 Background
This project fine-tunes an OpenAI model to handle Hinglish (Hindi + English) conversational inputs.

## 🛠️ Setup Instructions
1. Clone the repo.
2. Prepare environment:
    ```bash
    pip install -r requirements.txt
    ```
3. Set OpenAI API Key:
    ```bash
    export OPENAI_API_KEY="sk-xxxxxxxxxx"
    ```
4. Run scripts:
    ```bash
    python fine_tune.py
    python inference.py
    ```

## 🎯 Project Details

### Dataset
- Focused on casual, daily life conversations.
- 10 examples to keep it lightweight for quick fine-tuning.
- Short, natural prompts with simple completions.

### Model
- **gpt-3.5-turbo** chosen for affordability and speed.
- Fine-tuned models adapt well even with small datasets.

### Fine-tuning Parameters
- **Epochs**: 2 (default) — enough for a small dataset.
- **Learning Rate**: Default settings.

### Inference Settings
- Format: "User: [input] \n Assistant:"
- Temperature: Default (no extra randomness).

### Evaluation
- Human inspection based: checking if assistant replies naturally to Hinglish inputs.

## 🧪 Sample Inference Output

```plaintext
User: Mujhe ek chai pilao.
Assistant: Zarur! Ek garam chai abhi laata hoon.

User: Aaj mausam kaisa hai?
Assistant: Mausam aaj kaafi pleasant hai, halka sa thanda.

User: Kal Sunday hai na?
Assistant: Haan, kal Sunday hai. Kya plans hain?
