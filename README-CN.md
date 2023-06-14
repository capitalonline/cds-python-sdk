简体中文|[English](README.md)

<p align="center">
<a href=" https://www.alibabacloud.com"><img src="https://www.capitalonline.net/templets/default/icon/logo_header.png"></a>
</p>

# CapitalOnline Cloud SDK for python

欢迎使用`CapitalOnline Cloud SDK for python`，它可以管理[首都在线](https://www.capitalonline.net)多个全球服务，如首云全球云服务器、首云块存储、首云全球互通网络等，帮您轻松管理所有在线资源。基于首云官方[OpenAPI文档](https://github.com/capitalonline/openapi/blob/master/README.md)

# 功能特点

您可以通过SDK管理各种中资源，[这里](https://github.com/capitalonline/openapi/blob/master/%E9%A6%96%E4%BA%91OpenAPI(v1.2).md)可以看到所有可用接口清单。下面列出部分接口列表：

- [x] 实例管理
  - [x] CreateInstance
  - [x] DescribeInstance
  - [x] DeleteInstance
  - [x] ModifyInstanceName
  - [x] ModifyInstanceSpec
  - [x] CreateDisk
  - [x] ResizeDisk
  - [x] DeleteDisk
  - [x] ModifyIpAddress
  - [x] ExtendSystemDisk
  - [x] ResetInstancesPassword
  - [x] ResetImage
  - [x] ModifyInstanceChargeType
  - [x] StartInstance
  - [x] StartInstances
  - [x] StopInstances
  - [x] RebootInstances

- [x] 虚拟数据中心管理
  - [x] DescribeVdc
  - [x] CreateVdc
  - [x] DeleteVdc
  - [x] CreatePublicNetwork
  - [x] CreatePrivateNetwork
  - [x] ModifyPublicNetwork
  - [x] AddPublicIp
  - [x] DeletePublicIp
  - [x] DeletePublicNetwork
  - [x] DeletePrivateNetwork
  - [x] RenewPublicNetwork
  - [x] ModifyVdcName
  
 - [x] 负载均衡管理
    - [x] DescribeZones
    - [x] DescribeLoadBalancersSpec
    - [x] CreateLoadBalancer
    - [x] DescribeLoadBalancers
    - [x] DescribeLoadBalancersModifySpec
    - [x] ModifyLoadBalancerInstanceSpec
    - [x] DeleteLoadBalancer
    - [x] DescribeCACertificates
    - [x] DescribeCACertificate
    - [x] DeleteCACertificate
    - [x] UploadCACertificate
    - [x] DescribeLoadBalancerStrategys
    - [x] ModifyLoadBalancerStrategys
    - [x] ModifyLoadBalancerName

# 环境准备

1、要使用首云Python SDK, 您需要一个云账号以及一对`Access Key Id` 和 `Secret Access Key`。请在首云控制台中[综合管理页面](https://c2.capitalonline.net/portal/webapps/synthesize/safe)上创建和查看您的Access Key，或者联系您的系统管理员。

2、要使用首云SDK访问某个产品的API，您需要事先在[控制台](https://c2.capitalonline.net/main/home)上开通这个产品。

# SDK获取和安装

## 通过pip安装

您可以通过pip安装方式将首云Python SDK安装到您的项目中。

通过pip方式安装或者更新，请在命令行中执行以下命令：

```shell
# pip install --upgrade cds-python-sdk
```



## 通过源码包安装

```shell
# git clone https://github.com/capitalonline/cds-python-sdk.git
# cd cds-python-sdk
# python setup.py install
```

# 使用示例

以下这段代码示例向您展示了调用首云Python SDK的3个主要步骤：

1. 创建Client实例
2. 创建request请求并且设置参数
3. 发起请求并处理异常

```python
#!/usr/bin/python
from capitalonline.instance.client import NewClient,NewAddInstanceRequest
from capitalonline.instance.models import DataDisk, PrivateIp, SystemDisk, OrderedIP
ak = ''
sk = ''
Beijing_region = 'Beijing'

def TestClient_CreateInstance():
    # Init a credential with Access Key Id and Secret Access Key
    # You can apply them from the CDS web portal
	
    #创建client实例
    client, err = NewClient(ak, sk, Beijing_region)
    if err:
        print(f'API request failed,err:{err}')
        return
    #创建request，并且设置参数
    request = NewAddInstanceRequest()
    request.RegionId = 'CN_Shanghai_C'         #region id must be set.
    request.VdcId = ''                         #vdc id must be set.
    request.Password = '********'              #password must be set.
    request.InstanceName = 'test1'             #instance name must be set.
    request.InstanceChargeType = 'PostPaid'
    request.AutoRenew = 0
    request.Cpu = 4                            #cpu must be set.
    request.Ram = 4                            #ram must be set.
    request.ImageId = 'Centos_7.6_64'
    request.PublicIp = ['auto']
    request.InstanceType = 'CCS.IC3V2'         #instance type must be set.
    request.UTC = False

    dd1 = DataDisk()
    dd1.Size = 200
    dd1.Type = 'high_disk'

    ip1 = PrivateIp()
    ip1.PrivateId = ''                         #if set private ip, private id must be set.
    ip1.IP = ['auto']

    request.DataDisks = [dd1]
    request.PrivateIp = [ip1]
    
    ordered_ip1 = OrderedIP()                  # if set ordered ip, pipe id must be set. And if this parameter is used, other parameters(such as PublicIp AND PrivateIp) do not take effect.
    ordered_ip1.PipeId = ''
    ordered_ip1.IP = ['auto']

    request.OrderedIP = [ordered_ip1]
    system_disk = SystemDisk()
    system_disk.IOPS = 5
    system_disk.Size = 20
    system_disk.Type = 'ssd_system_disk'

    request.SystemDisk = system_disk
    # 发起请求，处理异常
    resp, err = client.CreateInstance(request)    
    print(f'Create instance response:{resp}, err:{err}')
    
if __name__ == '__main__':
    TestClient_CreateInstance()
```

更多示例参见各产品SDK目录下的client_test.py文件。

## 如何贡献

欢迎提交 Issue 或 Pull Request。

## 相关参考

- [CDS OpenAPI Explorer](https://github.com/capitalonline/openapi)

## 许可证

[Apache License v2.0](./LICENSE)

