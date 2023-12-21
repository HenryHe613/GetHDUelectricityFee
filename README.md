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

>注意，Bot现在只能在内部群中使用，所以可以给室友建一个群，归属于思政平台或者“早安·卓裂”。

寝室查电费的网页如下：[URL](https://wap.xt.beescrm.com/base/electricity_hd/index/ele_id/7)，请选择自己的楼、楼层、房间，然后查询。此时不要退出，把URL复制下来，删掉https，改为http，就是所需的URL。

4. 等着吧，默认21:30自动运行脚本。或者可以到Action中手动运行测试看看。

## 鸣谢

感谢[@headmasteryang](https://t.me/headmasteryang)提供电费查询算法