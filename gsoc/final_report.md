---
layout: page
title: Google Summer of Code 2024 - Final Report
---


## Project Summary 

My project for the 2024 edition of Google Summer of Code was done in collaboration with the RTEMS Project. RTEMS (Real-Time Executive for Multiprocessor Systems) is a real-time operating system (RTOS) designed for embedded systems. (More information can be found on the [Project Page](https://www.rtems.org/))

The goal of my project was to improve the POSIX compliance of the OS, specifically by working on the Asynchronous Input/Output (AIO) interface. My objective was to correct behaviors that did not comply with POSIX specifications and to implement the missing features.

## My Contributions

Below, you'll find a table summarizing all completed and planned contributions. The status of each contribution is specified. 
The "Completed" status refers to contributions whose code has already been merged into the upstream repository. 
The "WIP" status refers to contributions for which some work has already been done but that are yet to be completed. 
"Not started" refers to those contributions for which work has not yet begun. 
Each contribution is also listed with the related Merge Requests (MR).

After the table, there is a short description of each contribution. For more detailed information about each contribution, you can refer to the blog posts linked in the table, which provide more insight and detail about the approach used for the solution and the difficulties encountered for each task.

| Contribution                                                        | Status      | Related MR                                                                | Blog Posts |
| :------------------------------------------------------------------ | :---------: | :------------------------------------------------------------------------ | :--------: |
| `Review and merge existing patches`                                   | `Completed`   | [`!40`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/40)-                                                                                      [`!41`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/41)-                                                                                      [`!42`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/42)      |  |
| `Correct the behavior of aio_return() and aio_error()`                | `Completed`   | [`!85`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/85)      |  |
| `Add support for O_DSYNC in aio_fsync()`                              | `Completed`   | [`!128`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/128)    |  |
| `Add notification at request completion`                              | `Completed`   | [`!118`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/118)    |  |
| `Implement lio_listio()`                                              | `WIP`         | [`!188`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/188)    | - |
| `Implement lio_listio()`                                              | `Not started` | [`!188`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/188)    | - |
| `Update documentation`                                                | `Completed`   | [`!56`](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/56)-                                                                                      [`!26`](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/26) |  |

### Review and merge existing patches
description

### Correct the behavior of aio_return() and aio_error()
description

### Add support for O_DSYNC in aio_fsync()
description

### Add notification at request completion
description

### Implement lio_listio()
description

### Update documentation
description


## What I learned

text


