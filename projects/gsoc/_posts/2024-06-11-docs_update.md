---
layout: post
title: "Updating Doxygen Comments and API Guide"
date: 2024-06-11
categories: [GSoC]
tags: [GSoC]
excerpt: "I updated and converted all comments related to AIO to Doxygen, and also fixed formatting in related source files."
author: Alessandro Nardin
---

Since I had already modified some Doxygen comments during previous work, my mentor suggested that I update and convert all comments related to AIO to Doxygen. This task was not particularly complex but rather time-consuming. I also took this opportunity to fix the formatting in all the related source files.

I encountered a few difficulties during this process, mainly due to the frequent back-and-forth reviews needed to correct small formatting errors I had missed. Additionally, I had some trouble getting Doxygen to work correctly. Some errors were related to the BSPs documentation, which was outside the scope of my project, so I filtered them out from the Doxygen build. However, I still couldn't see the changes I made in `aio.h`.

After some research, I discovered the issue was because the code was put inside an `#if` clause, in particular:
```c
#if defined(_POSIX_ASYNCHRONOUS_IO)
#if defined(_POSIX_SYNCHRONIZED_IO)
```
When builing the Doxygen documentation, the file was preprocessed, and since the macros were not defined, the code was ignored. I considered 3 different solutions different solutions to solve the problem:
- Disable Preprocessing in the Doxygen configuration file.
- Predefine _POSIX_ASYNCHRONOUS_IO and _POSIX_SYNCHRONIZED_IO in the Doxygen configuration file.
- Define a DOXYGEN macro in the Doxygen configuration file and change the code to:
```c
#if defined(_POSIX_ASYNCHRONOUS_IO) || defined(DOXYGEN)
#if defined(_POSIX_SYNCHRONIZED_IO) || defined(DOXYGEN))
```

Ultimately, upon discussion with my mentors I decided to disable preprocessing when building the documentation.

Since I had updated the Doxygen documentation, I was also asked to update the API guide. For this, I partially reused the content I had written for the Doxygen documentation. This time, I had no problems building the documentation; following the instructions on the documentation page was sufficient.
