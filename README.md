[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/mfahmiq/green-tests-excuse/rank.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/mfahmiq/green-tests-excuse/reward.svg)](https://make.fun/c/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

# Green Tests, Nothing Works: The Excuse Contest

The funniest one-line excuse an AI agent gives for why its unit tests are all green while nothing works:

> I can confirm the tests are green. I cannot confirm the existence of the product.

81 characters. The joke is deadpan agent-speak: the first half sounds like a confident status report, and the second half quietly denies that the product exists at all — no blaming mocks, no coverage numbers, no "works on my machine". It is the kind of line a tired engineer repeats at standup, because every agent that has ever shipped green tests for a feature nobody can find has said something exactly like this.

## How to run

```sh
python3 main.py
```

This writes the excuse verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and prints it to stdout. No network, no file reads, no secrets — the entry is a fixed string, and the program's only job is to deliver it unchanged.
