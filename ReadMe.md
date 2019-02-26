## haf sample

This is the sample of haf.

### haf

> https://github.com/tsbxmw/haf

> https://autotest.wang

### init your workspace with the follow command

```bash
    tsbx-mw# python -m haf init
```

### how to run ?

Open shell at haf-sample path.

```bash
    tsbx-mw# python -m haf run -c=./config.json
```

### Files

| id | file name | description |
|-----|-----|-----|
| 1 | config.json | the haf run config file |
| 2 | test1.xlsx | xlsx case template |
| 3 | test2.json | json case template |
| 4 | test3.yml | yml case template |
| 5 | test4.py | python case template|
| 6 | report/css | report css files |
| 7 | report/js | report js files |
| 8 | report/base.css | report css file |
| 9 | report/base.html | report template file |
| 10 | report | report template files | 

> config.json

the config file of haf needed

```json
{
  "config":{
    "name": "HAF",
    "run": {
      "log": {
        "log_path": "./data"
      },
      "bus": {
        "only": false,
        "host": "",
        "port": "",
        "auth_key": ""
      },
      "report": {
        "report_path": "./data/report.html",
        "report_template": "./report/base.html"
      },
      "case": [
        {
          "case_path": "./test2.json"
        },

        {
          "case_path": "./test1.xlsx"
        },

        {
          "case_path": "./test3.yml"
        },

        {
          "case_path": "./test4.py"
        }
      ],
      "runner":{
        "only": false,
        "count": 1
      },
      "loader": {
        "only": false
      },
      "recorder": {
        "only": false
      },
      "web_server": {
        "host": "",
        "port": "",
        "run": true
      }
    }
  }
}
```

