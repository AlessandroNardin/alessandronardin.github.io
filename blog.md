---
layout: page
title: Blog
---

<p>On this page, you'll find all the posts I've published, listed in reverse chronological order with the most recent at the top.</p>

<div class="blog-posts-grid">
  {% for post in site.posts %}
    {% assign thumbnail_path = post.path | append: '/../../resources/thumbnail.jpg' %}

    <div class="blog-post-card">
      <img class="blog-thumbnail" src="{{ thumbnail_path | relative_url }}" alt="Post Thumbnail">

      <div class="blog-content">
        <h2 class="blog-title">
          <a href="{{ post.url | absolute_url }}">
            {% if post.path contains 'gsoc' %}GSoC - {% endif %}{{ post.title }}
          </a>
        </h2>
        <div class="blog-date">{{ post.date | date: "%B %d, %Y" }}</div>
        <p class="blog-excerpt">
          {{ post.excerpt | strip_html | truncatewords: 30 }}
        </p>
        <a class="blog-link" href="{{ post.url | absolute_url }}">Read more →</a>
      </div>
    </div>
  {% endfor %}
</div>
