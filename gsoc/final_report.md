---
layout: page
title: Google Summer of Code 2024 - Final Report
---

# Google Summer of Code 2024 - Final Report

## Project Summary 

My project for the 2024 edition of Google Summer of Code was in collaboration with the RTEMS Project. RTEMS (Real-Time Executive for Multiprocessor Systems) is a real-time operating system (RTOS) designed for embedded systems. [Learn more about RTEMS](https://www.rtems.org/).

The goal of my project was to enhance the POSIX compliance of RTEMS, specifically by improving the Asynchronous Input/Output (AIO) interface. My main objectives were to correct behaviors that did not adhere to POSIX specifications and to implement missing features.

## My Contributions

Below is a summary of all completed and planned contributions. The status of each contribution is indicated as "Completed," "WIP" (Work In Progress), or "Not Started." Each contribution also includes the related Merge Requests (MR) and links to blog posts providing more detailed information.

| Contribution                                                        | Status      | Related MR                                                                 | Blog Posts                                                                 |
| :------------------------------------------------------------------ | :---------: | :------------------------------------------------------------------------- | :------------------------------------------------------------------------: |
| Review and merge existing patches                                   | Completed   | [!40](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/40)-[!41](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/41)-[!42](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/42) | [Post 1](https://alessandronardin.github.io/gsoc/2024/06/04/post1/)        |
| Correct the behavior of `aio_return()` and `aio_error()`            | Completed   | [!85](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/85)       | [Post 3](https://alessandronardin.github.io/gsoc/2024/06/25/post3/)        |
| Add support for `O_DSYNC` in `aio_fsync()`                          | Completed   | [!128](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/128)     | [Post 4](#)                                                                |
| Add notification at request completion                              | Completed   | [!118](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/118)     | [Post 5](#)                                                                |
| Implement `lio_listio()`                                            | WIP         | [!188](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/188)     | -                                                                          |
| Implement `aio_suspend()`                                           | Not Started |                                                                            | -                                                                          |
| Update documentation                                                | Completed   | [!56](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/56)-[!26](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/26) | [Post 2](https://alessandronardin.github.io/gsoc/2024/06/11/post2/)        |

### Contribution Details

#### Review and merge existing patches
This was my first contribution to the project. I began by reviewing patches provided by my mentor to determine if they were still relevant and should be merged. Although this task didn't involve much code writing, except for a few formatting corrections, it was invaluable for learning the RTEMS project's workflow and contribution submission process.

#### Correct the behavior of `aio_return()` and `aio_error()`
The goal was to correct the behavior of `aio_return()` and `aio_error()`. These functions could previously be called multiple times for the same operation, violating POSIX specifications, which needed to be corrected.

#### Add support for `O_DSYNC` in `aio_fsync()`
This task involved adding missing functionality to the `aio_fsync()` function. One of the function’s parameters accepts two values specifying the type of synchronization to be performed. However, the function initially only accepted one value, necessitating the addition of support for the other.

#### Add notification at request completion
One of the missing features was notification at request completion. The `aiocb` (Asynchronous Input/Output Control Block) includes a `sigevent` struct, which should be used to generate a notification as per POSIX specifications. This field was previously ignored, so my task was to add the necessary code to utilize this field.

#### Implement `lio_listio()`
This task focused on implementing the missing `lio_listio()` method. Work on this took longer than expected due to a complex error that required considerable time to resolve.

#### Implement `aio_suspend()`
This task involved implementing the missing `aio_suspend()` method. Unfortunately, I could not start this task because completing `lio_listio()` took longer than anticipated.

#### Update documentation
This contribution includes all the merge requests I made to update the documentation, covering both Doxygen comments and the RTEMS API Docs.

## What I Learned

This experience has been an invaluable learning opportunity. Before this summer, my coding experience was limited to school and university projects. I had only worked on small codebases, often entirely written by me, and rarely used version control or debugging tools.

Working on the RTEMS project was a completely different experience. The large codebase challenged my existing knowledge, and I had to refine my understanding of Git, learn proper debugging techniques, write tests, and use test coverage tools. I also had to overcome bad coding habits and adhere to RTEMS coding standards to ensure my code was understandable to others.

My ability to read and understand code written by others has greatly improved. I now have a decent understanding of RTEMS' general structure and can follow discussions and understand which parts of the code are affected.

Overall, this project significantly enhanced my programming skills, teaching me the importance of writing clean, maintainable code and preparing me for future collaborative projects. I now feel more confident in tackling complex challenges within a professional codebase.

