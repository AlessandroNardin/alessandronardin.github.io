---
layout: page
title: Projects
---

On this page, you'll find all the projects I consider worth sharing. Feel free to explore, give feedback, or reach out if something sparks your interest!


<div class="projects-grid">
  {% for project_page in site.pages %}
    {% if project_page.layout == "project-homepage" and project_page.path contains 'projects/' %}
      <a href="{{ project_page.url | relative_url }}" class="project-card">

        {% if project_page.thumbnail %}
        <div class="project-thumbnail-link">
          <img src="{{ project_page.url | relative_url }}/{{ project_page.thumbnail }}" alt="{{ project_page.title }} thumbnail" class="project-thumbnail">
        </div>
        {% endif %}

        <div class="project-text">
          <h2 class="project-title">
            {{ project_page.title }}
          </h2>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>


