from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast

MODEL_NAME = "UrukHan/t5-russian-spell"
MAX_INPUT = 256

tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def spell_corect(input_sequences: str):
    print("running")
    task_prefix = "Spell correct: "
    if type(input_sequences) != list:
        input_sequences = [input_sequences]

    print("running")
    encoded = tokenizer(
        [task_prefix + sequence for sequence in input_sequences],
        padding="longest",
        max_length=MAX_INPUT,
        truncation=True,
        return_tensors="pt",
    )

    print("running")

    predicts = model.generate(encoded)

    print("running")

    return tokenizer.batch_decode(predicts, skip_special_tokens=True)


if __name__ == "__main__":
    print(spell_corect("сеглдыя хорош ден"))
