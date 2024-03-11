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
Custom prompt + custom examples + custom eval prompt

----
read

https://evjang.com/2023/03/26/self-reflection.html

https://nanothoughts.substack.com/p/reflecting-on-reflexion

https://drchrislevy.github.io/posts/dspy/dspy.html

https://kanav-ai.notion.site/DSPy-6f508d1db80542278ee0d6a94676e1ca

https://gist.github.com/cfcosta/05b1ccd898e1fb8fd5b93bc01916e66a

https://hamel.dev/blog/posts/prompt/
