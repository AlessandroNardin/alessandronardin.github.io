---
layout: post
title: "Corrections to aio_return and aio_error"
date: 2024-06-25
categories: [GSoC]
tags: [GSoC]
excerpt: "Correcting the implementation of aio_return() and aio_error() to make it compliant to the POSIX specifications."
author: Alessandro Nardin
---

The first issue I tackled involved the implementation of `aio_return` and `aio_error`. According to the specification for `aio_return()`:

> "The aio_return() function may be called exactly once to retrieve the return status of a given asynchronous operation; thereafter, if the same aiocb structure is used in a call to aio_return() or aio_error(), an error may be returned. When the aiocb structure referred to by aiocbp is used to submit another asynchronous operation, then aio_return() may be successfully used to retrieve the return status of that operation."

This aspect was not considered in the initial implementation, where both methods simply returned a private field of the `aiocbp` structure. I solved the problem by adding a new private field to the `aiocb` struct, called `return_status`, to track whether a request associated with an `aiocb` has already been returned. `return_status` can have two values: `AIO_RETURNED` or `AIO_NOTRETURNED`.

I then modified the existing code in this way:
- In the `aio_enqueue()` method, I set `return_status` to `AIO_NOTRETURNED` so that every time a new request for an `aiocb` is enqueued, it can be returned.
- In `aio_error()`, I added a check for `return_status`. If `return_status` is `AIO_RETURNED`, the function returns an error. Otherwise, it returns the value of the `error_code` field.
- In `aio_return()`, I added a check like the one in `aio_error()`, with the additional step of setting `return_status` to `AIO_RETURNED` when returning the value in `return_value`.

During this modification, I also noticed that the methods lacked a NULL pointer check for the input, so I added these checks where necessary.

