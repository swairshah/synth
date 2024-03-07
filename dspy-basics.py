import re
import dspy 
from ui.styles import * 
from ui.dialog import *

llm = dspy.OpenAI(model="gpt-3.5-turbo-0125", max_tokens=250)
# llm.basic_request("this is a test")
# llm.inspect_history()

# %%
dspy.settings.configure(lm=llm)

# %%
predict = dspy.Predict('question -> name')
response = predict(question="who killed JFK?")

# %%
from datasets import load_dataset
ds = load_dataset("maveriq/bigbenchhard", "penguins_in_a_table")["train"]
examples = [dspy.Example({"question": r["input"], "answer": r["target"]}).with_inputs("question") for r in ds]

valset = examples[0:5]
trainset = examples[20:]

# %%
from dspy.evaluate import Evaluate
from prompt_toolkit.shortcuts import yes_no_dialog

def user_eval(true, prediction, trace=None):
    pred = prediction.answer
    text=f"\nQUESITON: {true['question']}\nANSWER: {true['answer']}\n\nPREDICTION: {pred}\n\nIs this correct?"
    #ask_question(text)
    result = yes_no_dialog(
            title='Evaluate: ',
            text = text,
            style=bw_style,
    ).run()
    return result

def eval_metric(true, prediction, trace=None):
    pred = prediction.answer
    matches = re.findall(r"\([A-Z]\)", pred)
    parsed_answer = matches[-1] if matches else ""
    return parsed_answer == true.answer

evaluate = Evaluate(devset=valset, metric=user_eval, num_threads=1, display_progress=True, display_table=10)

# %%

class BasicQA(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.Predict("question -> answer")

    def forward(self, question):
        return self.prog(question=question)


basic_qa = BasicQA()
evaluate(basic_qa)
