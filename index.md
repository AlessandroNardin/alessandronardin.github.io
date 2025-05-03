---
layout: default
title: Portfolio
---

# About Me

**Hi, I'm Alessandro!**  
I am a **Computer Engineering student** at the **University of Trento**, currently pursuing my bachelor’s degree. At the moment, I am on an **Erasmus exchange** at **DTU in Denmark**, where I am taking courses and working on my bachelor thesis.

I am passionate about **robotics** and **embedded systems**, and one of my proudest achievements is being selected for **Google Summer of Code 2024**, where I contributed to **RTEMS**, an embedded operating system.

---

# Featured Projects

Here are a few of the projects I've worked on. Head to the project page for the complete list.

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

Check out my latest blog posts below — visit the blog page for the full archive.

<div class="blog-posts-grid">
  {% for post in site.posts limit:3 %}
    {% assign thumbnail_path = post.path | append: '/../../resources/thumbnail.jpg' %}
    <div class="blog-post-card">
      <img class="blog-thumbnail" src="{{ thumbnail_path | relative_url }}" alt="Post Thumbnail">
      <div class="blog-content">
        <h2 class="blog-title">
          <a href="{{ post.url | absolute_url }}">
            {% if post.path contains 'gsoc' %}**GSoC -** {% endif %}{{ post.title }}
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
