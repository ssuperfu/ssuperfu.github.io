---
permalink: /zh/
title: ""
excerpt: ""
author_profile: true
lang: zh
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

我是付超，主要研究方向包括计算机体系结构、片上缓存管理、硬件事务内存、NoC 互连与微体系结构优化。我的工作关注如何通过软硬件协同、缓存与一致性协议设计，以及面向新型应用负载的体系结构机制提升系统性能与能效。

## 代表性论文
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISCA 2026</div><img src='{{ "/images/500x300.png" | relative_url }}' alt="TDMSim publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TDMSim: Enabling High-Density and Energy-Efficient GPU DRAM Caches with 2D-Materials for Data-Intensive Applications](https://conferences.computer.org/iscapub26/pdfs/5065-3nexm57sBmVa6MJtFTiSrb/506501b255/506501b255.pdf)

**Chao Fu**, Jingyang Zheng, Xinliu He, Xiangqi Dong, Zheng Cao, Yuning Zhan, Wenzhong Bao, Peng Zhou, Jun Han

- 该工作连接二维材料器件与 GPU 体系结构，通过保留感知的缓存设计提升性能与能效。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FPL 2024</div><img src='{{ "/images/500x300.png" | relative_url }}' alt="Chimera publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Chimera: A co-simulation framework combining with gem5 and FPGA platform for efficient verification](https://ieeexplore.ieee.org/abstract/document/10705631/)

**Chao Fu**, Zengshi Wang, Jun Han

- 该工作紧密结合软件仿真与硬件仿真，加速 RTL 设计的 SoC 级评估流程。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TPDS</div><img src='{{ "/images/500x300.png" | relative_url }}' alt="Losatm publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Losatm: A hardware transactional memory integrated with a low-overhead scenario-awareness conflict manager](https://ieeexplore.ieee.org/abstract/document/9893383)

**Chao Fu**, Li Wan, Jun Han

- 该工作以低硬件开销自适应协调冲突处理，提升多核并发执行效率。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCAD</div><img src='{{ "/images/500x300.png" | relative_url }}' alt="Homonoia publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Homonoia: Reinventing underutilized cross-level cache resource using reinforcement learning](https://ieeexplore.ieee.org/abstract/document/11363629)

**Chao Fu**, Li Wan, Yufan Jia, Zhiyuan Zhang, Kanheng Jiang, Jun Han

- 该工作利用强化学习重用未充分利用的片上缓存资源，为缓存敏感应用扩展 LLC 容量。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCAD</div><img src='{{ "/images/500x300.png" | relative_url }}' alt="PCMT publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PCMT: Prioritizing Coherence Message Types for NoC Protocol-level Deadlock Freedom](https://ieeexplore.ieee.org/abstract/document/11142878)

Yufan Jia, Zhiyuan Zhang, **Chao Fu(corresponding author)**, Li Wan, Jun Han

- 该工作通过一致性消息优先级摆脱虚拟网络依赖，高效解决 NoC 协议级死锁。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TACO</div><img src='{{ "/images/500x300.png" | relative_url }}' alt="Thoth publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Thoth: Uncovering Data-Dependent Memory Access Patterns via Annotation-Directed Load Sampling](https://dl.acm.org/doi/pdf/10.1145/3806835)

Kanheng Jiang, Yongxin Lyu, Zhiyuan Zhang, Zengshi Wang, **Chao Fu(corresponding author)**, Jun Han

- 该工作通过注解导向的 load 采样识别不规则数据依赖访存模式，并提升硬件预取效果。
</div>
</div>
