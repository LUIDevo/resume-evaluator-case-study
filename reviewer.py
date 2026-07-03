import json
import os

from anthropic import Anthropic

client = Anthropic()

RUNS = 10
OUTPUT_DIR = "outputs"

with open("resume_sys_prompt.txt", "r") as file:
    system_prompt=file.read()

with open("./resumes/resume_max.txt", "r") as file:
    resume=file.read()

os.makedirs(OUTPUT_DIR, exist_ok=True)

for i in range(1, RUNS + 1):
    # Create a message request
    message = client.messages.create(
        model="claude-sonnet-5",  # Chosen model, ideal for efficiency and intelligence
        max_tokens=4096,
        system=system_prompt,
        messages=[
            {"role": "user", "content": resume}
        ]
    )

    text = "".join(block.text for block in message.content if block.type == "text")

    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]

    try:
        text = json.dumps(json.loads(text), indent=2)
    except json.JSONDecodeError:
        pass

    out_path = os.path.join(OUTPUT_DIR, f"run_{i:02d}.txt")
    with open(out_path, "w") as out_file:
        out_file.write(text)

    print(f"[{i}/{RUNS}] wrote {out_path}", flush=True)

    if message.stop_reason == "max_tokens":
        print(f"[warning] run {i} output truncated: hit max_tokens", flush=True)
