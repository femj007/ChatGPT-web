# ChatGPT-web

**本文由ChatGPT生成初稿**

基于ChatGPT API，ChatGPT-web是一个开源的Python 3项目，它可以帮助你在浏览器中使用OpenAI的GPT-3 API。它可以帮助你在网页上快速建立一个聊天机器人来回答你的问题。

本项目提供简单的前端页面交互，支持日志记录功能。

## 安装

要安装ChatGPT-web，请确保你已经安装了Python 3.5或更高版本，并且已经安装了下列Python库：

* Flask
* requests
* openai

要安装这些库，只需在命令行输入：

```bash
pip install -r requirements.txt
```

安装完这些库之后，您需要一个OpenAI Api Key来安装ChatGPT-web。您可以在[OpenAI官网](https://openai.com)上登录并申请一个Api Key。

```bash
$ cp .env.example .env
```

然后，复制生成`.env`文件，将您的Api Key添加到`.env`文件中。

最后，运行以下命令以运行ChatGPT-web：

```bash
$ flask run
```

## 使用

运行成功将打开一个本地 web 服务器，您可以在浏览器中访问此服务器， [http://localhost:5000](http://localhost:5000)，并开始使用ChatGPT-web。