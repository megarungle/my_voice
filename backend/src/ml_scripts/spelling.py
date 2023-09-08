import torch

from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast

MODEL_NAME = "UrukHan/t5-russian-spell"
MAX_INPUT = 256

tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


def correct_spelling(input_phrase: str) -> str:
    encoded = tokenizer(
        [f"Spell correct: {input_phrase}"],
        padding="longest",
        max_length=MAX_INPUT,
        truncation=True,
        return_tensors="pt",
    )

    predicts = model.generate(**encoded.to(device))
    res = tokenizer.batch_decode(predicts, skip_special_tokens=True)
    return res[0].lower()


if __name__ == "__main__":
    test_inputs = {"сеглдыя хорош ден": "сегодня хорош день.", "когд а вы прдет к нам в госи": "когда вы придете к нам в гости?"}
    for key, val in test_inputs.items():
        res = correct_spelling(key)
        print(res)
        assert res == val
