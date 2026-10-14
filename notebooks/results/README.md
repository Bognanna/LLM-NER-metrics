# Results directory

## Structure
├───benchmark               # Results of running tests on benchmark datasets. For each embedding model results are stored in separate directory.
│   ├───embeddinggemma      # Results of running tests with embeddinggemma model.
│   │   ├───detailed        # ...
│   │   └───summary
│   ├───granite-embedding   # Results of running tests with granite-embedding model.
│   │   ├───detailed
│   │   └───summary
│   ├───mxbai-embed-large   # Results of running tests with mxbai-embed-large model.
│   │   ├───detailed
│   │   └───summary
│   ├───nomic-embed-text    # Results of running tests with nomic-embed-text model.
│   │   ├───detailed
│   │   └───summary
│   ├───qwen3-embedding     # Results of running tests with qwen3-embedding model.
│   │   ├───detailed
│   │   └───summary
│   └───snowflake-arctic-embed  # Results of running tests with snowflake-arctic-embed model.
│       ├───detailed
│       └───summary
└───use cases               # Results of running tests on use cases. Each use case file contain results for all testes embedding models.

