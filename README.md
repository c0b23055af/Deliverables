# AI simulation

このリポジトリには、以下の3つのゲームにおいてAIの戦略を比較・評価するためのPythonシミュレーターが含まれています：

- Connect Four
- Minesweeper
- Tic-Tac-Toe (〇×ゲーム)

---

## Connect4.py

コネクトフォー（四目並べ）における2つの異なるAI戦略を、**限られた探索深度のMin-Maxアルゴリズム**を用いて比較するためのシミュレーターです。

- **BestAI**：攻撃的な評価関数を持つAI
- **testAI**：保守的な評価関数を持つAI（ベースライン）

本プロジェクトでは、testAIに対する勝率を最大化するようにBestAIをチューニングし、結果として攻撃的な評価関数を用いることで高い勝率を達成できました。

---

## Minesweeper.py

マインスイーパーを**自動でプレイするAI**の性能を評価するためのシミュレーターです。

- 特定の戦略ロジックに基づいたAIを実装
- 複数回のプレイを通じて勝率を統計的に分析

安全なマスを推定し、可能な限り確実に進めるよう設計されています。

---

## TicTacToe_MinMax.py

〇×ゲームにおいて、**Min-Maxアルゴリズムで動作する完璧なAI**と、**ランダムに手を打つAI**を対戦させるシミュレーターです。

- Min-Max法の有効性を定量的に示すための実験
- 完璧な戦略がランダム戦略に対してどれほど優位に立てるかを観察可能

このプログラムを通して、Min-Maxアルゴリズムの強力さを直感的かつ統計的に理解することができます。

---

## 実行方法

いずれもPython 3で動作します。必要に応じて以下のように実行してください。

```bash
python Connect4.py
python Minesweeper.py
python TicTacToe_MinMax.py
