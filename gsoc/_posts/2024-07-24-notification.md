---
layout: post
title: "Add notification at request completion"
date: 2024-07-24
categories: [GSoC]
tags: [GSoC]
excerpt: "Adding of notification via sigevent struct at request completion"
author: Alessandro Nardin
---

Another functionality that was missing from the original implementation was the generation of a notification upon request completion. Each `aiocbp` has the field `aio_sigevent` that specifies the type of notification that should occur when a request is completed. The implementation ignored this field and did not deliver any notification of completion.

To add support for this feature, I created two new functions:

- `rtems_aio_check_sigevent()`. This function is used to validate the content af a sigevent struct. The function is used inside the methods that enqueue requests, namely `aio_read()`, `aio_write()` and `aio_fsync()` to verify the correctness of the passed data. The function takes as pointer to a `sigevent` struct and then returns an integer. The value returned is `1` if the sigevent struct is valid, `0` otherwise.

- `rtems_aio_notify()`. This is the function that generated the notification. This function is called after each request has been processed, in the future i belive this function will also be used to generate a notification when a list of requests, enqueued with `lio_listio()`, is completed. This function takes as input pointer to a `sigevent struct` ( assumed to be not `NULL` ) and generates the notification. The notification is generated as specified by the [POSIX Specifications](https://pubs.opengroup.org/onlinepubs/9799919799/functions/V2_chap02.html#tag_16_04_01).

To verify that the code was working i added a new test, `psxaio04`.
`
To get feedback on the code and then merge the changes, I opened MR118. From the review process did not emerge major issues with my work, but my mentors ponted oput some aspecs taht could be improved. After fixing those issues and correcting every foratting error the code got merged.
