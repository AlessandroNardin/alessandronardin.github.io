---
layout: project-homepage
title: Google Summer of Code 2024
summary: "Description of my Project for the Google Summer of COde edition 2024"
permalink: /projects/gsoc/
thumbnail: /resources/thumbnail.jpg
---

{% 
include banner.html 
class="banner-green" 
content= "The final report detailing the outcome of my GSoC project is now available [here](final_report)." 
%}

# Project Abstract

For the 2024 edition of Google Summer of Code, I had the opportunity to contribute to the **RTEMS Project** by working on the **POSIX Asynchronous I/O (AIO) Implementation**.

**[RTEMS](https://www.rtems.org/) (Real-Time Executive for Multiprocessor Systems)** is an open-source real-time operating system designed for embedded systems that require high reliability and precise timing. It is widely used in aerospace, medical, industrial, and automotive applications where deterministic behavior is critical.

The goal of my project was to enhance RTEMS' compliance with the **POSIX (Portable Operating System Interface)** standards by refining and completing its support for Asynchronous I/O (AIO). AIO allows input and output operations to be performed in the background, enabling applications to continue executing while waiting for I/O tasks to complete. By implementing this functionality, the project improves RTEMS' portability and makes it easier for developers to write POSIX-compliant applications that can run across multiple platforms with minimal modifications.


# Project Scope

The scope of this project includes refining and completing the implementation of the Asynchronous I/O interface (AIO) within RTEMS. Currently, the implementation lacks some methods and functionalities. The focus of the project will be on:

- Refactoring and completing the implementation of `aio_fsync()` and `aio_return()` methods.
- Implementing missing methods such as `io_listio()` and `aio_suspend()`.
- Enhancing AIO processing to improve readability and efficiency.

# Deliverables

### May 27 (Coding Begins)

- Setup for efficient coding and testing.
- Comprehensive understanding of the project area.
- Detailed plan for project execution.

### July 8 - 12 (Midterm Evaluation)

- Refactoring of AIO processing.
- Correcting deficiencies in existing methods.

### August 19 - 26 (Final Evaluation)

- Modification of message structure between `aio_*` functions and the server.
- Implementation of `lio_listio()` method.
- Implementation of `aio_suspend()` method.
- Testing to ensure correctness of implementations.

### August 31 (Final Results Announced)

- Documentation enhancement to cover all introduced features.

# Proposed Schedule

- **March 14 - March 24 (Application Period)**: Proposal drafting and submission.
- **March 26 - April 22 (Acceptance Waiting Period)**: Familiarization with RTEMS contribution process and filing of tickets for identified deficiencies.
- **April 23 - May 23 (Community Bonding Period)**: Project documentation and research.
- **May 24 - June 26 (First Half)**: Refactoring and correcting deficiencies in existing methods.
- **June 27 - August 23 (Second Half)**: Implementation of missing methods and testing.
- **August 31 (Final Results Announced)**: Documentation enhancement.

# References

- [aio(7) - POSIX specification](#)
- [aio_read(3) - POSIX specification](#)
- [aio_write(3) - POSIX specification](#)
- [aio_fsync(3) - POSIX specification](#)
- [aio_error(3) - POSIX specification](#)
- [aio_return(3) - POSIX specification](#)
- [aio_suspend(3) - POSIX specification](#)
- [aio_cancel(3) - POSIX specification](#)
- [lio_listio(3) - POSIX specification](#)
- [aio_init(3) - Linux man page](#)
