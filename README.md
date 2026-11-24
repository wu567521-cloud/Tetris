# Project Structure

```text
project_name/
├── .gitignore              # Git 忽略設定
├── README.md               # 專案說明與教學
├── LICENSE                 # 授權協議
├── requirements.txt        # Python 依賴套件
├── src/
│   ├── main.py             # 入口檔案
│   ├── game_engine.py      # 遊戲核心邏輯
│   ├── block_handler.py    # 方塊處理
│   └── ui.py               # UI 層面
├── assets/                 # 圖片、音效等資源
├── docs/                   # 設計文件與說明
├── tests/                  # 測試檔案
├── config.yaml             # 配置文件
└── VERSION.txt             # 版本號
```

---

# 1. game_engine.py

負責遊戲核心邏輯。

## 1.1 環境處理

包含地圖旋轉、方塊切割等環境處理。

- **接收：** `2維 int list`
- **回傳：** `2維 int list`

## 1.2 方塊下落

- **接收：** `2維 int list`、`int array（單一方塊）`
- **回傳：** `2維 int list`、`int array（單一方塊）`

## 1.3 方塊旋轉

- **接收：** `2維 int list`、`char（R / L）`
- **回傳：** `2維 int list`

## 1.4 方塊消除

- **接收：** `2維 int list`、`int（分數）`、`queue（times 號碼）`
- **回傳：** `2維 int list`、`int（分數）`、`queue（times 號碼）`

## 1.5 方塊移動

- **接收：** `2維 int list`、`char（R / L / D）`、`int array（單一方塊相同的 times）`
- **回傳：** `2維 int list`、`int array（單一方塊相同的 times）`

## 1.6 方塊存取

- **接收：** `int array（單一方塊）`、`bool（是否存）`
- **回傳：** `int array（單一方塊）`

---

# 2. block_handler.py

負責方塊類型、特殊屬性、顏色及資料處理。

## 2.1 方塊類型（I、O 等，假隨機）

- **接收：** `queue（times 號碼）`
- **回傳：**
  - `int a`（方塊編碼）
  - `queue（times 號碼）`

方塊編碼：

```text
a + 方塊種類 * 10 + times * 10 * 100 * 10
```

## 2.2 特殊方塊（2:1:1）

- **接收：** `int a`
- **回傳：** `int a + 特殊方塊`

## 2.3 方塊顏色（16 色）

- **接收：** `int a`
- **回傳：** `int a + 方塊顏色 * 10 * 100`

## 2.4 方塊合併與切割

- **接收：** `int a`、`2維 int list`
- **回傳：** `int a`、`2維 int list`

## 2.5 方塊資料編碼

`a` 儲存為 `int`，其資料結構如下：

| 資料 | 位數 |
|---|---:|
| times | 3 位 |
| 方塊顏色 | 2 位 |
| 方塊種類 | 1 位 |
| 特殊方塊 | 1 位 |

---

# 3. ui.py

負責使用者介面（UI）及遊戲呈現。

## 3.1 遊戲開始畫面

- 畫面尺寸：20 × 10

## 3.2 方塊呈現

- 顯示遊戲中的方塊。

## 3.3 音效

- 負責遊戲音效播放。

## 3.4 分數

- 顯示目前遊戲分數。

## 3.5 整體框架

- 負責整合各 UI 元件。
- 呈現完整遊戲畫面。

---

# 4. 其他專案目錄

| 檔案／目錄 | 用途 |
|---|---|
| `.gitignore` | 設定 Git 忽略的檔案 |
| `README.md` | 專案說明與教學 |
| `LICENSE` | 專案授權協議 |
| `requirements.txt` | Python 依賴套件 |
| `assets/` | 圖片、音效等資源 |
| `docs/` | 設計文件與說明 |
| `tests/` | 測試檔案 |
| `config.yaml` | 遊戲配置 |
| `VERSION.txt` | 專案版本號 |
