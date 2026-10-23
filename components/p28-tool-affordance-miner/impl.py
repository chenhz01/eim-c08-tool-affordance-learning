# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P28 tool-affordance-miner — 工具可供性学习

L0: 看代码就能知道这个工具'能干什么、什么时候该用'。
L1: 从函数名+docstring 抽 动词+对象 作为可供性签名。
L2: mine(name, doc) → {'verb','object'}。
"""

def mine(name, doc):
    verbs = ["get","set","create","delete","parse","render","send","read","write","scan"]
    v = next((x for x in verbs if name.lower().startswith(x)), "use")
    obj = name.lower().replace(v, "").strip("_") or (doc.split()[0].lower() if doc else "thing")
    return {"verb": v, "object": obj}

def demo():
    print("[P28]", mine("parse_config", "Parse a config file"))


if __name__ == "__main__":
    demo()
