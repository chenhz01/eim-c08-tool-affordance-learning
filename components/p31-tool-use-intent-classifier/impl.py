# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P31 tool-use-intent-classifier — 工具可供性学习

L0: 听用户说什么，猜他要用哪个工具。
L1: 关键词重叠度打分，取最高分工具。
L2: classify(text, tools) → (tool, score)。
"""

def classify(text, tools):
    t = set(text.lower().split())
    best, bs = None, 0.0
    for name, kw in tools.items():
        s = len(t & set(kw)) / max(1, len(set(kw)))
        if s > bs: best, bs = name, s
    return best, round(bs, 2)

def demo():
    print("[P31]", classify("please deploy the app", {"deploy":["deploy","release"], "test":["test","check"]}))


if __name__ == "__main__":
    demo()
