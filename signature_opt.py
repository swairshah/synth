import dspy
from dspy.datasets import HotPotQA
from datasets import load_dataset

llm = dspy.OpenAI(model='gpt-3.5-turbo')
dspy.settings.configure(lm=llm)

dataset = HotPotQA(train_seed=1, train_size=20, eval_seed=2023, dev_size=50, test_size=0)

# %%
trainset, devset = dataset.train, dataset.dev

class CoTSignature(dspy.Signature):
    """Answer the question and give the reasoning for the same."""

    question = dspy.InputField(desc="question about something")
    answer = dspy.OutputField(desc="often between 1 and 5 words")

class CoTPipeline(dspy.Module):
    def __init__(self):
        super().__init__()

        self.signature = CoTSignature
        self.predictor = dspy.ChainOfThought(self.signature)

    def forward(self, question):
        result = self.predictor(question=question)
        return dspy.Prediction(
            answer=result.answer,
            reasoning=result.rationale,
        )

# %%
from dspy.evaluate import Evaluate

def validate_context_and_answer(example, pred, trace=None):
    answer_EM = dspy.evaluate.answer_exact_match(example, pred)
    return answer_EM

NUM_THREADS = 1
evaluate = Evaluate(devset=devset, 
                    metric=validate_context_and_answer, 
                    num_threads=NUM_THREADS, 
                    display_progress=True, 
                    display_table=False)

cot_baseline = CoTPipeline()

ds = [dspy.Example({"question": r["question"], "answer": r["answer"]}).with_inputs("question") for r in devset]

#evaluate(cot_baseline, devset=[i.with_inputs() for i in devset[:]])
evaluate(cot_baseline, devset=ds)

# %%
from dspy.teleprompt import SignatureOptimizer

teleprompter = SignatureOptimizer(
    metric=validate_context_and_answer,
    verbose=True,
)

# Used in Evaluate class in the optimization process
kwargs = dict(num_threads=64, display_progress=True, display_table=0) 

compiled_prompt_opt = teleprompter.compile(cot_baseline, devset=ds, eval_kwargs=kwargs)

# %%

from dspy.teleprompt import SignatureOptimizer

teleprompter = SignatureOptimizer(
    metric=validate_context_and_answer,
    verbose=True,
)

kwargs = dict(num_threads=64, display_progress=True, display_table=0) # Used in Evaluate class in the optimization process

compiled_prompt_opt = teleprompter.compile(cot_baseline, devset=ds, eval_kwargs=kwargs)

class CoTSignature(dspy.Signature):
    """Please answer the question and provide your reasoning for the answer. 
    Your response should be clear and detailed, explaining the rationale behind your decision. P
    lease ensure that your answer is well-reasoned and supported by relevant explanations and examples."""

    question = dspy.InputField(desc="question about something")
    reasoning = dspy.OutputField(desc="reasoning for the answer", prefix="[Rationale]")
    answer = dspy.OutputField(desc="often between 1 and 5 words")
