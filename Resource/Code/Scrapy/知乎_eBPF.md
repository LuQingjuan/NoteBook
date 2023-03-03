# eBPF
- [ ] [一文看懂eBPF、eBPF的使用（超详细）](https://zhuanlan.zhihu.com/p/480811707)
    [01-30 · 赞同 52]
    Linux内核库：乐高积木就是通过不断向主体添加积木来组合出更庞大的模型。 而 eBPF 就像乐高积木一样，可以不断向内核添加 eBPF 模块来增强内核的功能。 什么是 eBPF eBPF 全称 extended Ber...
- [ ] [ebpf真的有这么强大吗？](https://www.zhihu.com/question/530525662/answer/2673538233)
    [2022-09-14 · 赞同 8]
    乘云 DataBuff：该文章讲述了 eBPF 对可观测性的意义，以及我们为什么要在 OpenTelemetry 的背景下讨论 eBPF 。 一、什么是 eBPF eBPF 是一种允许我们在
- [ ] [我对eBPF的偏见](https://zhuanlan.zhihu.com/p/392926190)
    [2021-07-25 · 赞同 157]
    anonymous：适合饮酒作文。 我并不反对eBPF技术本身，相反，我很喜欢eBPF并且是它的粉丝，我反对的是对eBPF的滥用。 上周听...
- [ ] [目前国内有哪些开源的eBPF项目？](https://www.zhihu.com/question/470578229/answer/2450687763)
    [2022-04-21 · 赞同 5]
    Kindling：drivers和kindling-probe程序之间通信方式 eBPF程序采用BPF MAP 数据结构通信；内核模块采用mmap构造的ringbuffer进行通信。下图是eBPF程序使用的架构模型，为了...
- [ ] [初学者应当怎样学习ebpf？](https://www.zhihu.com/question/441658839/answer/2649335851)
    [2022-08-28 · 赞同 4]
    云微：虚拟机那样的小模块直接编译嵌入其他的大型软件中，提供 eBPF 程序本身的服务；运行和启动时资源占用率都很低； 让 eBPF 程序的分发和使用像网页和 web 服务一样自然（Make eBPF as a servi...
- [ ] [eBPF 完全入门指南.pdf（万字长文）](https://zhuanlan.zhihu.com/p/492185920)
    [2022-04-04 · 赞同 102]
    云原生基地：现在，Linux 内核只运行 eBPF，内核会将加载的 cBPF 字节码透明地转换成 eBPF 再执行。 eBPF 与 cBP...
- [ ] [Linux 内核中有哪些比较牛逼的设计?](https://www.zhihu.com/question/332710035/answer/2683741643)
    [2022-09-22 · 赞同 84]
    嘭嘭山：另一方面就是我想重点提的eBPF：eBPF(extended Berkeley Packet Filter)是一个用于访问 Linux 内核服务和硬件的新方法。eBPF在linux
- [ ] [聊聊最近很火的eBPF](https://zhuanlan.zhihu.com/p/182344856)
    [2020-08-13 · 赞同 155]
    iyacontrol：如何编写一个eBPF程序？ 在很多情况下，不是直接使用eBPF，而是通过Cilium，bcc或bpftrace等项目...
- [ ] [如果评价 BPF (Berkeley Packet Filter) 技术？](https://www.zhihu.com/question/361469669/answer/2244070365)
    [2021-11-26 · 赞同 10]
    helight：gobpf 包，它提供了和 eBPF VM 交互的支持（加载程序到内核，访问/操作 eBPF map 以及其它功能）。大量的 eBPF 程序都可以直接由 C 编写
- [ ] [聊聊风口上的 eBPF](https://zhuanlan.zhihu.com/p/343376492)
    [2021-05-07 · 赞同 41]
    又拍云：今天分享的主题是《eBPF 探索之旅》，围绕三部分展开： eBPF 是什么 eBPF 能做什么 如何编写 eBPF 程序 认识 eBPF...
- [ ] [ebpf 让主机安全成了一个笑话?](https://www.zhihu.com/question/522855742/answer/2829841026)
    [01-04 · 赞同]
    Kane Gong：ebpf加载是要root权限的，如果已经是root了，不管用不用ebpf，数据都可以被拦截
- [ ] [Ebpf简介](https://www.zhihu.com/zvideo/1311665394051174400)
    [2020-11-16 · 赞同 7]
    
- [ ] [超详细干货！eBPF入门与实践指南](https://zhuanlan.zhihu.com/p/533747093)
    [2022-06-25 · 赞同 5]
    Linux嵌入式：现在，Linux 内核只运行 eBPF，内核会将加载的 cBPF 字节码透明地转换成 eBPF 再执行。 eBPF 与 cBPF eBPF 新的设计针对现代硬件进行了优化
- [ ] [一文详解用eBPF观测HTTP](https://zhuanlan.zhihu.com/p/551257831)
    [2022-08-08 · 赞同 37]
    阿里开发者：作为阿里内外千万实例可观测数据的采集器，eBPF 网络可观测特性也预计会在未来8月发布。下文主要基于eBPF观测HTTP 1、HTTP 1.1以及HTTP2的角度介绍eBPF的针对可观测场景的应用...
- [ ] [xdp/ebpf上手](https://www.zhihu.com/zvideo/1345502794808332288)
    [2021-02-17 · 赞同]
    知乎可以把文章自动生成为视频，挺有意思
- [ ] [eBPF 和 WebAssembly：哪种虚拟机将制霸云原生时代?](https://zhuanlan.zhihu.com/p/446006811)
    [2021-12-16 · 赞同 33]
    WasmEdge：有两个轻量级代码执行沙箱/虚拟机非常火热： eBPF 和 WebAssembly。二者都能够运行由 C、C++ 和 Rust 编译而来的高性能字节码程序。 然而，最大的区别在于 eBPF 在 Linux...
- [ ] [如何评价下一代web框架fresh？](https://www.zhihu.com/question/537802407/answer/2560977304)
    [2022-07-07 · 赞同 77]
    黄祖荣：至于传统意义上的Web开发，最简单的出路就是转Go，走DevOps路线； 最有前途的出路还是学习eBPF相关的知识，将微服务化所需的...
- [ ] [五分钟入门 eBPF](https://zhuanlan.zhihu.com/p/603051777)
    [02-03 · 赞同]
    开源Linux：LLVM这样的编译器套件可以用来将伪 C 代码编译成 eBPF 字节码。 eBPF Maps使 eBPF 能够共享获取的信息并保存状态。因此，eBPF 程序可以利用 eBPF 映射来维护和检索各种格式的数...
- [ ] [一文搞懂eBPF技术的底层细节](https://zhuanlan.zhihu.com/p/549056789)
    [2022-08-02 · 赞同 1]
    嵌入式Linux内核：BPF 和 eBPF 在该系列中会交替使用。 第 1 部分和第 2 部分为新人或那些希望通过深入了解 eBPF 技术栈的底层技术来进一步了解 eBPF 技术的人提供了深入介绍
- [ ] [eBPF 介绍](https://www.zhihu.com/zvideo/1384978323236364289)
    [2021-06-06 · 赞同 3]
    
- [ ] [ebpf：先放一放](https://zhuanlan.zhihu.com/p/500843227)
    [2022-04-18 · 赞同 2]
    大川搬砖：前面写了几篇关于 libbpf-bootstrap 的文章。现在决定先放下对 ebpf 的研究。为什么？因为有些想法我短时间内无法实现。 下面首先说一下我的背景。
- [ ] [为什么ebpf干了好多不是过滤包的事情?](https://www.zhihu.com/question/543102221/answer/2573574318)
    [2022-07-14 · 赞同]
    沉默的猴子：因为它就是在kernel code的一个位置，插入一段额外的程序执行，kernel code范围很广，插入的程序行为多种多样，当...
- [ ] [云原生网络利器--Cilium 之 eBPF 篇](https://zhuanlan.zhihu.com/p/475638461)
    [2022-03-04 · 赞同 9]
    DaoCloud 道客：也支持了 eBPF 类型 Hook，在一些 Hook 点执行挂载的 eBPF 程序。在不同的挂载点，支持不同类型的 eBPF 程序类型。 为什么 eBPF 会有类型
- [ ] [一文入门前景广阔的 eBPF](https://zhuanlan.zhihu.com/p/567596888)
    [2022-09-23 · 赞同]
    云原生之家：刚好有eBPF,就会触发事件，并由加载的eBPF程序处理 4、eBPF的不足 但是我们要知道的是eBPF不是万能的，受限于本身内核版本支持能力、eBPF指令的种类、eBPF虚拟机结构等
- [ ] [eBPF学习过程中的疑惑](https://zhuanlan.zhihu.com/p/556628601)
    [2022-09-05 · 赞同]
    王瑞期：网上及书籍的介绍，都是基于某种eBPF的开发库或者框架来介绍说明的，到底和内核中的eBPF是什么关系呢？又比如，cilium/ebpf...
- [ ] [eBPF可观测摄像头带你5分钟真正看懂ForkJoin的分而治之，有什么隐藏的坑](https://www.zhihu.com/zvideo/1574002349651300352)
    [2022-11-10 · 赞同]
    ForkJoin子任务的计算量拆分到多少才算合理？为什么你用了ForkJoin反而降低性能？ 大量线程并行，如何规避线程阻塞？ 虽知“先fork再join”，但谁负责join？有什么坑需要注意？ ForkJoinP...
- [ ] [说说 eBPF 的超能力](https://zhuanlan.zhihu.com/p/589824699)
    [2022-12-08 · 赞同]
    开源Linux：这看起来是一个完美的事件。 一个eBPF示例 为了更具体一点，我将在这里展示一个示例。这将是 eBPF 的 Hello World。这是我的 eBPF 程序。实际的 eBPF 程序就是这里的这几行代码...
- [ ] [eBPF 和 WebAssembly 虚拟机在云原生时代的发展如何？](https://www.zhihu.com/question/558643924/answer/2888629302)
    [02-11 · 赞同 3]
    云微：WebAssembly 中使用 eBPF 程序，我们不仅能让 Wasm 应用享受到 eBPF 的高性能和对系统接口的访问能力，还可以...
- [ ] [关于 eBPF 的一些粗浅理解](https://zhuanlan.zhihu.com/p/463337245)
    [2022-02-27 · 赞同 36]
    兰新宇：呈现的正是 eBPF maps 作为用户态和内核态共享数据的方式（当然它也可以作为 eBPF 的内核态程序之间进行数据交互的渠道）。 这里就要说到 eBPF 的一个优势了
- [ ] [告别 Sidecar——使用 eBPF 解锁内核级服务网格](https://zhuanlan.zhihu.com/p/443585901)
    [2021-12-10 · 赞同 83]
    Jimmy Song：而且所有代理都需要大量的额外内存。在这篇文章的后面，我们将研究这两点，因为我们将其与基于 eBPF 的模型进行比较。 用 eBPF 解锁内核服务网格 为什么我们以前没有在内核中创建一个服务网格...
- [ ] [Microsoft 宣布新的开源项目 eBPF for Windows](https://zhuanlan.zhihu.com/p/371629376)
    [2021-05-12 · 赞同 3]
    OSCHINA：发布了新的开源项目 eBPF for Windows，以使 eBPF 在 Windows 10 和 Windows Server 2016 及更高版本上工作。 eBPF 是 kernel
- [ ] [所以ENFP到底是什么样的人呢？](https://www.zhihu.com/zvideo/1495802640554106880)
    [2022-04-08 · 赞同 1]
    
- [ ] [Linux内核超级装备eBPF技术详细研究](https://zhuanlan.zhihu.com/p/571304331)
    [2022-10-07 · 赞同 18]
    杨剑：bpftrace这些框架来编写eBPF程序。如今,也可以采用Golang，Rust和Python的框架进行eBPF编程。 eBPF的应用 eBPF是一个非常重要的将内核态功能映射到用户态的技术
- [ ] [你应该给eBPF一个机会](https://zhuanlan.zhihu.com/p/485998813)
    [2022-03-23 · 赞同 1]
    Kindling：简而言之，这就是eBPF ! 现在你已经对eBPF有了一个大致的了解，让我们回到一开始的问题：你为什么应该给eBPF一个机会。 原因1：有时候，只有eBPF才能完成你所需的工作
- [ ] [什么是eBPF](https://zhuanlan.zhihu.com/p/378766217)
    [2022-07-17 · 赞同 24]
    IT技术问答：或者保存一些统计信息，从内核态传递给用户态程序。 最后，eBPF 可以处理更多的内核事件，不再只局限在网络事件上。你可以这样...
- [ ] [eBPF 入门之初体验](https://zhuanlan.zhihu.com/p/347239769)
    [2021-01-27 · 赞同 12]
    Feisky：eBPF 提供了强大的跟踪、探测以及高效内核网络等功能，但由于其接口处于操作系统底层，新手入门起来还是有很大难度。幸好，eBPF...
- [ ] [云原生网络利器--Cilium 之 eBPF 篇](https://zhuanlan.zhihu.com/p/475405931)
    [2022-03-03 · 赞同 5]
    云原生基地：也支持了 eBPF 类型 Hook，在一些 Hook 点执行挂载的 eBPF 程序。在不同的挂载点，支持不同类型的 eBPF ...
- [ ] [eBPF 入门之编程](https://zhuanlan.zhihu.com/p/347241870)
    [2021-02-01 · 赞同 7]
    Feisky：特别是如何编写 eBPF 程序是入门的一大难点。本文将介绍一些常用的 eBPF 编程框架。 BCC 上篇文章介绍的 BCC ...
- [ ] [深入浅出eBPF｜你要了解的7个核心问题](https://zhuanlan.zhihu.com/p/529766164)
    [2022-06-17 · 赞同 12]
    阿里云云栖号：作为该技术的实践者，本文目标是通过回答7个核心问题介绍eBPF技术本身，为大家解开eBPF的面纱。 eBPF是什么？ eBPF...
- [ ] [eBPF开发指南](https://zhuanlan.zhihu.com/p/449778226)
    [2021-12-25 · 赞同 11]
    Senber：用户态程序和注入到内核中的程序通过共用一个位于内核的 eBPF MAP 实现通信。为了防止注入的代码导致内核崩溃，eBPF ...
- [ ] [eBPF 进阶: 内核新特性进展一览](https://zhuanlan.zhihu.com/p/606384782)
    [02-14 · 赞同 6]
    云微：PostgreSQL 安装并遇到性能降低时。 eBPF 概述：第 5 部分：跟踪用户进程：https://www.ebpf.top/...
- [ ] [LinuxTracing System浅析和eBPF开发经验分享](https://zhuanlan.zhihu.com/p/545539331)
    [2022-09-03 · 赞同 22]
    内核沉思录：bpftrace提供了一种易用的脚本语言来帮助用户快速高效的使用eBPF功能，其背后的原理还是利用LLVM 将脚本转为eBPF字节码。 eBPF用户态代码: 这部分代码负责将eBPF内核程序加载到内核，与eBPF...
- [ ] [eBPF Tracing 入门教程与实例](https://zhuanlan.zhihu.com/p/67273340)
    [2019-05-28 · 赞同 23]
    史努比：至少有24个关于 eBPF 的演讲。 eBPF 这一实用技术，将是每个开发者需要掌握的技巧。 也许你的新年目标得再多一个了：学习 eBPF...
- [ ] [为什么k8s管理员要懂eBPF](https://zhuanlan.zhihu.com/p/599071050)
    [01-14 · 赞同 1]
    码农小军：为什么eBPF在Kubernetes可观测性的革命中变得如此重要。让我们来看看eBPF的历史，它是如何工作的，它解决了哪些问题，以及为什么你应该开始使用它。 什么是eBPF？eBPF简史... eBPF是“ex...
- [ ] [深入浅出 eBPF｜你要了解的 7 个核心问题](https://zhuanlan.zhihu.com/p/538339986)
    [2022-07-08 · 赞同 5]
    云原生基地：本文目标是通过回答 7 个核心问题介绍 eBPF 技术本身，为大家解开 eBPF 的面纱。 eBPF 是什么 eBPF 是一个能...
- [ ] [eBPF 介绍](https://zhuanlan.zhihu.com/p/378258986)
    [2021-06-06 · 赞同 16]
    FOCUS：内核的系统调用，将编译好的 eBPF 字节码加载到内核中。在加载的过程中，内核会对 eBPF 程序进行验证，保证 eBPF 程...
- [ ] [基于eBPF的开源项目](https://zhuanlan.zhihu.com/p/507197444)
    [2022-04-29 · 赞同 2]
    云原生基地：等公司联合成立了eBPF基金会，大力发展eBPF技术。最近几年，eBPF技术在国内也得到了广泛应用，很多大厂也开始关注并采用eBPF...
- [ ] [请暂时抛弃使用 eBPF 取代服务网格和 sidecar 模式的幻想](https://zhuanlan.zhihu.com/p/528156952)
    [2022-06-13 · 赞同 24]
    Jimmy Song：目标都是通过超越系统调用的方式来实现性能提升。 eBPF 不是银弹，你不能用 eBPF 运行任意程序，实际上 eBPF 可以做的事情是非常有限的。 eBPF 的局限性 eBPF 的局限性也是因为内核...
- [ ] [Cilium eBPF实现机制源码分析](https://zhuanlan.zhihu.com/p/446660758)
    [2021-12-31 · 赞同 14]
    陈小鱼：go源码分析 eBPF map初始化 上面提到Cilium Daemon是管理eBPF的模块，那么从这个模块的入口文件开始阅读。 ebpf map是在ebpf prog加载之前
- [ ] [理解eBPF](https://zhuanlan.zhihu.com/p/527384017)
    [2022-06-11 · 赞同]
    谅皮：从内核态获取特定的内核态信息到用户态是eBPF存在的意义。 下面提供个更加详细的eBPF框架图供理解： eBPF的框架图 2、举例说明eBPF...
- [ ] [eHIDS 一款基于eBPF的HIDS开源工具](https://zhuanlan.zhihu.com/p/500076412)
    [2022-04-17 · 赞同]
    明翼： 运行在内核态用C写eBPF代码，llvm编译为eBPF字节码。 用户态使用golang编写，cilium/ebpf纯go类库，做eBPF字节码的内核加载，kprobe/uprobe
- [ ] [eBPF双子座：天使or恶魔？](https://zhuanlan.zhihu.com/p/607981113)
    [02-20 · 赞同 2]
    内核沉思录：增强操作系统的高性能和安全性，也是目前eBPF技术正在深入的领域，所以eBPF自身的安全能力，也是检验该项技术是否有可持续发展...
- [ ] [使用 eBPF 和 XDP 高速处理数据包](https://zhuanlan.zhihu.com/p/438158551)
    [2021-11-26 · 赞同 4]
    helight：gobpf 包，它提供了和 eBPF VM 交互的支持（加载程序到内核，访问/操作 eBPF map 以及其它功能）。大量...
- [ ] [性能诊断工具eBPF](https://zhuanlan.zhihu.com/p/450884927)
    [2021-12-28 · 赞同]
    沃德锅：Linux eBPF Tracing Tool 1 execsnoop 监控通过 exec 执行的新进程。 2 opensnoop ...
- [ ] [深入浅出eBPF｜你要了解的7个核心问题](https://zhuanlan.zhihu.com/p/526476483)
    [2022-06-09 · 赞同 18]
    阿里开发者：作为该技术的实践者，本文目标是通过回答7个核心问题介绍eBPF技术本身，为大家解开eBPF的面纱。 eBPF是什么？ eBPF是一个能够在内核运行沙箱程序的技术，提供了一种在内核事件和用户程序事件发生时安全注...
- [ ] [从零开始的内核eBPF之旅（1）](https://zhuanlan.zhihu.com/p/398158555)
    [2021-08-10 · 赞同 8]
    小安：obj-m是个makefile变量，它的值可以是一串.o文件的表列 EBPF详解（未完待续） 本篇主要叙述了ebpf的学习过程，后面...
- [ ] [运行时安全的利剑-eBPF](https://zhuanlan.zhihu.com/p/507388164)
    [2022-04-29 · 赞同]
    北京探真科技：就不得不提到一个这几年的热门技术 “eBPF”，那么，eBPF到底是什么？为何大家如此重视运行时安全？eBPF与运行时安全有...
- [ ] [初识 eBPF](https://zhuanlan.zhihu.com/p/468402448)
    [2022-02-17 · 赞同 11]
    江川一尾：eBPF 是目前 Linux 平台比较火的技术，前一段时间 Windows 平台也推出了自己的 eBPF for Windows。eBPF 是 BPF 的扩展，BPF（Berkeley
- [ ] [01｜技术概览：eBPF 的发展历程及工作原理](https://zhuanlan.zhihu.com/p/458753388)
    [2022-01-18 · 赞同 4]
    极客时间：也简单介绍了 eBPF 的主要应用场景，包括故障诊断、网络优化、安全控制、性能监控等。那你可能就要问了：为什么 eBPF 可以应用到这么广泛的领域呢？ eBPF 广泛的应用场景和强大的功能
- [ ] [最好的eBPF相关知识整理文章](https://zhuanlan.zhihu.com/p/585529223)
    [2022-11-22 · 赞同]
    王瑞期：绿色记忆:eBPF学习笔记 (gmem.cc) 这篇文章整理的ebpf体系相当清晰，看完就大概知道ebpf的相关知识点了...
- [ ] [eBPF 和可观测性，不得不说的关系](https://zhuanlan.zhihu.com/p/545804866)
    [2022-07-25 · 赞同 10]
    云原生基地：同时一些服务网格产品也在探索使用 eBPF。eBPF 似乎改变了竞争环境。 图片来源：eBPF.io 02 两者的关系 为什么 eBPF 与可观测性相关？ 传统意义上的观测性
- [ ] [讨论一下eBPF](https://zhuanlan.zhihu.com/p/157432039)
    [2020-07-26 · 赞同 39]
    知乎用户G0K17q：本文是思考一个方案具体是否引入eBPF的前置思考，用这个短文建一下高层逻辑。 BPF/eBPF（下面单独谈eBPF）本...
- [ ] [Linux中的eBPF](https://zhuanlan.zhihu.com/p/424170349)
    [2022-02-02 · 赞同 36]
    soolaugust：Linux内核只运行eBPF, 会将传统的cBPF字节码转换成eBPF再执行.而新的eBPF同样可以在之前的Linux版本上使用, 只是部分功能会受到限制. eBPF做了如下的改进
- [ ] [ebpf / xdp 上手](https://zhuanlan.zhihu.com/p/350660795)
    [2021-02-16 · 赞同 5]
    仕明：大年初二。 最近看了一些ebpf和xdp的文章，感觉挺有意思，趁假期就上手试了一下。 ebpf是针对传统bpf的扩展（Extend bpf），在较高版本的kernel里已经默认支持
- [ ] [内核也要可编程？聊聊最近很火的 eBPF](https://zhuanlan.zhihu.com/p/598699662)
    [01-13 · 赞同]
    开源Linux：LLVM这样的编译器套件可以用来将伪 C 代码编译成 eBPF 字节码。 eBPF Maps使 eBPF 能够共享获取的信息并保存状态。因此，eBPF 程序可以利用 eBPF 映射来维护和检索各种格式的数...
- [ ] [eBPF 实现 GPU 虚拟化](https://zhuanlan.zhihu.com/p/546309088)
    [2022-07-26 · 赞同 6]
    lychee：【eBPF概念及应用】 【视频标记点 01:14:08】 eBPF概念及应用_哔哩哔哩_bilibili 来源于中山大学陈鹏飞[1]教授的一次公开分享[2] 。课件如下
- [ ] [eBPF 如何简化服务网格](https://zhuanlan.zhihu.com/p/426834040)
    [2021-10-28 · 赞同 10]
    Jimmy Song：这样它就可以拦截和处理进出应用容器的流量。 引入 eBPF eBPF 是一种内核技术，允许自定义程序在内核中运行。这些程序在响应事件时运行，有成千上万个可能的事件，eBPF 程序可以被附加到这些事件...
- [ ] [ebpf在Android中的应用](https://zhuanlan.zhihu.com/p/380903337)
    [2021-06-16 · 赞同 8]
    赵俊民：1 背景eBPF - Introduction, Tutorials & Community Resources eBPF是...
- [ ] [eBPF 技术报告（下）](https://zhuanlan.zhihu.com/p/529227889)
    [2022-06-15 · 赞同]
    云原生基地：com/ebpf eBPF 技术报告（上） eBPF 技术报告（中） 5. eBPF 在云原生环境中的应 近年来，云计算原生方...
- [ ] [一文入门前景广阔的 eBPF](https://zhuanlan.zhihu.com/p/567375673)
    [2022-09-23 · 赞同]
    开源Linux：刚好有eBPF,就会触发事件，并由加载的eBPF程序处理 4、eBPF的不足 但是我们要知道的是eBPF不是万能的，受限于本身内核版本支持能力、eBPF指令的种类、eBPF虚拟机结构等
- [ ] [首届中国eBPF研讨会有感--我与eBPF结缘](https://zhuanlan.zhihu.com/p/590863180)
    [2022-12-10 · 赞同 3]
    明月悬空：通过XDP技术所要求的eBPF知识，我去研究了eBPF的指令以及它的编译、加载流程，这样我就是从eBPF的指令架构开始了eBPF...
- [ ] [有关于ebpf、istio或者opentelemetry方面的好的英文原版书籍推荐嘛？](https://www.zhihu.com/question/515733882/answer/2426971618)
    [2022-04-07 · 赞同 4]
    Kumhom Mark：逆向工程与云原生现场分析 系列（将）包括： Part 1: eBPF 跟踪 Istio/Envoy 之学步 Part 2: eBPF 跟踪 Istio/Envoy 之启动、监听与线程负载均衡...
- [ ] [一个ebpf的network 示例程序](https://zhuanlan.zhihu.com/p/463342888)
    [2022-02-03 · 赞同 1]
    看这世界多美丽：ebpf 是一个内核子系统，他可以让你在内核中运行你自己的代码，你可以通过高级语言编写代码，然后在ebpf中执行。ebpf可...
- [ ] [一文详解用eBPF观测HTTP](https://zhuanlan.zhihu.com/p/549823163)
    [2022-08-04 · 赞同]
    tcpisopen：作为阿里内外千万实例可观测数据的采集器，eBPF 网络可观测特性也预计会在未来8月发布。下文主要基于eBPF观测HTT...
- [ ] [Linux 内核模块与 eBPF 字节码程序的异同点是什么？](https://www.zhihu.com/question/486116854/answer/2124759063)
    [2021-09-16 · 赞同 3]
    匿名用户：1. eBPF类似一个linux内核态的虚拟机，eBPF它本身就是linux内核的一个模块。 2. eBPF可以在用户态编写对应的...
- [ ] [eBPF的map定义及疑惑](https://zhuanlan.zhihu.com/p/561601231)
    [2022-09-05 · 赞同 3]
    王瑞期：eBPF里面那些预定义的SEC，看得人一头雾水，文档实在太缺乏了。因为一直以来C语言不熟悉，我就没有直接去看源码（也不知道是要看li...
- [ ] [细谈eBPF的机器和字节码(纯技术)](https://zhuanlan.zhihu.com/p/549089588)
    [2022-08-02 · 赞同 1]
    嵌入式Linux内核：不能直接指向任意的内存。所有的内存访问必须在 eBPF 程序中使用之前首先将数据加载到 eBPF 栈。这一限制有助于 eBPF 验证器，它简化了内存模型，使其更容易进行内核检查
- [ ] [【eBPF】使用libbpf开发eBPF程序](https://zhuanlan.zhihu.com/p/596058784)
    [01-02 · 赞同]
    不上岸不改名：学习libbpf有助于理解bcc/bpftrace等功能。eBPF程序的运行流程如图所示： libbpf_ebpf_0 生成eBPF...
- [ ] [linux跟踪技术之ebpf](https://zhuanlan.zhihu.com/p/595190996)
    [2022-12-29 · 赞同]
    合天网安实验室：hook 的效果；通过ebpf,还可以在网络封包到达内核协议栈之前就进行处理，这可以实现流量控制，甚至隐蔽通信。 ebpf追踪 ebpf本质上只是运行在linux
- [ ] [如何评价从 tcpdump 角度看 cBPF/eBPF 程序设计？](https://www.zhihu.com/question/483974234/answer/2583778915)
    [2022-07-20 · 赞同 1]
    嵌入式内核：在《一文看懂eBPF！eBPF实现原理！》一文中，我们介绍了 eBPF 的实现原理，这篇文章我们主要介绍 eBPF 运行加速器 JIT（Just In Time）的实现原理
