# P29 · api-capability-extractor

> 机制簇：**工具可供性学习** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
从接口文档里自动读出'这个接口要什么参数'。

**L1 · 机制本质**
正则抽取函数名与括号内参数。

**L2 · 怎么用上**
extract(doc) → (name, params)。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P29] ('send', ['url', 'retries', 'timeout'])
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 工具数量多、文档缺失或过期、需要自动发现「这工具到底能干什么」。 |
| **不该用** | 工具集固定且文档完备、调用契约稳定的系统。 |
| **常见误用** | 把「跑通过一次」当可供性——没验证前置条件与副作用，换个输入就崩。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P28` tool-affordance-miner · `P30` self-tool-forge · `P31` tool-use-intent-classifier
- 本仓是 **P29 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P29-api-capability-extractor/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P29 · api-capability-extractor © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
