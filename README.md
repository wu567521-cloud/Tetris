# project_name/
├── .gitignore              # Git忽略設定
├── README.md              # 專案說明與教學
├── LICENSE                 # 授權協議
├── requirements.txt       # Python依賴套件
├── src/					#
│   ├── main.py            # 入口檔案
│   ├── game_engine.py     # 遊戲核心邏輯
					1.環境處理(包含地圖旋轉旋轉,方塊切割)
						接收:2維int list
						回傳:2維int list
					2.下落 胖
						接收:2維int list; int array(單一方塊)
						回傳:2維int list; int array(單一方塊)
					3.旋轉 
						接收:2維int list; char RL
						回傳:2維int list
					4.消除 胖
						接收:2維int list ; int 分數;queue times號碼
						回傳:2維int list ; int 分數;queue times號碼
					5.方塊移動
						接收:2維int list; char RLD int array(單一方塊相同的times)
						回傳:2維int list; int array(單一方塊相同的times)
					6.存方塊
						接收:int array(單一方塊); bool(是否存)
						回傳:int array(單一方塊)
│   ├── block_handler.py   # 方塊處理
					1.方塊類型(i o...)假隨機
						接收:queue times號碼
						回傳:int a+方塊種類*10+times*10*100*10; queue times號碼
					2.特殊方塊 2:1:1
						接收:int a
						回傳:int a+特殊方塊 
					3.方塊顏色 (16色)
						接收:int a
						回傳:int a+方塊顏色*10*100
					4.方塊合併與切割
						接收:int a;2維int list
						回傳:int a;2維int list
  					a存int list
					a=times(3位)/方塊顏色(2位)/方塊種類(1位)/特殊方塊(1位)
│   └── ui.py              # UI層面
					1.遊戲開始畫面(20*10)
					2.方塊呈現
					3.音效
					4.分數
					5.整體框架
├── assets/                # 圖片、音效等資源
├── docs/                  # 設計文件與說明
├── tests/                 # 測試檔案
├── config.yaml            # 配置文件
└── VERSION.txt            # 版本號
