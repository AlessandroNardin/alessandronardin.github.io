---
layout: post
title: "First Contribution: Reviewing Patches"
date: 2024-06-04
categories: [GSoC]
tags: [GSoC]
excerpt: "My first contribution to GSoC involved reviewing three patches sent by my mentor, Joel Sherrill."
author: Alessandro Nardin
---

During my participation in GSoC, my first contribution involved reviewing three patches sent by my mentor, Joel Sherrill (aka @DrRTEMS). I had to determine whether these patches were still relevant and should be merged or if they should be discarded.

The first patch involved a simple change in the header comment of `aio_read`. The comment seemed to have been copied from `aio_write`, as it still contained references to "write" instead of "read".

The second patch modified the content of `psxaio02.scn`. Initially, I was stuck because I had no idea what a `.scn` file was. After unsuccessfully searching online, I asked my mentor, who explained that it was a file containing the expected output of tests. Understanding this, I was able to evaluate the patch properly. The file had the wrong content because it included the output of a different test. The patch corrected this by adding the correct expected output.

The third patch was possibly the most significant. It refactored the method executed by the threads handling requests, extracting the request-handling part into a helper function. This made the method shorter and more readable.

All three patches were necessary, so I opened an issue and a merge request for each of them. Patches 1 and 2 were merged easily, with patch 2 requiring no additional work. For patch 1, I had to update the entire comment to Doxygen standards. Patch 3 required the most effort. Although the patch itself only needed the helper method to be made static, the `aio_misc.c` file did not comply with the RTEMS coding conventions. Consequently, I had to review the entire file and correct any errors. This was a tedious task, but it helped me better understand the coding and formatting conventions, which will hopefully prevent similar issues with my future code.
