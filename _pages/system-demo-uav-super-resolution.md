---
permalink: /systems-demos/uav-super-resolution/
title: "Edge-side super-resolution for UAV scenarios"
excerpt: "A lightweight edge-side vision system for UAV imagery enhancement."
author_profile: true
---

<article class="demo-post" markdown="1">

<figure class="demo-post__cover">
  <img src='{{ "/images/500x300.png" | relative_url }}' alt="Edge-side super-resolution for UAV scenarios">
</figure>

# Edge-side super-resolution for UAV scenarios

<div class="demo-post__meta">
  <span><i class="fas fa-calendar-alt" aria-hidden="true"></i> Demo system</span>
  <span><i class="fas fa-user" aria-hidden="true"></i> Chao Fu</span>
  <span><i class="fas fa-microchip" aria-hidden="true"></i> Edge AI</span>
</div>

<div class="demo-post__tags">
  <span># edge-ai</span><span># super-resolution</span><span># uav</span>
</div>

<div class="demo-post__toc" markdown="1">
**Table of Contents**

- [Overview](#overview)
- [System Design](#system-design)
- [Demo Highlights](#demo-highlights)
</div>

## Overview

This demo targets UAV scenarios where visual input is often bandwidth-limited, compressed, or captured under challenging operating conditions. The system performs edge-side super-resolution to improve visual quality before downstream perception or human inspection.

<figure class="demo-gif">
  <img src="{{ '/images/uav-super-resolution-demo.gif' | relative_url }}" alt="Edge-side super-resolution demo animation">
  <figcaption>Overview animation of the edge-side UAV super-resolution workflow.</figcaption>
</figure>

## System Design

The pipeline is organized around low-latency inference, constrained memory use, and deployability on edge platforms. It is intended to evaluate how model design, memory behavior, and system scheduling interact in a realistic UAV workload.

## Demo Highlights

- Enhances low-resolution UAV imagery at the edge.
- Supports architecture-aware evaluation of vision workloads.
- Provides a concrete deployment target for studying efficient intelligent systems.

<p class="demo-post__back"><a href="{{ '/systems-demos/' | relative_url }}"><i class="fas fa-arrow-left" aria-hidden="true"></i> Back to System & Demos</a></p>

</article>
