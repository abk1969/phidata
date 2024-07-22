from typing import Optional

from phi.assistant import Assistant
from phi.eval import Eval, EvalResult
from phi.llm.openai import OpenAIChat
from phi.tools.calculator import Calculator


def multiply_and_exponentiate():
    assistant = Assistant(
        llm=OpenAIChat(model="gpt-4o-mini"),
        tools=[Calculator(add=True, multiply=True, exponentiate=True)],
    )
    question = "What is 10*5 then to the power of 2? do it step by step"
    evaluation = Eval(
        assistant=assistant,
        question=question,
        ideal_answer="2500",
        save_result_to_file="evals/results/calculator/{eval_id}.json",
    )
    result: Optional[EvalResult] = evaluation.print_result()

    assert result is not None and result.accuracy_score >= 8


def factorial():
    assistant = Assistant(
        llm=OpenAIChat(model="gpt-4o-mini"),
        tools=[Calculator(factorial=True)],
    )
    question = "What is 10!?"
    evaluation = Eval(
        assistant=assistant,
        question=question,
        ideal_answer="3628800",
        save_result_to_file="evals/results/calculator/{eval_id}.json",
    )
    result: Optional[EvalResult] = evaluation.print_result()

    assert result is not None and result.accuracy_score >= 8


if __name__ == "__main__":
    multiply_and_exponentiate()
    factorial()