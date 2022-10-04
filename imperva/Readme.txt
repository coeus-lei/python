1.config.py 修改配置文件
        api_id      账号对应api_id
        api_key     账号对应api_key
        account_id  账号对应account_id
        site_ip     账号对应原站ip
2.domain.txt 文件添加域名
        域名格式www.domian.com
3.ssl目录放入对应域名crt,key文件，文件格式为：
        domain_chain.crt
        domain_key.key
4.GetSiteStatus.py获取账号下对应域名A记录以及CNAME
运行方式：   1.添加域名              python main.py
            2.获取账号CDN记录       python GetSiteStatus.py
