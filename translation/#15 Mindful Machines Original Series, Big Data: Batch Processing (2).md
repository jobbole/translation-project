# Mindful Machines Original Series, Big Data: Batch Processing

# Mindful Machines 原创系列之大数据：批处理


APRIL 24, 2018 BY MARCIN MEJRAN

2018.4.24 Marcin Mejran


This is the second part of the Mindful Machines series on Big Data (aka: Big Data Cheat Sheet), in the [previous post](https://mindfulmachines.io/blog/2018/4/10/series-big-data-batch-storage) we covered Batch Storage, in following posts we’ll cover Stream Processing, NoSQL and Infrastructure.

这是《Mindful Machines 系列之大数据》的第二部分（又名：《大数据备忘录》）。在[上一篇](https://mindfulmachines.io/blog/2018/4/10/series-big-data-batch-storage)文章中我们讨论了批量存储，在后续的文章中，我们将讨论流处理、NoSQL 和基础架构。


Your historical data is overflowing and you want to do something with it? What do you choose to process it? Presto? Spark? Redshift? MapReduce? In this post we go over the myriad of options out there and how they stack against each other. This isn’t a complete list of available technologies but rather the highlight reel that, among other things, explicitly avoids enterprise solutions although does cover PaaS.

你准备如何处理泛滥成灾的历史数据？你选择用什么来处理它？Presto？Spark？Redshift？MapReduce？在这篇文章中，我们将讨论各种数据处理方案，以及他们之间的联系。下文并非为了提供一个所有可行技术的完整清单，而是讨论一些技术亮点。尽管涉及 PaaS ，但本文会特别避免讨论企业级解决方案。

![](https://static1.squarespace.com/static/565272dee4b02fdfadbb3d38/t/5adf1fcf6d2a730adc0567a2/1524572116964/bigdatabatchprocessing2.png?format=1000w)

## Programmatic Batch Processing

## 程序化的批处理

These systems provide a programmatic (Java, Scala, Python, etc.) interface for querying data stored in batch storage systems (HDFS, S3, Cassandra, HBase, etc.).

这些系统为存储在批量存储系统（HDFS，S3，Cassandra，HBase 等）中的数据提供了程序化（Java，Scala，Python 等）的数据查询接口。

*   **Overall**
    *   Provide a flexible interface for querying data
    *   Schemas need to be managed manually or loaded from files
    *   Modern system provide high level APIs that allow for whole query optimizations
    
-   **总体**

    -   提供灵活的数据查询接口
    -   模式（Schema）需要人工管理或从文件中加载
    -   现代系统提供了支持整体查询优化的高级 API


*   **[Apache Hadoop MapReduce](https://hortonworks.com/apache/mapreduce/):** A cornerstone of the Big Data ecosystem which provides a way to efficiently process petabytes of data
    *   Open source but PaaS and enterprise versions exist
    *   Written in Java
    *   Released in 2006
    *   Implementation of Google’s [MapReduce paper](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
    *   Provides a way to query large amounts of data across multiple machines in an efficient and easy to implement way compared to traditional cluster computing approaches
    *   Writing raw Java MapReduce code is relatively complicated
    *   Google has not been using MapReduce as it’s primary big data processing model since [2014](http://www.datacenterknowledge.com/archives/2014/06/25/google-dumps-mapreduce-favor-new-hyper-scale-analytics-system) and there are newer technologies that are unseating MapReduce in the open source world (see other entries).
    *   Requires a Hadoop (YARN) cluster which introduces operational overhead
        *   PaaS versions exist ([Amazon EMR](https://aws.amazon.com/emr/), [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/), [Google Dataproc](https://cloud.google.com/dataproc/)) and can lower operational knowledge needed
    *   Commercial support provided by [Hortonworks](https://hortonworks.com/) and [Cloudera](https://www.cloudera.com/)
    
    
    
-   **[Apache Hadoop MapReduce](https://hortonworks.com/apache/mapreduce/)：** 大数据生态系统的基石，它提供了一种高效处理拍字节(petabytes)级别数据的方法
    -   开源；存在 PaaS 和企业版
    -   用 Java 编写
    -   发布于 2006 年
    -   脱胎于 Google 的 [MapReduce 论文](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
    -   与传统的集群计算方法相比，为大批量数据的跨机器查询提供了高效且易于实现的方法
    -   编写原始的 Java MapReduce 代码相对复杂
    -   自 [2014](http://www.datacenterknowledge.com/archives/2014/06/25/google-dumps-mapreduce-favor-new-hyper-scale-analytics-system) 年以来，Google 就不再使用 MapReduce 作为大数据处理的主要模型。开源世界中，新的技术正在取代 MapReduce（参见其他条目）。
    -   需要使用 Hadoop（YARN） 集群。 这增加了操作开销
        -   存在 PaaS 版（[Amazon EMR](https://aws.amazon.com/emr/)， [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/)， [Google Dataproc](https://cloud.google.com/dataproc/)），并且 PaaS 版可以减少所需的操作知识
    -   [Hortonworks](https://hortonworks.com/) 和 [Cloudera](https://www.cloudera.com/) 提供商业支持



*   **[Cascading](https://www.cascading.org/projects/cascading/)/[scalding](https://github.com/twitter/scalding):** Java/Scala, respectively, frameworks that abstract away the complexity of writing MapReduce code
    *   Open source
    *   Written in Java/Scala
    *   Significantly lowers the overhead of writing MapReduce code
    *   Can leverage [Tez](https://hortonworks.com/apache/tez/) or [Flink](https://flink.apache.org/) to significantly improve [performance](http://scalding.io/2015/05/scalding-cascading-tez-%E2%99%A5/)
    
    
-   **[Cascading](https://www.cascading.org/projects/cascading/)/[scalding](https://github.com/twitter/scalding)：** 分别使用
    Java、Scala 编写的程序框架，以帮助用户从复杂的 MapReduce 编程中抽离出来
    -   开源
    -   用 Java、Scala 编写
    -   显著降低编写 MapReduce 代码的开销
    -   可以利用 [Tez](https://hortonworks.com/apache/tez/) 或
        [FLink](https://flink.apache.org/)
        显著提高[性能](http://scalding.io/2015/05/scalding-cascading-tez-%E2%99%A5/)
    
    
    
*   **[Apache Spark](https://spark.apache.org/):** A highly popular cluster computing framework based on in memory storage of intermediate data
    *   Open source but PaaS and SaaS versions exist
    *   Written in Scala
    *   Started in 2009, described in a [paper](http://people.csail.mit.edu/matei/papers/2010/hotcloud_spark.pdf) published in 2010
    *   Shines in providing a mostly unified API across Python, Scala, Java, R and SQL that lets you mix together native code and optimized built-in commands
    *   Support a streaming paradigm on top of it’s batch processing engine
    *   Provides a build in machine learning library ([MLLib and ML](https://spark.apache.org/docs/latest/ml-guide.html))
    *   Contains significant configurable settings and requires tuning to get good [performance](https://databricks.com/blog/2017/07/12/benchmarking-big-data-sql-platforms-in-the-cloud.html)
    *   Spark’s biggest code contributor and commercial backer (Databricks) markets how much [faster](https://databricks.com/blog/2017/07/12/benchmarking-big-data-sql-platforms-in-the-cloud.html) it’s proprietary PaaS version is than the open source version which creates skewed incentives for them.
    *   PaaS solutions provided by [Amazon EMR](https://aws.amazon.com/emr/), [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) and [Google Dataproc](https://cloud.google.com/dataproc/)
    *   SaaS solution provided by [Databricks Unified Analytics Platform](https://databricks.com/product/unified-analytics-platform)
    *   Commercial support provided by [Hortonworks](https://hortonworks.com/) and [Cloudera](https://www.cloudera.com/)


-   **[Apache Spark](https://spark.apache.org/)：** 一种高度流行的将中间数据储存在内存中的集群计算框架
    -   开源；存在 PaaS 和 SaaS 版本
    -   用 Scala 编写
    -   始于 2009 年，在 2010 年发表的[论文](http://people.csail.mit.edu/matei/papers/2010/hotcloud_spark.pdf)中被介绍
    -   一大亮点是为 Python、Scala、Java、R 和 SQL 提供了基本统一的
        API，使得原生代码可以和优化的内置命令混合使用
    -   在批处理引擎之上，提供对流式范式（streaming paradigm）的支持
    -   内置机器学习库（[MLLib 和
        ML](https://spark.apache.org/docs/latest/ml-guide.html)）
    -   包含重要的，需要调谐的配置，以获得良好的[性能](https://databricks.com/blog/2017/07/12/benchmarking-big-data-sql-platforms-in-the-cloud.html)
    -   Spark 最大的代码贡献者和商业支持者（Databricks）宣传他们的私有 PaaS
        版比开源版要[快](https://databricks.com/blog/2017/07/12/benchmarking-big-data-sql-platforms-in-the-cloud.html)得多。 这对它们产生了倾斜的激励机制。
    -  [Amazon EMR](https://aws.amazon.com/emr/)， [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/)， [Google Dataproc](https://cloud.google.com/dataproc/) 提供 PaaS 解决方案
    -   [Databricks Unified Analytics Platform](https://databricks.com/product/unified-analytics-platform) 提供 SaaS 解决方案
    -   [Hortonworks](https://hortonworks.com/) 和 [Cloudera](https://www.cloudera.com/) 提供商业支持



*   **[Apache Flink](https://flink.apache.org/):** Cluster computing framework that aims to provide improvements compared to Spark
    *   Open source but PaaS versions exist
    *   Written in Java and Scala
    *   Released in 2013
    *   Provides an API across Python, Scala, Java and SQL
    *   Support a batch paradigm on top of it’s streaming processing engine
    *   Less configuration overhead than Spark
    *   Provides a built in machine learning library, [FlinkML](https://ci.apache.org/projects/flink/flink-docs-release-1.4/dev/libs/ml/index.html), but it’s less comprehensive and [performant](https://link.springer.com/article/10.1186/s41044-016-0020-2) than Spark’s
    *   Newer project that shows a lot of promise but Spark has added significant performance and feature improvement in newer versions that likely more than closed the gap
    *   PaaS solutions provided by [Amazon EMR](https://aws.amazon.com/emr/) and [Google Dataproc](https://cloud.google.com/dataproc/)


-   **[Apache Flink](https://flink.apache.org/)：** 集群计算框架，旨在提供比 Spark 更好的服务
    -   开源；存在 PaaS 版本
    -   用 Java 和 Scala 编写
    -   发布于 2013 年
    -   为 Python、Scala、Java 和 SQL 提供 API
    -   在流处理引擎之上提供对批处理范式（batch paradigm）的支持
    -   配置开销小于 Spark
    -   提供内置的机器学习库—[FlinkML](https://ci.apache.org/projects/flink/flink-docs-release-1.4/dev/libs/ml/index.html)，
        但其广泛性和[性能](https://link.springer.com/article/10.1186/s41044-016-0020-2)都不如
        Spark 的机器学习库
    -   是一个比较新的项目，并且看上去前景很好。但是 Spark
        在新版本中的性能提升和功能改进不仅弥补了两者的差距，还有超越的趋势
    -   [Amazon EMR](https://aws.amazon.com/emr/) 和 [Google
        Dataproc](https://cloud.google.com/dataproc/) 提供 PaaS 解决方案


## SQL Batch Processing

## SQL 批处理

These frameworks provide a SQL interface for querying data stored in HDFS or other blob storage systems (S3, etc.) in a distributed fashion.

这些框架提供了一个 SQL 接口，用于查询以分布式方式存储在 HDFS 或其他 blob（译者注：二进制大对象） 存储系统（S3 等）中的数据。

*   **Overall**
    *   Provide a centralized schema repository
    *   Allow for whole query optimizations but restrict you to only using SQL and potentially custom UDFs
    *   Most require a traditional SQL server to host table metadata


-   **总体**
    -   提供集中式模式仓库
    -   支持整体查询优化，但仅限于使用 SQL 和潜在的自定义 UDFs
    -   大多数都需要传统的 SQL Server 来承载表元数据



*   **[Apache Hive](https://hive.apache.org/):** A SQL layer originally on top of HAdoop MapReduce and now on top of YARN
    *   Open source but PaaS versions exist
    *   Written in Java
    *   Released by Facebook in 2009
    *   Custom UDFs, in Java, can be difficult and time consuming to write
    *   More optimized for complex analytical queries
    *   The newest versions partially bypass MapReduce and run a daemon on individual nodes ([LLAP](https://cwiki.apache.org/confluence/display/Hive/LLAP)) to further optimize performance.
        *   As a result newer versions stack up quite well [performance](https://www.youtube.com/watch?v=dS1Ke-_hJV0) [wise](https://www.slideshare.net/ssuser6bb12d/hive-presto-and-spark-on-tpcds-benchmark) against Presto and Spark
    *   PaaS solutions provided by [Amazon EMR](https://aws.amazon.com/emr/), [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) and [Google Dataproc](https://cloud.google.com/dataproc/)
    *   Commercial support provided by [Hortonworks](https://hortonworks.com/) and [Cloudera](https://www.cloudera.com/)


-   **[Apache Hive](https://hive.apache.org/)：** 最初是 Hadoop MapReduce 之上的一个 SQL 层，如今在 YARN 之上
    -   开源；存在 PaaS 版本
    -   用 Java 编写
    -   Facebook 于 2009 年发布
    -   使用 Java 编写自定义 UDFs 可能很难且非常耗时
    -   更适用于复杂的分析性查询
    -   最新版本部分程度上绕过了 MapReduce
        并在单个节点（[LLAP](https://cwiki.apache.org/confluence/display/Hive/LLAP)）上运行守护进程，以进一步优化性能。
        -   因此，新版本的[性能](https://www.youtube.com/watch?v=dS1Ke-_hJV0)与
            Presto 和 Spark
            [相当](https://www.slideshare.net/ssuser6bb12d/hive-presto-and-spark-on-tpcds-benchmark)
    -   [Amazon EMR](https://aws.amazon.com/emr/)、[Azure
        HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) 和
        [Google Dataproc](https://cloud.google.com/dataproc/) 提供 PaaS 解决方案
    -   [Hortonworks](https://hortonworks.com/) 和
        [Cloudera](https://www.cloudera.com/) 提供商业支持



*   **[Apache Spark SQL](https://spark.apache.org/sql/):** A SQL computing layer that is built on top of Spark
    *   Open source
    *   Written in Scala
    *   Started as Shark in 2010
    *   Requires a Spark cluster
    *   More optimized for complex analytical queries
    *   Custom UDFs are easy to write in Scala, Python, Java or R
    *   Requires a Spark cluster which can be difficult to tune
    *   PaaS solutions provided by [Amazon EMR](https://aws.amazon.com/emr/), [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) and [Google Dataproc](https://cloud.google.com/dataproc/)
    *   Commercial support provided by [Hortonworks](https://hortonworks.com/) and [Cloudera](https://www.cloudera.com/)


-   **[Apache Spark SQL](https://spark.apache.org/sql/)：** 建立在 Spark 之上的 SQL 计算层
    -   开源
    -   用 Scala 编写
    -   最早以 Shark 为名，出现于 2010 年
    -   需要使用 Spark 集群
    -   更适用于复杂的分析性查询
    -   使用 Scala、Python、Java 或 R 编写自定义 UDFs 非常简单
    -   需要使用 Spark 集群，有时可能很难调谐
    -   [Amazon EMR](https://aws.amazon.com/emr/)、[Azure
        HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) 和
        [Google Dataproc](https://cloud.google.com/dataproc/) 提供 PaaS 解决方案
    -   [Hortonworks](https://hortonworks.com/) 和
        [Cloudera](https://www.cloudera.com/) 提供商业支持



*   **[Apache Flink SQL](https://flink.apache.org/):**  A SQL computing layer that is built on top of Flink
    *   Open source
    *   Written in Java
    *   Released in 2016
    *   Requires a Flink cluster
    *   Custom UDFs are easy to write in Scala or Java
    *   Performance compared to Spark is hard to get numbers for
    *   PaaS solutions provided by [Amazon EMR](https://aws.amazon.com/emr/) and [Google Dataproc](https://cloud.google.com/dataproc/)


-   **[Apache Flink SQL](https://flink.apache.org/)：** 一个建立在 Flink 之上的 SQL 计算层
    -   开源
    -   用 Java 编写
    -   发布于 2016 年
    -   需要 Flink 集群
    -   使用 Scala 或 Java 编写自定义 UDFs 非常简单
    -   性能与 Spark 不相上下
    -   [Amazon EMR](https://aws.amazon.com/emr/) 和 [Google
        Dataproc](https://cloud.google.com/dataproc/) 提供 PaaS 解决方案



*   **[Presto](https://prestodb.io/):** A SQL computing layer optimized for massive datasets
    *   Open source
    *   Written in Java
    *   Released in 2013 by Facebook
    *   More optimized for many smaller OLAP queries
    *   Support for custom Java UDFs
    *   Requires tuning to get good performance
    *   Provides comparable performance to [Redshift](https://engineering.grab.com/scaling-like-a-boss-with-presto)
    *   Performance improvements compared to [Spark](http://tech.marksblogg.com/billion-nyc-taxi-rides-ec2-versus-emr.html) although results may differ on [Databrick’s SaaS Spark](https://databricks.com/blog/2017/07/12/benchmarking-big-data-sql-platforms-in-the-cloud.html)
    *   Used by Facebook to query their 300PB data warehouse
    *   PaaS version in [Amazon Athena](https://aws.amazon.com/athena/)


-   **[Presto](https://prestodb.io/):** 针对海量数据集打造的 SQL 计算层
    -   开源
    -   用 Java 编写
    -   Facebook 于 2013 年发布
    -   更适用于大量较小的 OLAP 查询
    -   支持使用 Java 编写自定义 UDFs
    -   需要调谐以获得良好的性能
    -   性能与
        [Redshift](https://engineering.grab.com/scaling-like-a-boss-with-presto)
        相当
    -   性能比
        [Spark](http://tech.marksblogg.com/billion-nyc-taxi-rides-ec2-versus-emr.html)
        有进一步优化。与 [Databricks 公司的 SaaS 版
        Spark](https://databricks.com/blog/2017/07/12/benchmarking-big-data-sql-platforms-in-the-cloud.html)
        相比，结果可能不同。
    -   被 Facebook 用于查询其 300 PB 的数据仓库
    -   [Amazon Athena](https://aws.amazon.com/athena/) 提供 PaaS 版本



*   **[Apache Impala:](https://impala.apache.org/)** A SQL computing layer released by Cloudera based on Google’s Dremel
    *   Open source
    *   Released in 2012 by Cloudera
    *   Written in C++
    *   Support for custom UDFs in C++ and Java (but Java is slower)
    *   Based on the [Dremel](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36632.pdf) paper by Google
    *   More optimized for many smaller OLAP queries
    *   Commercial support provided by [Cloudera](https://www.cloudera.com/)


-   **[Apache Impala:](https://impala.apache.org/)** 由 Cloudera 发布的，基于 Google Dremel 技术的 SQL 计算层
    -   开源
    -   2012 年由 Cloudera 发布
    -   用 C++ 编写
    -   支持使用 C++ 和 Java 编写自定义 UDFs（但 Java 较慢）
    -   基于 Google 的
        [Dremel](https://static.googleusercontent.com/media/research.google.com/en/pubs/archive/36632.pdf)
        论文
    -   更适用于大量较小的 OLAP 查询
    -   [Cloudera](https://www.cloudera.com/) 提供商业支持


*   **[Amazon Redshift Spectrum:](https://aws.amazon.com/redshift/spectrum/)** A computing engine version of Redshift
    *   Proprietary PaaS
    *   Unlike Redshift can scale computing independently of storage and access arbitrary file formats stored in S3
    *   Limited support for custom UDFs in Python
    *   Can leverage Redshift for table metadata
    *   Required a running Redshift cluster



-   **[Amazon Redshift Spectrum:](https://aws.amazon.com/redshift/spectrum/)** Redshift 的计算引擎版
    -   专有的 PaaS
    -   与 Redshift 不同的是，计算能力可以独立于存储能力而扩展。并支持读取存储于
        S3 上任意格式的文件
    -   为使用 Python 编写自定义 UDFs 提供有限的支持
    -   可以利用 Redshift 管理表元数据
    -   需要使用运行中的 Redshift 集群



## Data Warehouse

## 数据仓库

These are full featured Data Warehouses that tie together the data storage and data processing into a single entity.

数据仓库集数据存储与数据处理于一体


*   **Overall**
    *   Low latency and high throughput query performance but not necessarily faster than other modern batch processing solutions
    *   Columnar data storage
    *   Limits on flexibility (data types, UDFs, data processing approaches, etc.)
    *   Lock-in if used as primary data store
    *   Computing tied to storage system in terms of sc aling


-   **总体**
    -   低延迟和高吞吐量的查询性能，但不一定比其他现代批处理解决方案更快
    -   列式数据存储
    -   灵活度有一定局限（数据类型，UDFs，数据处理方法等）
    -   如果用作主数据仓库，会被套牢
    -   就扩展而言，计算与存储系统密切相关
    

*   **[Druid](http://druid.io/):** Columnar data store designed to provide low-latency analytical queries
    *   Open source
    *   Written in Java
    *   Open sourced in 2012
    *   Provides sub-second analytical/OLAP queries
    *   Supports real-time ingestion of data rather than just batch ingestion
    *   Provides a limited subset of SQL queries (only large to small table joins)
    *   Custom UDF support exists in Java but is complicated
    *   Seamless scaling of the cluster up/down independently of storage
    *   Leverages “deep” storage such as S3 or HDFS to avoid data loss if nodes go down
    *   Complicated infrastructure setup involving multiple types of nodes and distributed storage (S3, HDFS, etc.)
        *   Number of external dependencies (S3/HDFS, ZooKeeper, RDBM) which increases operational overhead
    *   Well suited for time series data
    *   Used by [Airbnb, eBay, Netflix, Walmart and others](http://druid.io/druid-powered.html)

-   **[Druid](http://druid.io/)：** 为提供低延迟分析性查询设计的列式数据仓库
    -   开源
    -   用 Java 编写
    -   2012 年开始开源
    -   提供亚秒级分析性查询、OLAP 查询
    -   支持实时数据摄取，而不仅是批量摄取
    -   提供有限的 SQL 查询子集（仅限于大到小表连接）
    -   支持使用 Java 编写自定义 UDFs，但这很复杂
    -   集群可独立于存储无缝缩放
    -   利用 S3 或 HDFS 等“深度”存储，避免节点失效时的数据丢失
    -   基础构架设置复杂，涉及多种类型的节点和分布式存储（S3、HDFS 等）
        -   数个外部依赖关系（S3/HDFS，ZooKeor，RDBM）增加了操作开销
    -   适用于处理时间序列数据
    -   被
        [Airbnb、eBay、Netflix、沃尔玛](http://druid.io/druid-powered.html)等使用


*    **[ClickHouse](https://clickhouse.yandex/):** Columnar data store designed to provide low-latency analytical queries and simplicity
    *   Open Source
    *   Written in C++
    *   Open sourced in 2016 by [Yandex](https://yandex.com/)
    *   No support for custom UDFs
    *   Significantly [higher performance](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/#comment-3302778860) than Druid for some workloads
    *   Less scalable than Druid or other approaches
    *   Leverages Zookeeper but can run a single node cluster without it


-   **[ClickHouse](https://clickhouse.yandex/)：** 为低延迟分析性查询和简单性而设计的列式数据仓库
    -   开源
    -   用 C++ 编写
    -   2016 年由 [Yandex](https://yandex.com/) 开放源码
    -   不支持自定义 UDFs
    -   对某些工作的[性能明显高于](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/#comment-3302778860)
        Druid
    -   可扩展性不如 Druid 或其他解决方案
    -   使用 Zookeeper， 同时也可以在不用 Zookeeper 的情况下运行单节点集群



*   **[Amazon Redshift](https://aws.amazon.com/redshift/):** A fully-managed data warehouse solution that lets you efficiently store and query data using a SQL syntax.
    *   Proprietary PaaS
    *   General purpose analytical store that support full SQL syntax
    *   Limited support for custom UDFs in Python
    *   Loading/unloading data takes time (hours potentially)
    *   No real time ingestion, only batch, although micro-batches can simulate real-time
    *   Need to explicitly scale the cluster up/down (with write downtime for the duration)
    *   *   Storage and computing are tied together
    *   Lack of complex data types such as arrays, structs, maps or native json



-   **[Amazon Redshift](https://aws.amazon.com/redshift/):** 全托管的数据仓库解决方案，可以使用 SQL
    语法高效地存储和查询数据。
    -   专有的 PaaS
    -   支持所有 SQL 语法，可进行一般的分析存储
    -   为使用 Python 编写自定义 UDFs 提供有限的支持
    -   加载、卸载数据需要时间（有可能数小时）
    -   没有实时摄取，只有批处理，虽然可用微型批次模拟实时
    -   需要明确地调整集群的上行/下限（调整期间，不支持数据写入）
        -   存储和计算是紧密联系在一起的
    -   缺少复杂的数据类型，如数组、结构、映射或本地 JSON



*   **[Google BigQuery](https://cloud.google.com/bigquery/):** A fully-managed data warehouse solution that lets you efficiently store and query data using a SQL syntax.
    *   Proprietary PaaS
    *   General purpose analytical store that support full SQL syntax
    *   Real time ingestion support
    *   Limited support for custom UDFs in Javascript
    *   [Fastest queries than Redshift but more expensive](https://blog.fivetran.com/warehouse-benchmark-dce9f4c529c1)
    *   Unlike Redshift it is serverless and you do not need to manage, scale or pay for a cluster yourself
    *   Supports complex data types (arrays, structs) but not native json


-   **[Google BigQuery](https://cloud.google.com/bigquery/):** 全托管的数据仓库解决方案，可以使用 SQL
    语法高效地存储和查询数据。
    -   专有的 PaaS
    -   支持所有 SQL 语法，可进行一般的分析存储
    -   支持数据实时摄取
    -   为使用 Javascript 编写自定义 UDFs 提供有限的支持
    -   [查询速度比 Redshift
        快，但更贵](https://blog.fivetran.com/warehouse-benchmark-dce9f4c529c1)
    -   与 Redshift
        不同的是，它采取无服务器的方式。你不需要自己管理、缩放集群以及支付集群费用。
    -   支持复杂的数据类型（数组、结构）但不支持原生 JSON



*   **[Azure SQL Data Warehouse:](https://azure.microsoft.com/en-us/services/sql-data-warehouse/)** A fully-managed data warehouse solution that lets you scale computing independently of storage
    *   Proprietary PaaS
    *   General purpose analytical store that support full SQL syntax
    *   No real time ingestion, only batch, although micro-batches can simulate real-time
    *   No real support for custom UDFs (only ones written in SQL)
    *   [Performance may not be the best compared to Redshift](http://sql10.blogspot.com/2017/02/sql-server-vs-azure-data-warehouse-vs.html)
    *   Computing nodes can be scaled independently of storage
    *   Lack of complex data types such as arrays, structs, maps or native json



-   **[Azure SQL Data Warehouse:](https://azure.microsoft.com/en-us/services/sql-data-warehouse/)：** 完全托管的数据仓库解决方案，计算能力可以不依赖于存储空间而独立扩展
    -   专有的 PaaS
    -   支持所有 SQL 语法，可进行一般的分析存储
    -   没有实时摄取，只有批处理，虽然可用微型批次模拟实时
    -   不支持自定义 UDFs（除非使用 SQL 编写）
    -   [与 Redshift
        相比，性能可能不是最好的](http://sql10.blogspot.com/2017/02/sql-server-vs-azure-data-warehouse-vs.html)
    -   计算节点可不依赖于存储节点独立扩展
    -   缺少复杂的数据类型，如数组、结构、映射或本地 JSON



## RDBM

## 关系数据库管理系统

The traditional SQL database may seem an odd choice however, in addition to simply scaling vertically, with [sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture)) and read-replicas it can scale across multiple nodes. In the following points I’m focusing more on these databases as analytical data stores (relatively few large queries) rather than traditional databases (massive numbers of relatively small queries).

传统的 SQL
数据库看上去可能不是个常规的选择。但是，除了简单的纵向扩展，它还可以通过[分片](https://en.wikipedia.org/wiki/Shard_(database_architecture))（sharding）和只读副本（read-replicas）进行跨节点扩展在。后文中，我会更多地将这些数据库作为分析型数据库（相对少量的大型查询），而不是传统数据库（大量的小型查询）来分析。

*   **Overall**
    *   Powerful [ACID](https://en.wikipedia.org/wiki/ACID) guarantees
    *   Row level updates and inserts
    *   Requires structured data however some databases also have support for free form JSON fields
    *   Can scale to handle large data sizes
        *   Vertically: Modern machines can be quite large so even a single machine can store significant data
        *   Horizontally: Sharding is possible although it requires additional manual setup and potentially client logic changes
    *   There are tradeoffs as you scale (ie: queries across partitions or complex queries)
        *   Computing tied to storage system in terms of scaling
        *   Multi-master or automatic failover setups can be tricky to get right so often a single point of failure exists
    *   Used by [Uber](https://eng.uber.com/mysql-migration/) and [Facebook](https://code.facebook.com/posts/190251048047090/myrocks-a-space-and-write-optimized-mysql-database/) to handle massive amounts of data
    *   There are better purpose built technologies if you truly ne ed to scale big

-   **总体**
    -   强有力的 [ACID](https://en.wikipedia.org/wiki/ACID)
        保证（译者注：Atomicity 原子性、Consistency 一致性、Isolation
        隔离性、Durability 耐久性）
    -   行级更新和插入
    -   需要结构化数据。一些数据库也支持自由格式的 JSON 字段
    -   可扩展至大数据规模
        -   纵向上：现代机器的存储空间可以相当大，所以即使一台机器也能存储显著的数据
        -   横向上：能支持分片（Sharding）。虽然需要额外的手动设置和潜在的客户端逻辑更改
    -   进行扩展时，你需要进行权衡（例如：跨分区查询还是复杂查询）
        -   就扩展而言，计算与存储系统密切相关
        -   复杂的多主集群或自动故障转移设置可能会导致系统中存在单点故障
    -   被 [Uber](https://eng.uber.com/mysql-migration/) 和
        [Facebook](https://code.facebook.com/posts/190251048047090/myrocks-a-space-and-write-optimized-mysql-database/)
        采用，进行大数据处理
    -   如果你真的需要扩展规模，还有更好的专用技术可以选择


*   **[MySQL](https://www.mysql.com/)**
    *   Open source; PaaS and enterprise versions exist
    *   Support for JSON data types
    *   Recent support for window functions
    *   Commercial support by [Oracle](https://www.mysql.com/products/) (who owns MySQL), PaaS support by [AWS](https://aws.amazon.com/rds/)

-   **[MySQL](https://www.mysql.com/)**
    -   开源；存在 PaaS 和企业版
    -   支持 JSON 数据类型
    -   新增对窗口函数的支持
    -   [Oracle](https://www.mysql.com/products/)（MySQL
        的拥有者）的商业支持，[AWS](https://aws.amazon.com/rds/) 的 PaaS 支持

*   **[MariaDB](https://mariadb.org/)**
    *   Open source
    *   Originally a fork of MySQL
    *   Supports window function
    *   No JSON data type but native functions for working with JSON
    *   Support for a [columnar](https://mariadb.com/products/technology/columnstore) storage engine which significantly speeds up analytical workloads
    *   Commercial support by [MariaDB](https://mariadb.com/), PaaS support by [AWS](https://aws.amazon.com/rds/)

-   **[MariaDB](https://mariadb.org/)**
    -   开源
    -   最初是 MySQL 的一个分支
    -   支持窗口函数
    -   无 JSON 数据格式，但有处理 JSON 的原生函数
    -   支持[列式](https://mariadb.com/products/technology/columnstore)存储引擎，显著提升分析速度
    -   [MariaDB](https://mariadb.com/)
        的商业支持，[AWS](https://aws.amazon.com/rds/) 的 PaaS 支持


*   **[PostgreSQL](https://www.postgresql.org/)**
    *   Open source;PaaS and enterprise versions exist
    *   Support for JSON data types
    *   Commercial support by various companies
    *   Better parallel single query optimizations than MySQL
    *   Third party support for [columnar](https://github.com/citusdata/cstore_fdw) storage engine which significantly speeds up analytical workloads
    *   Support for sharding via [PL/Proxy](https://plproxy.github.io/)

-   **[PostgreSQL](https://www.postgresql.org/)**
    -   开源；存在 PaaS 和企业版
    -   支持 JSON 数据类型
    -   拥有多个公司的商业支持
    -   比 MySQL 更好的并行单一查询优化
    -   第三方对[列式](https://github.com/citusdata/cstore_fdw)存储引擎的支持，大大加快了分析速度
    -   支持通过 [PL 或者代理](https://plproxy.github.io/)进行分片（sharding）


*   **[Amazon Aurora:](https://aws.amazon.com/rds/aurora/)** Fully managed MySQL and PostgeSQL compatible databases on AWS
    *   Proprietary PaaS
    *   Automatically and seamlessly allocates storage
    *   Data is replicated across and within availability zones
    *   Claims [improved performance](https://www.percona.com/blog/2016/05/26/aws-aurora-benchmarking-part-2/) compared to open source versions due to tight coupling with the SSD storage layer
        *   PostgreSQL performance may be [lower](https://www.chooseacloud.com/postgresql) on Aurora
    *   Lags behind open source in version support, Aurora MySQL 5.7 support came out over 2 years after MySQL 5.7
    *   Does not support clustering beyond read replicas
    
-   **[Amazon Aurora](https://aws.amazon.com/rds/aurora/)：** 兼容 MySQL 和 PostageSQL 的 AWS 全托管数据库
    -   专有的 PaaS
    -   存储空间自动且无缝分配
    -   数据在所有可使用区域复制
    -   声称对比于开源版，通过与 SSD
        存储层的紧密耦合[提高了性能](https://www.percona.com/blog/2016/05/26/aws-aurora-benchmarking-part-2/)
        -   比 PostgreSQL [更好的](https://www.chooseacloud.com/postgresql)性能
    -   在开源版本的支持方面存在落后。Auro 对 MySQL 5.7 的支持在 MySQL 5.7 之后
        2 年出现
    -   不支持除只读副本外的集群
   
    
