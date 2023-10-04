# qq_group_member_extract
用于根据聊天记录导出群成员名单（适用于群被封了的情况）

有时候群突然被封了，然后群里还有好友没加就有可能出现失联的情况。

不过你先别急着退群，用我的这个脚本可以根据聊天记录直接导出群成员名单。


### ✨使用说明

1. 登录PC版QQ，点击左下角的三条杠，打开消息管理器。
2. 点击群聊，在列表中找到想要导出成员名单的群（被封的群只要没退群在这里也可以找到）
3. 右键群名，点击导出消息记录。
4. 保存类型选择`文本文件txt`，点击保存，等待导出完成。导出完成后可以看到一个以群名命名的txt文件。
5. 在[release页面](https://github.com/Zhaokugua/qq_group_member_extract/releases)下载可执行文件的压缩包，或者直接下载源代码py文件。压缩包全部解压缩之后直接双击运行，py文件使用命令`python qq_group_member_extract.py`命令运行。
6. 将导出的聊天记录复制或者剪切到和程序相同路径（文件夹），并重命名为`聊天记录.txt`或者直接把文件拖到程序里面，然后敲下回车。
7. 程序会自动运行并生成群成员名单的json文件，包含聊天记录中所有曾经用过的群名片。


### 🌈使用预览
聊天记录文件`聊天记录（测试用）.txt`：
```txt
消息记录（此消息记录为文本格式，不支持重新导入）

================================================================
消息分组:我创建的群聊
================================================================
消息对象:测试群组
================================================================

2022-04-26 13:00:12 系统消息(1000000)
[图片]你已经成功创建群聊，马上邀请你的好友加入吧。

2022-04-26 13:58:09 我是喵喵(123456789)
[图片]

2022-04-26 13:58:44 赵苦瓜(1234554321)
没设置好系统代理

2022-04-26 13:59:48 赵苦瓜(1234554321)
点fiddler那个黄色的看看

2022-04-26 14:00:35 我是喵喵(123456789)
[图片]

2022-04-26 14:02:48 我是狗子(987654321)
NB！

2022-04-26 14:02:58 赵苦瓜(1234554321)
[图片]

2022-04-26 14:03:34 我不是喵喵(123456789)
[图片]

2022-04-26 14:03:34 我就是喵喵(123456789)
OK

2022-04-26 14:03:40 赵苦瓜(1234554321)
好
```
运行中展示：
```shell
F:\Python\群成员提取\dist\群成员提取（改进版）>群成员提取（改进版）.exe 
请把聊天记录文件重命名为“聊天记录.txt”并放在和程序同路径或者直接拖到这里然后敲回车：F:\\Python\\群成员提取\\dist\\群成员提取（改进版）\\聊天记录（测试用）.txt
[('系统消息', '1000000')]
[('我是喵喵', '123456789')]
[('赵苦瓜', '1234554321')]
[('赵苦瓜', '1234554321')]
[('我是喵喵', '123456789')]
[('我是狗子', '987654321')]
[('赵苦瓜', '1234554321')]
[('我不是喵喵', '123456789')]
[('我就是喵喵', '123456789')]
[('赵苦瓜', '1234554321')]
```
运行结果展示`聊天记录（测试用）.txt __result.json`：
```json
{
  "1000000": [
    "系统消息"
  ],
  "123456789": [
    "我是喵喵",
    "我不是喵喵",
    "我就是喵喵"
  ],
  "1234554321": [
    "赵苦瓜"
  ],
  "987654321": [
    "我是狗子"
  ]
}
```
