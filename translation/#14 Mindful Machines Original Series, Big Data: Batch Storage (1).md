# Mindful Machines Original Series, Big Data: Batch Storage
# Mindful Machines 原创系列之大数据：批量存储




APRIL 10, 2018 BY MARCIN MEJRAN IN DATA ENGINEERING

2018.4.10  Marcin Mejran  《数据工程》


This is the first part of the Mindful Machines series on 
Big Data, focused on Batch Storage (aka: Big Data Cheat Sheet: Data Storage). In follow on posts we’ll cover [Batch Processing](https://mindfulmachines.io/blog/2018/4/24/series-big-data-batch-processing), Stream Processing, NoSQL and Infrastructure.


这是《Mindful Machines 系列之大数据》的第一部分。主要聚焦于批量存储（又名：《大数据备忘录：数据存储》）。在后续文章中，我们将涉及[批处理](https://mindfulmachines.io/blog/2018/4/24/series-big-data-batch-processing)、流处理、 NoSQL 和基础架构。


You’ve got a lot of data coming in you and you want to store it somewhere for future analysis? Where do you put it all? In this post we go over the myriad of options out there and how they stack against each other. This isn’t a complete list of available technologies but rather the highlight reel that, among other things, explicitly avoids enterprise solutions although does cover PaaS.

你有很多数据并且打算把它们存储起来以备将来分析吗？你准备如何存储这些数据？在这篇文章中，我们将讨论各种数据存储方案，以及他们之间的联系。下文并非为了提供一个所有可行技术的完整清单，而是讨论一些技术亮点。尽管涉及 PaaS，但本文会特别避免讨论企业级解决方案。

Some good background reading for understanding distributed storage includes [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem) and some of its [limitations](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html%20).

为了更好的了解分布式存储，请参阅 [CAP 定理](https://en.wikipedia.org/wiki/CAP_theorem)及其[局限性](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html%20)

![](https://static1.squarespace.com/static/565272dee4b02fdfadbb3d38/t/5abd436f575d1f4c80636747/1522353024477/bigdatabatchstorage2.png?format=750w)

# RDBM
# 关系数据库管理系统
The traditional SQL database may seem an odd choice however, in addition to simply scaling vertically, with [sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture)) and read-replicas it can scale across multiple nodes. In the following points I’m focusing more on these databases as analytical data stores (relatively few large queries) rather than traditional databases (massive numbers of relatively small queries).

传统的 SQL 数据库看上去可能不是个常规的选择。但是，除了简单的纵向扩展，它还可以通过 [分片](https://en.wikipedia.org/wiki/Shard_(database_architecture))（sharding）和只读副本（read-replicas）进行跨节点扩展。在后文中，我会更多的将这些数据库作为分析型数据库（相对少量的大型查询），而不是传统数据库（大量的小型查询）来分析。


Overall:
   - Powerful [ACID](https://en.wikipedia.org/wiki/ACID) guarantees
   - Row level updates and inserts
   - Requires structured data however some databases also have support for free form JSON fields
   - Can scale to handle large data sizes
      - Vertically: Modern machines can be quite large so even a single machine can store significant data
      - Horizontally: Sharding is possible although it requires additional manual setup and potentially client logic changes
   - There are tradeoffs as you scale (ie: queries across partitions or complex queries)
      - Computing tied to storage system in terms of scaling
      - Multi-master or automatic failover setups can be tricky to get right so often a single point of failure exists
   - Used by [Uber](https://eng.uber.com/mysql-migration) and [Facebook](https://code.facebook.com/posts/190251048047090/myrocks-a-space-and-write-optimized-mysql-database) to handle massive amounts of data
   - There are better purpose built technologies if you truly need to scale big

总体：
   - 强有力的 [ACID](https://en.wikipedia.org/wiki/ACID) 保证（译者注：Atomicity 原子性、Consistency 一致性、Isolation 隔离性、Durability 耐久性）
   - 行级更新和插入
   - 需要结构化数据。一些数据库也支持自由格式的 JSON 字段
   - 可扩展至大数据规模
      - 纵向上：现代机器的存储空间可以相当大，所以即使一台机器也能存储显著的数据
      - 横向上：能支持分片（Sharding）。虽然需要额外的手动设置和潜在的客户端逻辑更改
   - 进行扩展时，你需要进行权衡（例如：跨分区查询还是复杂查询）
      - 就扩展而言，计算与存储系统密切相关
      - 复杂的多主集群或自动故障转移设置可能会导致系统中存在单点故障
   - 被 [Uber](https://eng.uber.com/mysql-migration) 和 [Facebook](https://code.facebook.com/posts/190251048047090/myrocks-a-space-and-write-optimized-mysql-database) 采用，进行大数据处理
   - 如果你真的需要扩展规模，还有更好的专用技术可以选择



[MySQL](https://www.mysql.com):
   - Open source; PaaS and enterprise versions exist
   - Support for JSON data types
   - Recent support for window functions
   - Commercial support by [Oracle](https://www.mysql.com/products) (who owns MySQL), PaaS support by [AWS](https://aws.amazon.com/rds)

[MySQL](https://www.mysql.com)：
   - 开源；存在 PaaS 和企业版
   - 支持 JSON 数据类型
   - 新增对窗口函数的支持
   - [Oracle](https://www.mysql.com/products) （MySQL的拥有者）的商业支持，[AWS](https://aws.amazon.com/rds) 的 PaaS 支持



[MariaDB](https://mariadb.org):
   - Open source
   - Originally a fork of MySQL
   - Support window functions
   - No JSON data type but native functions for working with JSON
   - Support for a [columnar](https://mariadb.com/products/technology/columnstore) storage engine which significantly speeds up analytical workloads
   - Commercial support by [MariaDB](https://mariadb.com), PaaS support by [AWS](https://aws.amazon.com/rds)
   
[MariaDB](https://mariadb.org)：
   - 开源
   - 最初是 MySQL 的一个分支
   - 支持窗口函数
   - 无 JSON 数据格式，但支持处理 JSON 的原生函数
   - 支持[列式](https://mariadb.com/products/technology/columnstore)存储引擎，显著提升分析速度
   - [MariaDB](https://mariadb.com) 的商业支持，[AWS](https://aws.amazon.com/rds) 的 PaaS 支持
   


[PostgreSQL](https://www.postgresql.org)
   - Open source; PaaS and enterprise versions exist
   - Support for JSON data types
   - Commercial support by various companies
   - Better parallel single query optimizations than MySQL
   - Third party support for [columnar](https://github.com/citusdata/cstore_fdw) storage engine which significantly speeds up analytical workloads
   - Support for sharding via [PL/Proxy](https://plproxy.github.io)
   
   
   
[PostgreSQL](https://www.postgresql.org)
   - 开源；存在 PaaS 和企业版
   - 支持 JSON 格式
   - 拥有多个公司的商业支持
   - 比 MySQL 更好的并行单一查询优化
   - 第三方对[列式](https://github.com/citusdata/cstore_fdw)存储引擎的支持，大大加快了分析速度
   - 支持通过 [PL 或者代理](https://plproxy.github.io)进行分片（sharding）



[Amazon Aurora](https://aws.amazon.com/rds/aurora): Fully managed MySQL and PostgeSQL compatible databases on AWS
   - Proprietary PaaS
   - Automatically and seamlessly allocates storage
   - Data is replicated across and within availability zones
   - Claims [improved performance](https://www.percona.com/blog/2016/05/26/aws-aurora-benchmarking-part-2) compared to open source versions due to tight coupling with the SSD storage layer
      - PostgreSQL performance may be [lower](https://www.chooseacloud.com/postgresql) on Aurora
   - Lags behind open source in version support, Aurora MySQL 5.7 support came out over 2 years after MySQL 5.7
   - Does not support clustering beyond read replicas
   
   
   
   
[Amazon Aurora](https://aws.amazon.com/rds/aurora): 兼容 MySQL 和 PostageSQL 的 AWS 全托管数据库
   - 专有的 PaaS
   - 存储空间自动切无缝分配
   - 数据在所有可使用区域复制
   - 声称对比于开源版，通过与 SSD 存储层的紧密耦合[提高了性能](https://www.percona.com/blog/2016/05/26/aws-aurora-benchmarking-part-2)。
      - 比PostgreSQL[更好的](https://www.chooseacloud.com/postgresql)性能
   - 在开源版本的支持方面存在落后。Auro 对 MySQL 5.7 的支持在 MySQL 5.7 之后 2 年出现
   - 不支持除只读副本外的集群




# Object/File Storage:
# 对象/文件存储：

These are distributed scalable ways of storing large amounts of bulk data such as historical logs or images files. These data stores can efficiently read out batches of data for further processing (via Spark, Presto, etc.) and so are capable of acting as a Data Warehouse backend.

这些分布式、可扩展的数据存储多用于存储大量的类似历史日志或图像文件等大块数据。这些数据存储可以有效地进行批量数据读取以便进一步处理（通过 Spark、Presto 等）。因此能够充当数据仓库（Data Warehouse）的后端。


Overall:
   - Efficient storage of structured, semi-structured and unstructured data
   - Not designed for individual row level reads and writes
   - Not optimized for storing small files/objects
   - Data processing systems (Spark, MapReduce, etc.) can connect to them
   - Computing can scale independently of storage
   
总体：
   - 结构化、半结构化和非结构化数据的高效存储
   - 不是为单行的读写而设计的
   - 不适用存储小文件或对象
   - 可以连接数据处理系统（Spark、MapReduce 等）
   - 计算可以不依赖于存储而独立扩展


   
[Apache HDFS](https://hortonworks.com/apache/hdfs): The Hadoop Distributed File System (HDFS) provides a distributed way of storing hundreds of petabytes of data
   - Open source; PaaS and enterprise versions exist
   - Written in Java
   - First release in 2006
   - Distributed, fault-tolerant and scalable
      - Data is stored multiple times across the cluster either as full copies or utilizing erasure coding
      - Multiple master nodes allow for seamless failover
   - Stores files in directories but not designed as a mountable file system
   - Various other projects have strong support for HDFS including HBase, Spark, Hive, Hadoop MapReduce, Presto and Flink
   - Even with modern tooling ([Hortonworks](https://hortonworks.com/products/data-platforms/hdp), [Cloudera](https://www.cloudera.com/products/open-source/apache-hadoop.html)) there is still a non-trivial amount of operational knowledge needed to run your own cluster
      - PaaS versions exist ([Amazon EMR](https://aws.amazon.com/emr), [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight), [Google Dataproc](https://azure.microsoft.com/en-us/services/hdinsight)) and can lower operational knowledge needed
   - Not optimized for storing large number of smaller files (<64mb) such as images
      - You can bundle them together into, for example, SequenceFiles
   - Based on the [Google File System](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) paper
   - If you’re running your own hardware or need the performance then it’s a solid choice but otherwise a cloud store like S3 makes more sense
   - Commercial support provided by [Hortonworks](https://hortonworks.com) and [Cloudera](https://www.cloudera.com)

[Apache HDFS](https://hortonworks.com/apache/hdfs)：Hadoop 分布式文件系统（HDFS）提供了一种存储数百 PB 字节的分布式数据存储。
   - 开源；存在 PaaS 和企业版
   - 用 Java 编写
   - 2006 年首次发行
   - 分布式，容错的，可扩展
      - 数据在集群中以完整副本或纠删编码的形式存储多份
      - 多个主节点支持无缝故障转移
   - 以目录形式存储文件，但未设计成可挂载的文件系统
   - 其他多个项目强有力的支持 HDFS，包括 HBASE、SCAK、HIVE、Hadoop MapReduce、Presto 和 Flink
   - 即使使用现代工具（[Hortonworks](https://hortonworks.com/products/data-platforms/hdp)，[Cloudera](https://www.cloudera.com/products/open-source/apache-hadoop.html)），运行自己的集群仍然需要大量的操作知识
      - 存在 PaaS 版（[Amazon EMR](https://aws.amazon.com/emr)， [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight)， [Google Dataproc](https://cloud.google.com/dataproc)），并且 PaaS 版可以减少所需的操作知识。
   - 没有针对存储大量较小的文件（<64  MB）例如图像，进行优化
      - 你可以把它们组合在一起形成，例如，SequenceFiles
   - 基于[谷歌文件系统](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)相关论文
   - 如果您正在运行自己的硬件或对性能有要求，那么这是一个可靠的选择.。否则，像 S3 这样的云存储是更好的选择
   - [Hortonworks](https://hortonworks.com) 及 [Cloudera](https://www.cloudera.com) 提供的商业支持


[Amazon S3](https://aws.amazon.com/s3): A fully managed object/file storage platform provided by Amazon 
   - Proprietary PaaS
   - Distributed, highly available (99.99%) and fault-tolerant (11 9’s)
   - Fully managed so no configuration or manual scaling is necessary
   - Can emulate a file system including listing objects/files in "directories” (technically just uses the prefixes of keys)
   - Can be considered an alternative to HDFS as many projects are able to query data stored in S3 (including MapReduce, Spark, Flink, Presto, etc.)
      - HBase can use S3 as a storage backend if using Amazon EMR
   - List operations can be slow and are only eventually consistent (ie: may return stale data)
      - Latest release of Hadoop includes experimental [metadata caching](https://hadoop.apache.org/docs/r3.0.0) support to work around this
   - Relatively low cost and lack of operational overhead 
   - A solid choice for storing batch data if you’re in the Amazon ecosystem
   
[Amazon S3](https://aws.amazon.com/s3)：一个由 Amazon 提供的全托管对象/文件存储平台
   - 专有的 PaaS
   - 分布式，高可用性（99.99%）和容错性（99.999999999%）
   - 完全托管，无需自行配置或人工扩展
   - 可以模拟一个文件系统，包括在“目录”中列出对象/文件（技术上，仅使用键的前缀）
   - 可以认为是 HDFS 的替代方案，因为许多项目能够查询存储在 S3 中的数据（包括 MapReduce、Spark、Fl.、Presto 等）
      - 如果使用Amazon EMR，HBase 可以使用 S3 作为存储后端
   - 列表操作比较缓慢，并且仅在最终结果才能保持一致。（例如：可能返回过期数据）
      - Hadoop 的最新发布版本中包括了实验性的[元数据缓存](https://hadoop.apache.org/docs/r3.0.0)支持来解决这个问题
   - 相对低的成本和较少的操作开销
   - 如果你是 Amazon 生态系统的用户，那么这是一个存储批量数据的可靠选择



[Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs): An object/file storage platform akin to S3 provided by Azure 
   - Proprietary PaaS
   - Distributed, highly available (99.99%) and fault-tolerant (11 9’s or greater depending on replication configuration)
   - Fully managed so no configuration or manual scaling is necessary
   - Strongly consistent in list operations unlike S3
   - Can be considered an alternative to HDFS as many projects are able to query data stored in S3 (including MapReduce, Spark, Flink, Presto, etc.)
      - HBase can use Azure Blob Storage as a backend natively
   - Relatively low cost and lack of operational overhead 
   - A solid choice for storing batch data if you’re in the Azure ecosystem
   
[Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs)：由 Azure 提供的类似于 S3 的对象/文件存储平台
   - 专有的 PaaS
   - 分布式的、高度可用的（99.99%）以及容错的（根据复制配置的不同，可达到 99.999999999% 或者更高）
   - 完全托管，无需配置或人工扩展
   - 不同于 S3，可在列表操作时保持强一致性
   - 可以认为是 HDFS 的替代方案，因为许多项目能够查询存储在 S3 中的数据（包括 MapReduce、Spark、Fl.、Presto 等）
      - HBase 可以用 Azure Blob Storage 作为原生后端
   - 相对低的成本和较少的操作开销
   - 如果你是 Azure 生态系统的用户，那么这是一个存储批量数据的可靠选择


[Google Cloud Storage](https://cloud.google.com/storage): An object/file storage platform akin to S3 provided by Google 
   - Proprietary PaaS
   - Distributed, highly available (99.9% to 99.95%) and fault-tolerant (11 9’s)
   - Fully managed so no configuration or manual scaling is necessary
   - Strongly consistent in list operations unlike S3
   - Can be considered an alternative to HDFS as many projects are able to query data stored in S3 (including MapReduce, Spark, Flink, Presto, etc.)
      - HBase is not supported, Google instead prefers you use the HBase interface for BigTable
   - Relatively low cost and lack of operational overhead
   - A solid choice for storing batch data if you’re in the Google ecosystem
   
[Google Cloud Storage](https://cloud.google.com/storage): 由 Google 提供的类似于 S3 的对象/文件存储平台
   - 专有的 PaaS
   - 分布式的、高度可用的（99.9% 到 99.95%）以及容错的（99.999999999%）
   - 完全托管，无需配置或人工扩展
   - 不同于S3，可在列表操作时保持强一致性
   - 可以认为是 HDFS 的替代方案，因为许多项目能够查询存储在 S3 中的数据（包括 MapReduce、Spark、Fl.、Presto 等）
      - 不支持 HBase，Google 更希望你使用 BigTable 的 HBase 接口
   - 相对低的成本和较少的操作开销
   - 如果你是 Google 生态系统的用户，那么这是一个存储批量数据的可靠选择



# Columnar NoSQL
# 列式 NoSQL

Instead of storing data as rows these databases instead store data as [columns](https://en.wikipedia.org/wiki/Column-oriented_DBMS) or groups of columns. This approach allows for much higher performance in cases where only a subset of the columns needs to be read for a given query.

与以行的形式存储数据相反，列式 NoSQL 数据库以[列](https://en.wikipedia.org/wiki/Column-oriented_DBMS)或者一组列的形式存储数据。在仅需读取某些列的子集的查询中，这样的存储方式能极大的提高性能。

Overall:
   - Efficient storage of structured data
   - Allow for key level write and reads in addition to bulk reads and writes
   - Data processing systems (Spark, MapReduce, etc.) can connect to them and as a result computing can scale independently of storage
   - Can act as a regular NoSQL database
   
总体：
   - 高效存储结构化数据
   - 除了批量读取和写入外，还允许进行关键字级别的写入和读取
   - 可以了解数据处理系统（Spark，MapReduce 等）从而使计算能力的扩展独立于存储能力
   - 可以用作常规的 NoSQL 数据库



[Apache Cassandra](http://cassandra.apache.org): A masterless database that avoids any single point of failure and aims for high availability. 
   - Open source but PaaS and enterprise version exist
   - Written in Java
   - Initially developed by Facebook and publicly released in 2008
   - Availability over consistency (AP) in general
      - Supports tunable per query consistency with rigorous [testing](https://www.datastax.com/dev/blog/testing-apache-cassandra-with-jepsen) to avoid issues
   - Uses a limited SQL syntax for queries (no joins)
   - Requires structured data whose schema is defined ahead of time
   - No external dependencies needed (like ZooKeeper) which makes deployment relatively easy
   - Overall good performance with an original emphasis on batch write performance
   - Supports secondary indexes
   - Used by [Uber](https://eng.uber.com/michelangelo/%20) and [Netflix](https://medium.com/netflix-techblog/scaling-time-series-data-storage-part-i-ec2b6d44ba39%20)
   - Based on the [Dynamo paper](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) from Amazon
   - First class support for Spark and lack of dependencies makes for a great Spark data storage backend
   - Commercial support provided by [DataStax](https://www.datastax.com)
   
[Apache Cassandra](http://cassandra.apache.org)：通过无主从区别的数据库模式避免单点故障，提高可用性
   - 开源；存在 PaaS 和企业版
   - 用 Java 编写
   - 最初由 Facebook 开发并于 2008 年公开发布
   - 大体上，可用性高于一致性（AP）
      - 通过严格[测试](https://www.datastax.com/dev/blog/testing-apache-cassandra-with-jepsen)，支持每个查询一致性的可调，从而避免错误
   - 通过有限的 SQL 语法进行查询（不支持 Join）
   - 需要模式（Schema）已预先定义的结构化数据
   - 无需外部依赖（如 ZooKeeper），这使得部署相对容易
   - 总体性能良好，尤其注重批量写入的性能
   - 支持二级索引
   - 被 [Uber](https://eng.uber.com/michelangelo/%20) 和 [Netflix](https://medium.com/netflix-techblog/scaling-time-series-data-storage-part-i-ec2b6d44ba39%20) 使用
   - 基于亚马逊的 [Dynamo 论文](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
   - 对 Spark 的一级支持和无其它依赖关系，使其非常适合作为 Spark 的数据存储后端
   - [DataStax](https://www.datastax.com) 提供的商业支持



[Apache HBase](https://hbase.apache.org): A strongly consistent (CP) database built on top of HDFS and Zookeeper. 
   - Open source but enterprise versions exists
   - Written in Java
   - First release in 2007
   - Consistency over availability (CP)
   - Native support for being a MapReduce data source. Spark support through a [third-party](https://github.com/hortonworks-spark/shc) and soon built-in support in HBase 3.0.0 (may be a while judging by the 2.0.0 releases)
   - Support for [Coprocessors](https://blogs.apache.org/hbase/entry/coprocessor_introduction) that allow for custom code to easily run on HBase servers
   - Read performance on par or better than Cassandra but slower write performance
      - Actual results depends on who’s doing the test: [Hortonworks](https://hortonworks.com/blog/hbase-cassandra-benchmark) or [DataStax](https://www.datastax.com/nosql-databases/benchmarks-cassandra-vs-mongodb-vs-hbase)
   - Dependency on HDFS and Zookeeper means that deployment is fairly involved if you haven’t already bought into the Hadoop ecosystem
   - Supports secondary indexes
   - Used by [Facebook](https://www.facebook.com/notes/facebook-engineering/the-underlying-technology-of-messages/454991608919%20) among others
   - Inspired by[BigTable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf) from Google 
   - Dependency on HDFS makes it harder to justify as a batch data store versus plain HDFS
   - Commercial support provided by [Hortonworks](https://hortonworks.com) and [Cloudera](https://www.cloudera.com)

[Apache HBase](https://hbase.apache.org):一个强一致的（CP）数据库。构建在 HDFS 和 Zookeeper 之上。
   - 开源；存在企业版
   - 用 Java 编写
   - 2007 年首次发行
   - 一致性高于可用性（CP）
   - 提供对 MapReduce 的原生支持。通过第三方支持 Spark。很快，又提供了内置的 HBase 3.0.0 支持（用 2.0.0 发行版评判，可能过了一段时间）
   - 支持[协处理器](https://blogs.apache.org/hbase/entry/coprocessor_introduction)，使自定义代码能在 HBase 服务器上轻松运行
   - 读取性能与 Cassandra 平分秋色甚至更胜。但写入速度较慢
      - 实际结果取决于测试者是 [Hortonworks](https://hortonworks.com/blog/hbase-cassandra-benchmark) 还是 [DataStax](https://www.datastax.com/nosql-databases/benchmarks-cassandra-vs-mongodb-vs-hbase)
   - 依赖 HDFS 和 Zookeeper。如果你并不是 Hadoop 生态系统的用户，那么部署起来比较复杂
   - 支持二级索引
   - 被 [Facebook](https://www.facebook.com/notes/facebook-engineering/the-underlying-technology-of-messages/454991608919%20) 等使用
   - 受到 Google BigTable 的影响
   - 对于 HDFS 的依赖，使得很难说清着究竟是批量数据存储仓库，还是普通的 HDFS
   - [Hortonworks](https://hortonworks.com) 和 [Cloudera](https://www.cloudera.com) 的商业支持


[Google BigTable](https://cloud.google.com/bigtable): A fully managed database that aims for high consistency
   - Proprietary PaaS
   - Consistency over availability (CP)
   - Fully managed
   - HBase is inspired by BigTable and BigTable provides an open source HBase compatibility layer
      - Third party libraries (Spark, MapReduce, etc.) that have HBase support generally also have BigTable support
      - No support for custom Coprocessors
   - No support for secondary indexes

[Google BigTable](https://cloud.google.com/bigtable)：面向高一致性的全托管数据库
   - 专有的 PaaS   
   - 一致性高于可用性（CP）
   - 完全托管
   - HBase 就是受到了 BigTable 影响。 同时， BigTable 提供了 开源的 HBase 兼容层
      - 支持 HBase 的第三方库（Spark， MapReduce 等）一般也同样支持 BigTable
      - 不支持自定义协处理器
   - 不支持二级索引



[Amazon DynamoDB](https://aws.amazon.com/dynamodb): A fully managed database that aims for high availability
   - Proprietary PaaS
   - Availability over consistency (AP) in general but has support for tunable per query consistency
   - Fully managed
      - Provides [auto-scaling](https://aws.amazon.com/blogs/aws/new-auto-scaling-for-amazon-dynamodb) for the read and write capacity
   - You do not need to define a schema ahead of time for each table but merely the index keys
   - Like Cassandra its derived from the [Dynamo approach](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) (from Amazon) and so shares various similarities
   - There is also support for MapReduce and Spark operations against DynamoDB tables
   - Supports secondary indexes.

[Amazon DynamoDB](https://aws.amazon.com/dynamodb): 面向高可用性的全托管数据库
   - 专有的 PaaS
   - 可用性高于一致性（AP），但支持每个查询一致性的可调
   - 完全托管
      - 支持读写能力的[自动扩展](https://aws.amazon.com/blogs/aws/new-auto-scaling-for-amazon-dynamodb)
   - 无需预先为每个表格定义模式（Schema），只需定义索引键
   - 与 Cassandra 一样继承自[Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)，因此拥有许多相似之处
   - 支持 MapReduce 和 Spark 对 DynamoDB 表进行操作
   - 支持二级索引


 
# Data Warehouse
# 数据仓库
These are full featured Data Warehouses that tie together the data storage and data processing into a single entity. In the future Data Processing post in this series we’ll go more into the computing performance of these solutions which is often a key reason for using them to store data.

数据仓库集数据存储与数据处理于一体。在本系列的后续《数据处理》一文中，我们将深入研究这些解决方案的计算性能，这正是使用它们存储数据的关键原因。


Overall:
   - Low latency and high throughput query performance but not necessarily faster than other modern batch processing solutions
   - Optimized columnar data storage
   - Limits on flexibility (data types, UDFs, data processing approaches, etc.)
   - Lock-in if used as primary data store
   
总体：
   - 低延迟和高吞吐量的查询性能，但不一定比其他现代批处理解决方案更快
   - 优化的列式数据存储
   - 灵活度有一定局限（数据类型，UDFs，数据处理方法等）
   - 如果用作主数据仓库，会被套牢



[Druid](http://druid.io): Columnar data store designed to provide low-latency analytical queries
   - Open source
   - Written in Java
   - Open sourced in 2012
   - Provides sub-second analytical/OLAP queries
   - Supports real-time ingestion of data rather than just batch ingestion
   - Provides a limited subset of SQL queries (only large to small table joins)
   - Seamless scaling of the cluster up/down independently of storage
   - Leverages “deep” storage such as S3 or HDFS to avoid data loss if nodes go down
   - Complicated infrastructure setup involving multiple types of nodes and distributed storage (S3, HDFS, etc.)
      - Number of external dependencies (S3/HDFS, ZooKeeper, RDBM) which increases operational overhead
   - Well suited for time series data
   - Used by [Airbnb, eBay, Netflix, Walmart and others](http://druid.io/druid-powered.html)
   - A solid choice for a specialized analytical/OLAP system but otherwise other options are more flexible and lower overhead (at the cost of slower queries)
   
[Druid](http://druid.io): ：为提供低延迟分析性查询设计的列式数据仓库
   - 开源
   - 用 Java 编写
   - 2012 年开始开源
   - 提供亚秒级分析性查询/联机查询
   - 支持实时摄取数据，而不单只是批量摄取
   - 提供 SQL 查询的有限子集（仅限于大到小表连接）
   - 集群可独立于存储无缝缩放
   - 利用 S3 或 HDFS 等“深度”存储，避免节点失效时的数据丢失
   - 基础构架设置复杂，涉及多种类型的节点和分布式存储（S3、HDFS 等）
      - 增加操作开销的数个外部依赖关系（S3/HDFS，ZooKeor，RDBM）
   - 适用于处理时间序列数据
   - 被 [Airbnb、eBay、Netflix、沃尔玛等](http://druid.io/druid-powered.html)使用
   - 对于专门的分析/OLAP系统，这是一个可靠的选择。否则，可以选择其他更为灵活，开销更小的解决方案（以较慢的查询为代价）



[ClickHouse](https://clickhouse.yandex): Columnar data store designed to provide low-latency analytical queries and simplicity
   - Open Source
   - Written in C++
   - Open sourced in 2016 by [Yandex](https://yandex.com)
   - Significantly [higher performance](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/#comment-3302778860) than Druid for some workloads
   - Less scalable than Druid or other approaches
   - Leverages Zookeeper but can run a single node cluster without it
   
[ClickHouse](https://clickhouse.yandex)：为提供低延迟分析性查询和简单性而设计的列式数据仓库
   - 开源
   - 用 C++ 编写
   - 2016 年由 [Yandex](https://yandex.com) 开放源码
   - 对某些工作的[性能](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/#comment-3302778860)明显高于 Druid
   - 可扩展性不如 Druid 或其他解决方案 
   - 使用 Zookeeper， 同时也可以在不用 Zookeeper 的情况下运行单节点集群
  

[Amazon Redshift](https://aws.amazon.com/redshift): A fully-managed data warehouse solution that lets you efficiently store and query data using a SQL syntax. 
   - Proprietary PaaS
   - General purpose analytical store that support full SQL syntax
   - Loading/unloading data takes time (hours potentially)
   - No real time ingestion, only batch, although micro-batches can simulate real-time
   - Need to explicitly scale the cluster up/down (with write downtime for the duration)
      - Storage and computing are tied together
   - Lack of complex data types such as arrays, structs, maps or native json
   
[Amazon Redshift](https://aws.amazon.com/redshift): 全托管的数据仓库解决方案，可以使用 SQL语法高效地存储和查询数据。
   - 专有的 PaaS 
   - 支持所有 SQL 语法，可进行一般的分析存储
   - 加载/卸载数据需要时间（有可能数小时）
   - 没有实时摄取，只有批处理，虽然可用微型批次模拟实时
   - 需要明确地调整集群的上行/下限（调整期间，不支持数据写入）
      - 存储和计算是紧密联系在一起的
   - 缺少复杂的数据类型，如数组、结构、映射或本地JSON

[Google BigQuery](https://cloud.google.com/bigquery): A fully-managed data warehouse solution that let’s you efficiently store and query data using a SQL syntax. 
   - Proprietary PaaS
   - General purpose analytical store that support full SQL syntax
   - Real time ingestion support
   - Unlike Redshift it is serverless and you do not need to manage, scale or pay for a cluster yourself
   - Supports complex data types (arrays, structs) but not native json
   
[Google BigQuery](https://cloud.google.com/bigquery): 全托管的数据仓库解决方案，可以使用 SQL 语法高效地存储和查询数据。
   - 专有的 PaaS
   - 支持所有 SQL 语法，可进行一般的分析存储
   - 支持数据实时摄取
   - 与 Redshift 不同的是，它采取无服务器的方式。你不需要自己管理、缩放集群以及支付集群费用
   - 支持复杂数据类型（数组、结构）但不支持原生JSON


[Azure SQL Data Warehouse](https://azure.microsoft.com/en-us/services/sql-data-warehouse)
   - Proprietary PaaS
   - General purpose analytical store that support full SQL syntax
   - No real time ingestion, only batch, although micro-batches can simulate real-time
   - Computing nodes can be scaled independently of storage
      - Can pause computing resources if not using to save cost
      - Storage in Azure Blob Storage
   - Lack of complex data types such as arrays, structs, maps or native json
   
[Azure SQL Data Warehouse](https://azure.microsoft.com/en-us/services/sql-data-warehouse)
   - 专有的 PaaS
   - 支持所有 SQL 语法，可进行一般的分析存储
   - 没有实时摄取，只有批处理，虽然微批次可以模拟实时
   - 计算节点可不依赖于存储节点独立扩展
      - 计算资源在不使用的情况下可以暂停从而节省费用
      - 利用 Azure Blob Storage 存储数据
   - 缺少复杂的数据类型，如数组、结构、映射或本地JSON


