---
permalink: /zh/systems-demos/uav-super-resolution/
title: "面向无人机场景的边缘侧超分辨率系统"
excerpt: "面向无人机图像增强的轻量级边缘侧视觉系统。"
author_profile: true
lang: zh
---

<article class="demo-post" markdown="1">

<figure class="demo-post__cover">
  <img src='{{ "/images/500x300.png" | relative_url }}' alt="面向无人机场景的边缘侧超分辨率系统">
</figure>

# 面向无人机场景的边缘侧超分辨率系统

<div class="demo-post__meta">
  <span><i class="fas fa-calendar-alt" aria-hidden="true"></i> 系统演示</span>
  <span><i class="fas fa-user" aria-hidden="true"></i> 傅超</span>
  <span><i class="fas fa-microchip" aria-hidden="true"></i> 边缘智能</span>
</div>

<div class="demo-post__tags">
  <span># 边缘智能</span><span># 超分辨率</span><span># 无人机</span>
</div>

<div class="demo-post__toc" markdown="1">
**目录**

- [系统概述](#系统概述)
- [系统设计](#系统设计)
- [演示重点](#演示重点)
</div>

## 系统概述

该系统面向无人机场景中常见的带宽受限、压缩传输或成像条件复杂的问题，在边缘侧对低分辨率图像进行超分辨率增强，为后续感知任务或人工判读提供更高质量的视觉输入。

<figure class="demo-gif">
  <img src="{{ '/images/uav-super-resolution-demo.gif' | relative_url }}" alt="无人机场景边缘侧超分辨率系统动图">
  <figcaption>边缘侧无人机超分辨率流程概览动图。</figcaption>
</figure>

## 系统设计

系统流程围绕低时延推理、受限内存使用和边缘平台可部署性组织，用于评估模型设计、存储行为和系统调度在真实无人机视觉负载中的交互影响。

## 演示重点

- 在边缘侧增强低分辨率无人机图像。
- 支持面向视觉负载的体系结构感知评估。
- 为高效智能系统研究提供具体部署目标。

<p class="demo-post__back"><a href="{{ '/zh/systems-demos/' | relative_url }}"><i class="fas fa-arrow-left" aria-hidden="true"></i> 返回系统与演示</a></p>

</article>
