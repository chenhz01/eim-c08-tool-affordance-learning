# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P30 self-tool-forge — 工具可供性学习

L0: 缺什么工具就现场造一个能跑的小函数。
L1: 按 (name, params, body) 生成可执行 Python 源码字符串。
L2: forge(name, params, body) → 源码。
"""

def forge(name, params, body):
    ps = ", ".join(params)
    lines = [f"def {name}({ps}):"] + ["    " + l for l in body.strip().splitlines()] or ["    pass"]
    return "\n".join(lines)

def demo():
    src = forge("add", ["a","b"], "return a + b")
    ns = {}; exec(src, ns)
    print("[P30]", ns["add"](2, 3))


if __name__ == "__main__":
    demo()
