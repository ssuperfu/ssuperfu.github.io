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

## 关于我

我是**傅超**，现任**复旦大学绍兴研究院副研究员**。我博士毕业于**复旦大学**，导师为 [**韩军教授**](https://icmne.fudan.edu.cn/2c/af/c48925a732335/page.htm)。

我的研究聚焦于**面向具身智能部署的计算机体系结构与系统级设计**。围绕这一目标，我的研究方向包括：
  - 基于 Chiplet 的异构体系结构探索与 ESL 设计方法；
  - 面向异构 SoC 的存储系统与缓存一致性机制；
  - 面向具身智能系统的大模型端到端部署与领域专用体系结构。

总体而言，我关注先进计算机体系结构如何支撑**可扩展、高效、可部署的智能系统**。

我也重视**应用驱动和产学研结合的研究**，相关演示系统包括：
  - **面向无人机场景的边缘侧超分辨率系统** [演示]({{ '/zh/systems-demos/uav-super-resolution/' | relative_url }})；
  - **边缘平台上的交互式实时 VSLAM 渲染系统** [演示]({{ '/zh/systems-demos/realtime-vslam-rendering/' | relative_url }})；
  - **面向具身智能的软硬件在环系统** [演示]({{ '/zh/systems-demos/embodied-ai-hil/' | relative_url }})。

## 代表性论文
<p class="section-intro">
  <strong>Someone</strong> 表示第一作者；<strong>Someone<sup>†</sup></strong> 表示共同一作；<strong><u>Someone</u></strong> 表示通讯作者。
</p>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISCA 2026</div><img src='{{ "/images/isca_2026.png" | relative_url }}' alt="TDMSim publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TDMSim: Enabling High-Density and Energy-Efficient GPU DRAM Caches with 2D-Materials for Data-Intensive Applications](https://conferences.computer.org/iscapub26/pdfs/5065-3nexm57sBmVa6MJtFTiSrb/506501b255/506501b255.pdf)

**傅超<sup>†</sup>**, Jingyang Zheng<sup>†</sup>, Xinliu He, Xiangqi Dong, Zheng Cao, Yuning Zhan, Wenzhong Bao, Peng Zhou, Jun Han

- 该工作连接二维材料器件与 GPU 体系结构，通过保留感知的缓存设计提升性能与能效。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FPL 2024</div><img src='{{ "/images/fpl_2024.png" | relative_url }}' alt="Chimera publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Chimera: A co-simulation framework combining with gem5 and FPGA platform for efficient verification](https://ieeexplore.ieee.org/abstract/document/10705631/)

**傅超**, Zengshi Wang, Jun Han

- 该工作紧密结合软件仿真与硬件仿真，加速 RTL 设计的 SoC 级评估流程。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TPDS 2022</div><img src='{{ "/images/tpds_2022.png" | relative_url }}' alt="Losatm publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Losatm: A hardware transactional memory integrated with a low-overhead scenario-awareness conflict manager](https://ieeexplore.ieee.org/abstract/document/9893383)

**傅超**, Li Wan, Jun Han

- 该工作以低硬件开销自适应协调冲突处理，提升多核并发执行效率。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCAD 2025</div><img src='{{ "/images/tcad_2025_2.png" | relative_url }}' alt="Homonoia publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Homonoia: Reinventing underutilized cross-level cache resource using reinforcement learning](https://ieeexplore.ieee.org/abstract/document/11363629)

**傅超**, Li Wan, Yufan Jia, Zhiyuan Zhang, Kanheng Jiang, Jun Han

- 该工作利用强化学习重用未充分利用的片上缓存资源，为缓存敏感应用扩展 LLC 容量。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCAD 2025</div><img src='{{ "/images/tcad_2025_1.png" | relative_url }}' alt="PCMT publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PCMT: Prioritizing Coherence Message Types for NoC Protocol-level Deadlock Freedom](https://ieeexplore.ieee.org/abstract/document/11142878)

Yufan Jia, Zhiyuan Zhang, **<u>傅超</u>**, Li Wan, Jun Han

- 该工作通过一致性消息优先级摆脱虚拟网络依赖，高效解决 NoC 协议级死锁。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TACO 2026</div><img src='{{ "/images/taco_2026.png" | relative_url }}' alt="Thoth publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Thoth: Uncovering Data-Dependent Memory Access Patterns via Annotation-Directed Load Sampling](https://dl.acm.org/doi/pdf/10.1145/3806835)

Kanheng Jiang, Yongxin Lyu, Zhiyuan Zhang, Zengshi Wang, **<u>傅超</u>**, Jun Han

- 该工作通过注解导向的 load 采样识别不规则数据依赖访存模式，并提升硬件预取效果。
</div>
</div>
