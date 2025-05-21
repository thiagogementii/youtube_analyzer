from transformers import pipeline

def summarize_text(text: str) -> str:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=200, min_length=30, do_sample=False)
    return summary[0]['summary_text']
