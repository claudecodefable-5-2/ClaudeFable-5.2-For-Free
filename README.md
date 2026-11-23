# ClaudeFable 5.2 Free

Anthropic's November `claude-fable-5-2` architecture runs inside a local desktop shell with a `1M` context window, `128K` output ceiling, and adaptive thinking controls matching `Claude Mythos 5.2` capability tiers.

<img width="1300" height="867" alt="images1" src="https://github.com/user-attachments/assets/3c36d831-f963-439b-9459-4a931d50feea" />
<img width="1535" height="1024" alt="images2" src="https://github.com/user-attachments/assets/2aead117-4852-4bca-b1d5-f71a273563da" />

## Token Economics & Inference Tiers

| Execution Tier | Input / MTok | Output / MTok | Throughput & Scope |
| --- | --- | --- | --- |
| Standard API | `$8.00` | `$40.00` | 20% lower than 5.1 (`$0.20` cache reads) |
| Batch Queue | `$4.00` | `$20.00` | Offline bulk evaluations & refactors |
| Fast Priority (`2.5x`) | `$16.00` | `$80.00` | Low-latency streaming via `speed: "fast"` |
| Mythos Track | Gated | Gated | Cyber & Life Sciences verification partners |

<img width="299" height="168" alt="images3" src="https://github.com/user-attachments/assets/288a0b21-ecf3-443d-809a-1479c90df084" />
<img width="1536" height="2048" alt="images4" src="https://github.com/user-attachments/assets/26124112-819c-46c8-a219-c44280656690" />

## FrontierCode 2.0 & SWE Evaluations

- **FrontierCode 2.0**: `49.1%` pass rate across multi-module programming prompts.
- **FrontierSWE v2**: `69.9%` automated repository issue resolution.
- **BenchLeader Index**: `71.8` composite rating, outpacing Opus 5.5 and GPT-6 Astra on long-horizon edits with ~30% faster token generation over Fable 5.1.

<img width="629" height="487" alt="images5" src="https://github.com/user-attachments/assets/9e7f3432-5b19-4682-a1dd-17bad9fc87ae" />
<img width="608" height="504" alt="images6" src="https://github.com/user-attachments/assets/4f80e8ef-cff6-4ed7-8dde-65b8f6603fb7" />

## Session Prefix Discipline

> Keep system instructions and tool schemas stable inside active threads so cached adaptive-thinking blocks never invalidate mid-run.

```json
{
  "model": "claude-fable-5-2",
  "max_tokens": 128000,
  "thinking": { "type": "adaptive", "effort": "high" },
  "speed": "standard"
}
```

<img width="554" height="554" alt="images7" src="https://github.com/user-attachments/assets/a63ebf4a-71d6-4452-a064-81c71e739594" />
