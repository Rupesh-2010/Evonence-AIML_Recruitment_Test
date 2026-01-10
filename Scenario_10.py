# Scenario 10: Summarization with Constraints
# Task: Write a prompt to summarize a news article into 2 sentences.
# If the summary exceeds 50 words, truncate it to the nearest complete sentence.

#####################################    ANSWER      #####################################


def constrained_summary_prompt(article_text):       # Created Function.

    # Create instruction for model to return only 2 sentences
    prompt = (
        "Summarize the following news article into exactly 2 sentences. "
        "Be concise, factual, and avoid opinions.\n\n"
        f"ARTICLE:\n{article_text}\n\n"
        "OUTPUT: Provide only the 2-sentence summary."
    )
    return prompt                # Send prompt to model


def truncate_to_50_words(summary):

    words = summary.strip().split()     # Break summary into words

    if len(words) <= 50:            # If already under limit

        return summary.strip()

    import re  # Used for sentence split

    sentences = re.split(r'(?<=[.!?])\s+', summary.strip())       # Split text into sentences

    truncated = []  # Store final lines
    total = 0       # Track word count

    # Add sentences until limit
    for s in sentences:
        count = len(s.split())
        if total + count <= 50:
            truncated.append(s)
            total += count
        else:
            break

    # Join and return result
    return " ".join(truncated).strip()


# Example article
article = "Python continues to gain traction in data science due to its simplicity, extensive libraries, and strong community support..."

# Build prompt for model
prompt = constrained_summary_prompt(article)

# Fake model response
model_output = "Python is widely used in data science for its readability and rich libraries. Its community and tooling accelerate experimentation and deployment."

# Print truncated summary
print(truncate_to_50_words(model_output))

