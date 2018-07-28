# slack-dump
Dump the raw data from your slack team.

## Usage
1. Visit a slack website,
https://api.slack.com/custom-integrations/legacy-tokens
and get your Legacy token.

2. Set your os enviroment variable

```
$ export SLACK_USER_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXx
```

3. Run dump.py in background.

```
$ nohup python3 dump.py &
```
