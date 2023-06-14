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

    ordered_ip1 = OrderedIP()                 # if set ordered ip, pipe id must be set.
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
