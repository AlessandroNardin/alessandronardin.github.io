---
layout: default
title: Portfolio
---

# About Me

Hi, I'm Alessandro.
Welcome to my website. Here you'll find the projects and experiments I'm most proud to share (or at least the ones I've found the time to upload).

Currently, I'm pursuing a Master's degree in Automation and Robotics Engineering at the University of Pisa. In parallel, I am an Honors Student (Allievo Ordinario) at Scuola Superiore Sant'Anna, a selective path that allows me to dive deeper into advanced topics and spend some extra hours in the lab.
Before moving to Pisa, I earned my Bachelor's degree in Computer, Telecommunications, and Electronics Engineering at the University of Trento, with a strong focus on Computer Engineering.


Note: I might forget to update this section for a while, so for context: this text was written on February 3rd, 2026.

---

# Featured Projects

Here are the projects I’ve worked on. It's a growing list (currently starting with one), but you can view everything on the Projects page.

<div class="projects-grid">
  {% assign shown_projects = 0 %}
  {% for project_page in site.pages %}
    {% if project_page.layout == "project-homepage" and project_page.path contains 'projects/' and shown_projects < 6 %}
      <a href="{{ project_page.url | relative_url }}" class="project-card">
        {% if project_page.thumbnail %}
        <div class="project-thumbnail-link">
          <img src="{{ project_page.url | relative_url }}/{{ project_page.thumbnail }}" alt="{{ project_page.title }} thumbnail" class="project-thumbnail">
        </div>
        {% endif %}
        <div class="project-text">
          <h2 class="project-title">{{ project_page.title }}</h2>
        </div>
      </a>
      {% assign shown_projects = shown_projects | plus: 1 %}
    {% endif %}
  {% endfor %}
</div>

---

# Recent Posts

My latest blog posts. Right now it's mostly about my GSoC experience, but I might write more if I stumble upon something interesting enough to share.

<div class="blog-posts-grid">
  {% for post in site.posts limit:3 %}
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
