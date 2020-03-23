# ambari-flume-service

Reference from: ambari-server/src/main/resources/common-service/FLUME/1.4.0.2

**test environment：**

- ambari 2.7.3

- hdp 3.1.0

- flume 1.9.0

**rpmbuild:**

  1. you can change version in follow files:

    buildrpm/buildrpm.sh

    buildrpm/rpmbuild/SPECS/flume.spec

  2. install rpmbuild on your host `yum install rpmbuild -y`

  3. copy buildrpm dir to your host

  4. `cd buildrpm`

  5. `sh buildrpm.sh`

**install：**

1. use buildrpm.sh build flume rpm
2. upload flume rpm to your repo
3. copy FLUME to `/var/lib/ambari-server/resources/stacks/HDP/3.1/services/`
4. `ambari-server restart`
5. to ambari web add service ,the service will in the service list
6. good luck

**注意：**

- 在 flume.spec 中最好将flume安装到 `/usr/hdp/current/flume-server`

  因为当 hadoop parameters for stack supporting rolling upgrade，service_check的`flume_bin={stack_root}/current/flume-server/bin/flume-ng`

  如果单纯变更到其它安装目录，可能会报错如下:
  ```bash
  resource_management.core.exceptions.ExecutionFailed: Execution of 'env JAVA_HOME=/usr/jdk64/jdk1.8.0_112 /usr/hdp/current/flume-server/bin/flume-ng version' returned 126. env: /usr/hdp/current/flume-server/bin/flume-ng: Permission denied
  ```

- 如果报错：
`resource_management.core.exceptions.Fail: User 'flume' doesn't exist`检查FlumeHandlerLinux#install()添加用户操作是否成功
