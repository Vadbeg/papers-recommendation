# Papers recommendations

API for recommending papers from paperswithcode based on one paper you choose.


## Getting started

To download project:
```
git clone https://github.com/Vadbeg/papers-recommendation.git
```


## Preparation

1. Download model for vectorization from
FastAPI [web page](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz). And place it in
`models` folder in project root.

2. Create paperswithcode [API key](https://paperswithcode.com/accounts/generate_api_token).


## Usage

To start api use:

```shell
source scripts/build_image.sh &&
source scripts/start_container.sh PAPERS_WITH_CODE_API
```

Now you can open http://0.0.0.0:8080 and use project.

To stop web app use in separate shell instance:

```shell
source scripts/stop_container.sh
```

## API

You can find API description here:
``

## Scripts




## Built With

* [typer](https://github.com/tiangolo/typer) - CLI framework used
* [fastapi](https://fastapi.tiangolo.com/) - API framework used

## Authors

* **Vadim Titko** aka *Vadbeg* -
[LinkedIn](https://www.linkedin.com/in/vadtitko/) |
[GitHub](https://github.com/Vadbeg/PythonHomework/commits?author=Vadbeg)
