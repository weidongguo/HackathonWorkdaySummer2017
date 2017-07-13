# HackathonWorkdaySummer2017

## Post message to a channel
https://api.slack.com/incoming-webhooks
To post message to a channel through a webhook, one can do

```
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' <WEBHOOK_URL>
```

whereas <WEBHOOK_URL> is a webhook url for a channel.
This URL has to be registered in your slack app.

For example
```
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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
```

## Add Reaction to a message
https://api.slack.com/methods/reactions.add