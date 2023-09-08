import torch

from typing import List

from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast

MODEL_NAME = "UrukHan/t5-russian-spell"
MAX_INPUT = 256

tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


def spell_correct(input_sequences: List[str]) -> List[str]:
    task_prefix = "Spell correct: "
    if type(input_sequences) != list:
        input_sequences = [input_sequences]

    encoded = tokenizer(
        [task_prefix + sequence for sequence in input_sequences],
        padding="longest",
        max_length=MAX_INPUT,
        truncation=True,
        return_tensors="pt",
    )

    predicts = model.generate(**encoded.to(device))
    res = tokenizer.batch_decode(predicts, skip_special_tokens=True)
    res = [result.lower() for result in res]

    return res


if __name__ == "__main__":
    input_sequences = ["сеглдыя хорош ден", "когд а вы прдет к нам в госи"]
    res = spell_correct(input_sequences)
    print(res)
    assert res == ["сегодня хорош день.", "когда вы придете к нам в гости?"]
