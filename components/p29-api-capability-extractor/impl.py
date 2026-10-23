# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P29 api-capability-extractor — 工具可供性学习

L0: 从接口文档里自动读出'这个接口要什么参数'。
L1: 正则抽取函数名与括号内参数。
L2: extract(doc) → (name, params)。
"""

import re
def extract(doc):
    m = re.search(r"(\w+)\s*\(([^)]*)\)", doc)
    if not m: return (None, [])
    params = [p.strip().split("=")[0].strip() for p in m.group(2).split(",") if p.strip()]
    return m.group(1), params

def demo():
    print("[P29]", extract("def send(url, retries=3, timeout=10)"))


if __name__ == "__main__":
    demo()
