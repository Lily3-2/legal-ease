Skeleton of the directories

project_root/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── summarization.py
│   ├── translation.py
│   └── audio.py
│
├── models/
│   ├── original_pegasus/
│   │   ├── config.json
│   │   ├── pytorch_model.bin
│   │   └── tokenizer.json
│   │
│   └── fine_tuned_pegasus/
│       ├── config.json
│       ├── pytorch_model.bin
│       └── tokenizer.json
│
├── templates/
│   └── index.html
│
└── app.py