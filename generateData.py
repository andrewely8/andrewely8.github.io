import random
import pandas as pd

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

L_BOUND = -50
R_BOUND = 50

def format_linear_expr(a, b, var="x"):
    parts = []
    if a == 0:
        pass
    elif a == 1:
        parts.append(var)
    elif a == -1:
        parts.append(f"-{var}")
    else:
        parts.append(f"{a}{var}")
    if b != 0:
        if parts:
            if b > 0:
                parts.append(f"+ {b}")
            else:
                parts.append(f"- {abs(b)}")
        else:
            parts.append(str(b))
    if not parts:
        return "0"
    return " ".join(parts)


def count_solutions(a, b, c, d, op, L=L_BOUND, R=R_BOUND):
    cnt = 0
    for x in range(L, R + 1):
        left = a*x + b
        right = c*x + d
        if op == "<":
            equation = left < right
        elif op == "<=":
            equation = left <= right
        elif op == ">":
            equation = left > right
        elif op == ">=":
            equation = left >= right
        if equation:
            cnt += 1
    return cnt


def generate_one_example():
    a = random.randint(-5, 5)
    c = random.randint(-5, 5)
    b = random.randint(-10, 10)
    d = random.randint(-10, 10)

    if a == 0 and c == 0 and b == d:
        return generate_one_example()

    op = random.choice(["<=", "<", ">=", ">"])

    left_str = format_linear_expr(a, b, "x")
    right_str = format_linear_expr(c, d, "x")

    cnt = count_solutions(a, b, c, d, op, L_BOUND, R_BOUND)

    question = (
        f"For how many integers x in the range "
        f"[{L_BOUND}, {R_BOUND}] is the inequality\n\n"
        f"    {left_str} {op} {right_str}\n\n"
        f"satisfied? Answer with a single integer."
    )

    answer = str(cnt)
    boxedAnswer = "\\boxed{"+answer+"}."
    return question, boxedAnswer


def generate_dataset(n_examples):
    questions = []
    answers = []
    for _ in range(n_examples):
        q, a = generate_one_example()
        questions.append(q)
        answers.append(a)
    df = pd.DataFrame({"question": questions, "answer": answers})
    return df


df_train = generate_dataset(2000)
df_val   = generate_dataset(40)
df_test  = generate_dataset(40)

print("Train size:", len(df_train))
print("Val size:", len(df_val))
print("Test size:", len(df_test))



##This will overwrite the current data sets
#df_train.to_json("train.json", orient="records", lines=True)
# df_val.to_json("validation.json", orient="records", lines=True)
# df_test.to_json("test.json", orient="records", lines=True)
