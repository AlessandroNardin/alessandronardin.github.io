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

After the table, there is a short description outlining the goal of each contribution. For more detailed information about each of them, you can refer to the blog posts linked in the table, which provide more insight and detail about the approach used for the solution and the difficulties encountered for each task.

| Contribution                                                        | Status      | Related MR                                                                | Blog Posts |
| :------------------------------------------------------------------ | :---------: | :------------------------------------------------------------------------ | :--------: |
| Review and merge existing patches                                   | Completed   | [!40](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/40)-                                                                                  [!41](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/41)-                                                                                  [!42](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/42)      | [link](https://alessandronardin.github.io/gsoc/2024/06/04/post1/) |
| Correct the behavior of aio_return() and aio_error()                | Completed   | [!85](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/85)      | [link](https://alessandronardin.github.io/gsoc/2024/06/25/post3/) |
| Add support for O_DSYNC in aio_fsync()                              | Completed   | [!128](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/128)    | [link]() |
| Add notification at request completion                              | Completed   | [!118](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/118)    | [link]() |
| Implement lio_listio()                                              | WIP         | [!188](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/188)    | - |
| Implement aio_suspend()                                             | Not started |                                                                           | - |
| Update documentation                                                | Completed   | [!56](https://gitlab.rtems.org/rtems/rtos/rtems/-/merge_requests/56)-                                                                                  [!26](https://gitlab.rtems.org/rtems/docs/rtems-docs/-/merge_requests/26) | [link](https://alessandronardin.github.io/gsoc/2024/06/11/post2/) |

### Review and merge existing patches
This was my first contribution to the project. I began by reviewing patches provided by my mentor to determine if they were still relevant and should be merged. This task didn't involve writing any code, except for correcting a few formatting errors. However, it was valuable in helping me learn the RTEMS project's workflow and familiarize myself with the contribution submission process.

### Correct the behavior of aio_return() and aio_error()
The goal of this part of the project was to correct the behavior of aio_return() and aio_error(). The issue was that these functions could be called multiple times for the same operation. This behavior violated POSIX specifications and needed to be corrected.

### Add support for O_DSYNC in aio_fsync()
The objective here was to add missing functionality to the aio_fsync() function. According to the specification, one of the function’s parameters can accept two values that specify the type of synchronization to be performed. However, the function only accepted one of these values, so it was necessary to add support for the other.

### Add notification at request completion
One of the features missing from the implementation was the notification of request completion. One of the fields of the aiocb (Asynchronous Input/Output Control Block) is a sigevent struct, which must be used to generate a notification, as outlined by the POSIX specifications. This field was being ignored by the implementation, so my task was to add the code that utilized this field.

### Implement lio_listio()
The goal of this part was to implement the missing lio_listio() method. The work on this task took longer than expected due to an error that took considerable time to resolve.

### Implement aio_suspend()
The goal of this part was to implement the missing aio_suspend() method. However, I was unable to start work on this task because finishing lio_listio() took longer than expected.

### Update documentation
This contribution covers all the merge requests I made to update the documentation, including both Doxygen comments and the RTEMS API Docs.


## What I learned

This experience has been an invaluable learning opportunity for me. Prior to this summer, my coding experience was limited to school and university projects. This meant I had only worked on small codebases, often entirely written by me. As a result, I rarely used version control programs since the code was typically used for a short period and then discarded. My experience with debugging tools was also limited, as the simple nature of the code I worked on allowed me to rely on print statements to diagnose and solve any errors.

Working on the RTEMS project was a completely different experience. The large scale of the codebase challenged my existing knowledge. I had to refine my understanding of Git to manage my project fork effectively and submit my work for review. I also had to learn proper debugging techniques to resolve the errors I encountered. Writing tests to verify my code’s functionality and using test coverage tools to measure how much of my code was tested were also new skills I developed. I had to overcome my bad coding habits and adhere to the RTEMS coding standards to ensure that the code I wrote was understandable to others.

I feel that my ability to read and understand code written by others, which I had rarely needed before, has greatly improved. When I started the application process, I couldn't even grasp the various project proposals listed by the organization. Now, after reading the documentation and working with the code, I have a decent understanding of the project's general structure. Even though my knowledge is primarily limited to the AIO interface, I can follow discussions by others and at least understand which part of the code is being affected.

Overall, this project has significantly enhanced my skills as a programmer, teaching me the importance of writing clean, maintainable code that can stand the test of time. I've gained experience in working on a large and collaborative project, which has pushed me to improve my technical abilities and my approach to collaboration. This summer has not only broadened my understanding of coding practices but has also prepared me to contribute more effectively to any future projects. I now feel more confident in my ability to tackle complex challenges and work within a professional codebase, skills that will certainly benefit me in the future.       


