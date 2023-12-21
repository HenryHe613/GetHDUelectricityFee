# 自动获取HDU的寝室电费

通过钉钉内部群Bot自动推送

## 使用方法

1. fork该项目

2. 进入`repo`的`settings`->`Secrets and variables`->`Actions`->`Repository secrets`

3. 新建`secret`，内容分别是

| Name | Secret |
| ---- | ------- |
| SECRET | 你在钉钉Bot中获得的secret |
| TOKEN | 钉钉Bot中获得的access_token |
| URL | 你的寝室的查电费网页（需http，非https） |

