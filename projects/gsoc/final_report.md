---
layout: project-page
title: Google Summer of Code 2024 - Final Report
---

{%
include banner.html
class="banner-green"
content="
## Post-GSoC Update

Following the official end of GSoC, I continued working to complete tasks that were not finished during the summer. Below is an updated table outlining the status of all the unfinished contributions.

| Contribution                      | Status     | Related MR                                                                                       | Blog Posts |
|----------------------------------|:----------:|--------------------------------------------------------------------------------------------------|:----------:|
| Implement `lio_listio()`         | Completed  | [!188](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/188)                           | -          |
| Implement `aio_suspend()`        | Completed  | [!275](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/275)                           | -          |
| Update documentation             | Completed  | [!56](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/56), [!26](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/26), [!44](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/44), [!97](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/97) | [link](https://alessandronardin.github.io/projects/gsoc/2024/06/11/docs_update/) |
"
%}

# Project Summary

My project for the **2024 edition of Google Summer of Code** was done in collaboration with the **RTEMS Project**. RTEMS (Real-Time Executive for Multiprocessor Systems) is a real-time operating system (RTOS) designed for embedded systems. (More information can be found on the [Project Page](https://www.rtems.org/))

The goal of my project was to improve the **POSIX compliance** of the OS, specifically by working on the **Asynchronous Input/Output (AIO)** interface. My objective was to correct behaviors that did not comply with POSIX specifications and to implement missing features.

# My Contributions

Overall, I’m satisfied with the work I accomplished this summer. Most of the tasks I planned have been successfully completed, although not all have been merged. There was more work than anticipated to implement missing features and correct issues in the existing functions. This, combined with an unexpected and difficult-to-diagnose error, led to my delay in fully completing `lio_listio()`. However, I plan to continue contributing even after GSoC to finish what I started.

Below is a table summarizing all completed and planned contributions. After the table, you'll find a brief description of each contribution. For more detailed information, see the linked blog posts, which provide insights into the implementation and challenges.

| Contribution                      | Status         | Related MR                                                                                       | Blog Posts |
|----------------------------------|:--------------:|--------------------------------------------------------------------------------------------------|:----------:|
| Review and merge existing patches| Completed      | [!40](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/40), [!41](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/41), [!42](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/42) | [link](https://alessandronardin.github.io/projects/gsoc/2024/06/04/patch_review/) |
| Correct the behavior of `aio_return()` and `aio_error()` | Completed | [!85](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/85) | [link](https://alessandronardin.github.io/projects/gsoc/2024/06/25/error_return_correction/) |
| Add support for `O_DSYNC` in `aio_fsync()` | Completed | [!128](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/128) | [link](https://alessandronardin.github.io/projects/gsoc/2024/08/02/dsync/) |
| Add notification at request completion | Completed | [!118](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/118) | [link](https://alessandronardin.github.io/projects/gsoc/2024/07/24/notification/) |
| Implement `lio_listio()`         | Work in Progress | [!188](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/188) | - |
| Implement `aio_suspend()`        | Not Started    | -                                                                                                | - |
| Update documentation             | Completed      | [!56](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/56), [!26](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/26), [!44](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/44) | [link](https://alessandronardin.github.io/projects/gsoc/2024/06/11/docs_update/) |

### Review and Merge Existing Patches

This was my first contribution. I began by reviewing patches provided by my mentor to assess their relevance. This task didn’t involve writing much code, aside from fixing minor formatting issues. However, it helped me learn the RTEMS workflow and contribution process.

### Correct the Behavior of `aio_return()` and `aio_error()`

This task aimed to correct the behavior of these functions, which were previously callable multiple times for the same operation—a violation of POSIX. The fix ensured correct behavior in line with the specification.

### Add Support for `O_DSYNC` in `aio_fsync()`

The goal here was to implement support for the `O_DSYNC` flag in the `aio_fsync()` function. The function previously only accepted one synchronization type, so this update made it compliant with POSIX expectations.

### Add Notification at Request Completion

POSIX requires the `sigevent` field in the **aiocb** structure to generate a notification when an I/O request completes. This field was previously ignored in RTEMS, so I implemented the necessary logic to support it.

### Implement `lio_listio()`

This task involved implementing the missing `lio_listio()` function. The core work is mostly complete, but one issue remains unresolved before it can be merged.

### Implement `aio_suspend()`

I planned to work on this after completing `lio_listio()`, but due to delays with that task, I wasn’t able to start it during the GSoC period.

### Update Documentation

This contribution includes updates to both **Doxygen** comments and the **RTEMS API documentation**, improving clarity and completeness.

# What I Learned

This experience has been an invaluable learning opportunity. Before this summer, my programming experience was mostly limited to academic projects. These were small, short-lived, and often didn’t require tools like version control or professional debugging techniques.

Working on the **RTEMS project** was a completely different challenge. The large codebase forced me to improve my Git skills, learn proper debugging methods, and understand the importance of writing well-tested, maintainable code. I also had to write and run test coverage analysis ([Dedicated Post about coverage](https://alessandronardin.github.io/projects/gsoc/2024/08/02/coverage/)).

I greatly improved my ability to understand unfamiliar code. When I first applied, I couldn’t fully grasp RTEMS project proposals. Now, I understand much of the structure, especially in the AIO area, and can follow conversations within the community.

Overall, GSoC helped me grow as a developer. I now feel more confident in my ability to contribute to large projects and to produce high-quality, collaborative code. These skills will be invaluable in my future career.
