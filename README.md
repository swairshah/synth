# synth

## Approach 1.

Raw data -> data-instructdata model -> filter

* prompt2model : [https://arxiv.org/abs/2308.12261](https://arxiv.org/abs/2308.12261)

* genstruct-7b: [https://huggingface.co/BatsResearch/bonito-v1](https://huggingface.co/NousResearch/Genstruct-7B)

* bonito: [https://huggingface.co/BatsResearch/bonito-v1
](https://huggingface.co/BatsResearch/bonito-v1)
## Approach 2.

dspy seed examples -> singature optimization with human input 

## Approach 3.

Custom prompt (p_0) + custom examples + custom eval prompt

```
while (n_loop < iter_limit or selection_rate < threshold):
1. Given a base prompt p_i (+ a few seed example, generate a sample
2. Ask evaluator in the loop to select/reject them
3. run evaluator prompt to modify prompt to get p_{i+1}
```

* Automatic Prompt Optimization with "Gradient Descent" and Beam Search https://arxiv.org/abs/2305.03495
* Promptbreeder : https://arxiv.org/abs/2309.16797
