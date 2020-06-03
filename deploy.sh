# 在部署环境下，执行该脚本进行部署
# centos7实测可用
nohup scrapyd > scrapyd.log &
nohup scrapyd-deploy > deploy.log &