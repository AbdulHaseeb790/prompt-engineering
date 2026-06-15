# Prompt Engineering Fundamentals

A beginner-to-advanced collection of prompt engineering techniques used with Large Language Models (LLMs) such as GPT, Claude, Llama, Gemini, and others.

This repository contains practical examples, explanations, and mini-projects to help developers learn how to communicate effectively with AI models.

---

# Topics Covered

## 1. Zero-Shot Prompting

Zero-shot prompting means giving the model a task without providing any examples.

### Example

```text
Translate the following sentence into French:

Hello, how are you?
```

### Use Cases

* Simple Q&A
* Summarization
* Translation
* Text generation

### Advantages

* Fast and simple
* Requires minimal setup

### Limitations

* Less reliable for complex tasks
* Output format may vary

---

## 2. Few-Shot Prompting

Few-shot prompting provides examples before asking the model to perform a task.

### Example

```text
English: Hello
French: Bonjour

English: Good Morning
French: Bonjour

English: Thank You
French:
```

### Use Cases

* Classification
* Data extraction
* Consistent formatting
* Specialized tasks

### Advantages

* Improves accuracy
* Helps control output style

### Limitations

* Uses more tokens
* Requires quality examples

---

## 3. Chain of Thought Prompting

Chain of Thought (CoT) prompting encourages the model to reason step-by-step before producing the final answer.

### Example

```text
A shop sells pencils for $2 each.

If Ali buys 4 pencils, how much does he pay?

Think step by step.
```

### Output

```text
Each pencil costs $2.

Ali buys 4 pencils.

Total cost = 4 × 2

Total cost = $8
```

### Use Cases

* Mathematics
* Logical reasoning
* Decision-making tasks

### Benefits

* More accurate reasoning
* Easier debugging of model outputs

---

## 4. System Prompt Design

A system prompt defines the model's behavior, personality, and rules.

### Example

```text
You are an expert Python instructor.

Explain concepts in simple language.

Always provide examples.
```

### Purpose

System prompts help:

* Control model behavior
* Maintain consistency
* Define expertise level
* Enforce output rules

---

## 5. Prompt Templates

Prompt templates allow dynamic insertion of variables into prompts.

### Example

```python
template = """
You are a {role} assistant.

Answer the following question:

{question}
"""
```

### Variables

```python
role = "Python Teacher"

question = "What is a list in Python?"
```

### Final Prompt

```text
You are a Python Teacher assistant.

Answer the following question:

What is a list in Python?
```

### Benefits

* Reusable prompts
* Easier maintenance
* Dynamic applications

---

## 6. Common Prompt Engineering Mistakes

### Mistake 1: Being Too Vague

Bad Prompt

```text
Tell me about Python.
```

Better Prompt

```text
Explain Python lists for beginners with three examples.
```

---

### Mistake 2: Missing Context

Bad Prompt

```text
Write code.
```

Better Prompt

```text
Write a Python function that calculates factorial using recursion.
```

---

### Mistake 3: Not Specifying Output Format

Bad Prompt

```text
Analyze this data.
```

Better Prompt

```text
Analyze this data and return the result as a Markdown table.
```

---

### Mistake 4: Overloading a Single Prompt

Bad Prompt

```text
Explain Python, create a project, teach OOP, and build a website.
```

Better Prompt

Break large tasks into smaller prompts.

---

## 7. Mini Project — Prompt Template Engine

### Project Goal

Build a simple prompt template engine that dynamically generates prompts.

### Features

* User-defined templates
* Variable replacement
* Multiple prompt types
* Reusable prompt storage

### Example

Template

```text
You are a {role} assistant.

Question:
{question}
```

Input

```python
{
    "role": "Chef",
    "question": "How do I make pasta?"
}
```

Generated Prompt

```text
You are a Chef assistant.

Question:
How do I make pasta?
```

### Skills Learned

* Prompt Engineering
* String Formatting
* Template Systems
* LLM Application Design

---

# Learning Outcomes

After completing this repository, you will understand:

* Zero-Shot Prompting
* Few-Shot Prompting
* Chain of Thought Prompting
* System Prompt Design
* Prompt Templates
* Prompt Optimization
* Real-World Prompt Engineering Techniques

---

# Author

**Abdul Haseeb**
Software Engineering Student | AI Developer | Future Agentic AI Engineer
