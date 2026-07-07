---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

## About Me

I am **Chao Fu**, an Associate Researcher at **Shaoxin Laboratory, Fudan University**. I received my Ph.D. from **Fudan University**, where I was advised by [**Prof. Jun Han**](https://icmne.fudan.edu.cn/2c/af/c48925a732335/page.htm).

My research focuses on **computer architecture and system-level design for embodied AI deployment**.
To this end, my research span:
  - Chiplet-based heterogeneous architecture exploration and ESL design methodologies;
  - Memory systems and cache coherence for heterogeneous SoCs;
  - End-to-end deployment of LLMs and domain-specific architectures for embodied AI systems.

My research broadly explores how advanced computer architectures can support **scalable, efficient, and deployable intelligent systems**.

I also emphasize **application-driven and industry-academia-oriented research**, with demo systems including:
  - **Edge-side super-resolution for UAV scenarios** [**[demo details]**]({{ '/systems-demos/uav-super-resolution/' | relative_url }});
  - **Interactive real-time VSLAM rendering on edge platforms** [**[demo details]**]({{ '/systems-demos/realtime-vslam-rendering/' | relative_url }});
  - **Hardware-software-in-the-loop systems for embodied AI** [**[demo details]**]({{ '/systems-demos/embodied-ai-hil/' | relative_url }}).


<!-- (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=idFeW10AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->

## Selected Publications
<p class="section-intro">
  <strong>Someone</strong> denotes first authors; <strong>Someone<sup>†</sup></strong> denotes equal contributions; <strong><u>Someone</u></strong> denotes corresponding authors.
</p>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISCA 2026</div><img src='{{ "/images/isca_2026.png" | relative_url }}' alt="TDMSim publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TDMSim: Enabling High-Density and Energy-Efficient GPU DRAM Caches with 2D-Materials for Data-Intensive Applications](https://conferences.computer.org/iscapub26/pdfs/5065-3nexm57sBmVa6MJtFTiSrb/506501b255/506501b255.pdf)

**Chao Fu<sup>†</sup>**, Jingyang Zheng<sup>†</sup>, Xinliu He, Xiangqi Dong, Zheng Cao, Yuning Zhan, Wenzhong Bao, Peng Zhou, Jun Han

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- This work bridges 2D-material devices and GPU architecture, achieving substantial performance and energy gains through retention-aware cache design.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FPL 2024</div><img src='{{ "/images/fpl_2024.png" | relative_url }}' alt="Chimera publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Chimera: A co-simulation framework combining with gem5 and FPGA platform for efficient verification](https://ieeexplore.ieee.org/abstract/document/10705631/)

**Chao Fu**, Zengshi Wang, Jun Han

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- This work tightly integrates software simulation and hardware emulation to streamline SoC-level evaluation of RTL designs.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TPDS 2022</div><img src='{{ "/images/tpds_2022.png" | relative_url }}' alt="Losatm publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Losatm: A hardware transactional memory integrated with a low-overhead scenario-awareness conflict manager](https://ieeexplore.ieee.org/abstract/document/9893383)

**Chao Fu**, Li Wan, Jun Han

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- This work adaptively coordinates contention handling to improve multicore concurrency with minimal hardware cost.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCAD 2025</div><img src='{{ "/images/tcad_2025_2.png" | relative_url }}' alt="Homonoia publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Homonoia: Reinventing underutilized cross-level cache resource using reinforcement learning](https://ieeexplore.ieee.org/abstract/document/11363629)

**Chao Fu**, Li Wan, Yufan Jia, Zhiyuan Zhang, Kanheng Jiang, Jun Han

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- This work repurposes underutilized on-chip caches with reinforcement learning to expand LLC capacity for cache-sensitive workloads.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCAD 2025</div><img src='{{ "/images/tcad_2025_1.png" | relative_url }}' alt="PCMT publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PCMT: Prioritizing Coherence Message Types for NoC Protocol-level Deadlock Freedom](https://ieeexplore.ieee.org/abstract/document/11142878)

Yufan Jia, Zhiyuan Zhang, **<u>Chao Fu</u>**, Li Wan, Jun Han

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- This work removes virtual-network dependence by prioritizing coherence messages to resolve NoC protocol-level deadlocks efficiently.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TACO 2026</div><img src='{{ "/images/taco_2026.png" | relative_url }}' alt="Thoth publication preview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Thoth: Uncovering Data-Dependent Memory Access Patterns via Annotation-Directed Load Sampling](https://dl.acm.org/doi/pdf/10.1145/3806835)

Kanheng Jiang, Yongxin Lyu, Zhiyuan Zhang, Zengshi Wang, **<u>Chao Fu</u>**, Jun Han

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- This work uses annotation-directed load sampling to expose irregular data-dependent memory patterns and improve hardware prefetching.
</div>
</div>

