# C08 · Tool Affordance Learning

> **机制簇**：工具可供性学习 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
AI 不该靠猜「这个按钮能不能点」，而是从代码里读出工具真正能干什么、边界在哪。

**L1 · 机制本质**
从签名、文档、调用点静态推断前置条件与副作用，产出 affordance 卡片；失败调用反哺修正。

**L2 · 怎么用上**
affordance-extractor 静态抽取；precondition-inferrer 推前置条件；failure-feedback 回写修正。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c08-tool-affordance-learning.git && cd eim-c08-tool-affordance-learning
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p28-tool-affordance-miner/impl.py        # 看 demo 输出
python components/p28-tool-affordance-miner/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P28` | tool-affordance-miner | 从函数名+docstring 抽 动词+对象 作为可供性签名。 | `components/p28-tool-affordance-miner/` |
| `P29` | api-capability-extractor | 正则抽取函数名与括号内参数。 | `components/p29-api-capability-extractor/` |
| `P30` | self-tool-forge | 按 (name, params, body) 生成可执行 Python 源码字符串。 | `components/p30-self-tool-forge/` |
| `P31` | tool-use-intent-classifier | 关键词重叠度打分，取最高分工具。 | `components/p31-tool-use-intent-classifier/` |

## 该用 / 不该用 / 常见误用

**该用**
工具/API 数量多、文档不全的智能体；自动生成的工具集。

**不该用**
工具集极小且文档完整清晰（读文档更快）。

**常见误用（这条最重要）**
把「能调用成功」当作「可安全调用」。权限、副作用与成本是另外一层。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C08 · Tool Affordance Learning © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
