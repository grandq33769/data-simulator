## 0.4.2 (2020-12-28)

### Fix

- **simulate/time**: add "offset" args

## 0.4.1 (2020-12-24)

### Fix

- **configs/sample**: remove mypy wrong checking

## 0.4.0 (2020-12-22)

### Fix

- **config**: sample config template
- **config**: accept "str" as Environment args
- **simulator**: 1. add detailed logging\n2. add callback args\n3. accept kwargs to callback\n4. update callback kwargs after simulation
- **model**: enrich the base model

### Feat

- **simulate**: create simulate-related function
- **request**: create a generalized http request function

## 0.3.1 (2020-12-21)

### Fix

- **config**: accept "time" kwargs
- **executor**: log format
- **simulator**: give "time" args into simulate()

## 0.3.0 (2020-12-19)

### Feat

- **main**: create structure
- **exec**: create "executor" and "simulator"

### Fix

- **config**: make more sample config
- **config/sample**: add 'sample' config
- **model/et**: reconstruct the et model
- **model/et**: reconstruct the et model
- **model**: change the default value in config model
- **model**: change the default value in config model

### Refactor

- **model**: seperate "base" & "data" and add "scheduler"

## 0.1.1 (2020-12-12)

### Fix

- **model**: remove unecessary name string attribute
- **exec/validator**: use config.py instead of config.json
- **model**: remove unecessary name string attribute

### Feat

- **configs**: create config directory

## 0.1.0 (2020-12-12)

### Feat

- **model/et**: add bidding related model
- **model/et**: add env class
- **model**: add "Base" model for general function
- **validator**: construct validator template
- **model**: add "Base" model for general function
- **exec**: customerize the executor type
- **model**: add "ExecuteType" model
- **model**: add "config" related model
- **model**: add "config" related model
- **model**: add model prototype
- **model**: add model prototype
- **executor**: add "schedule" in executor
- **infra**: add "src" structure

### Fix

- **model**: seperate Base and DefaultBase
- **model/et**: remove unnecessary files
- **model**: seperate Base class and default base class
- **model**: add "get_attributes" method
- **model**: remove "attribute" script
- **model**: remove "attribute" script
